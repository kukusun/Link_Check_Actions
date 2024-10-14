name: Check Redirects

on:
  schedule:
    - cron: '0 19 * * *'  # 每天中国上海时间晚上3点运行一次
  workflow_dispatch:

jobs:
  check:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests

    - name: Run redirect checker
      run: |
        python check_redirects.py

    - name: Check if results file is empty
      id: check_results
      run: |
        if [ ! -s check_results.md ]; then
          echo "results_empty=true" >> $GITHUB_ENV
        else
          echo "results_empty=false" >> $GITHUB_ENV
        fi

    - name: Commit results
      if: env.results_empty == 'false'
      run: |
        DATE=$(TZ='Asia/Shanghai' date +'%Y年%m月%d日%H时%M分')
        if [ "${{ github.event_name }}" = "workflow_dispatch" ]; then
          FILENAME="results/[Manual]check_results_$DATE.md"
        else
          FILENAME="results/[Actions]check_results_$DATE.md"
        fi
        mv check_results.md $FILENAME
        git config --global user.name 'github-actions'
        git config --global user.email 'github-actions@github.com'
        git add $FILENAME
        git commit -m "Update check results for $DATE"
        git push

    - name: Send email with results
      if: env.results_empty == 'false'
      uses: actions/github-script@v6
      with:
        script: |
          const fs = require('fs');
          const nodemailer = require('nodemailer');
          const results = fs.readFileSync('check_results.md', 'utf8');
          const fileName = path.basename('check_results.md');
          let transporter = nodemailer.createTransport({
            service: 'outlook',
            auth: {
              user: process.env.EMAIL_USER,
              pass: process.env.EMAIL_PASSWORD
            }
          });

          let mailOptions = {
            from: 'your-email@gmail.com',
            to: 'kukusun@outlook.com',
            subject: '链接检测结果：${fileName}',
            text: results
          };

          transporter.sendMail(mailOptions, function(error, info){
            if (error) {
              console.log(error);
            } else {
              console.log('Email sent: ' + info.response);
            }
          });
      env:
        EMAIL_USER: ${{ secrets.EMAIL_USER }}
        EMAIL_PASSWORD: ${{ secrets.EMAIL_PASSWORD }}
