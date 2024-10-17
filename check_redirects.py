import requests

# 在这里添加你收藏的链接
urls = [
    "https://kukusun.github.io/blog/",
    "https://tmp-hd106.vx-cdn.com/file-670fadd53483d-670fae4b71ea3/Windows6.1-KB3102810-x64.msu",
    "https://kukusun.github.io/blog",
    "https://potplayer.daum.net",
    "https://github.com/rozbo/hexo-neat",
    "https://learn.microsoft.com/zh-cn/windows/deployment/upgrade/windows-10-edition-upgrades",
    "https://learn.microsoft.com/zh-cn/windows/deployment/upgrade/windows-edition-upgrades",
    "https://learn.microsoft.com/zh-cn/windows/deployment/upgrade/windows-edition-upgrades-aabb",
    "https://httpstat.us/100",
    "https://httpstat.us/101",
    "https://httpstat.us/102",
    "https://httpstat.us/103",
    "https://httpstat.us/200",
    "https://httpstat.us/201",
    "https://httpstat.us/202",
    "https://httpstat.us/203",
    "https://httpstat.us/204",
    "https://httpstat.us/205",
    "https://httpstat.us/206",
    "https://httpstat.us/207",
    "https://httpstat.us/208",
    "https://httpstat.us/226",
    "https://httpstat.us/300",
    "https://httpstat.us/301",
    "https://httpstat.us/302",
    "https://httpstat.us/303",
    "https://httpstat.us/304",
    "https://httpstat.us/305",
    "https://httpstat.us/306",
    "https://httpstat.us/307",
    "https://httpstat.us/308",
    "https://httpstat.us/400",
    "https://httpstat.us/401",
    "https://httpstat.us/402",
    "https://httpstat.us/403",
    "https://httpstat.us/404",
    "https://httpstat.us/405",
    "https://httpstat.us/406",
    "https://httpstat.us/407",
    "https://httpstat.us/408",
    "https://httpstat.us/409",
    "https://httpstat.us/410",
    "https://httpstat.us/411",
    "https://httpstat.us/412",
    "https://httpstat.us/413",
    "https://httpstat.us/414",
    "https://httpstat.us/415",
    "https://httpstat.us/416",
    "https://httpstat.us/417",
    "https://httpstat.us/418",
    "https://httpstat.us/421",
    "https://httpstat.us/422",
    "https://httpstat.us/423",
    "https://httpstat.us/424",
    "https://httpstat.us/425",
    "https://httpstat.us/426",
    "https://httpstat.us/428",
    "https://httpstat.us/429",
    "https://httpstat.us/431",
    "https://httpstat.us/451",
    "https://httpstat.us/500",
    "https://httpstat.us/501",
    "https://httpstat.us/502",
    "https://httpstat.us/503",
    "https://httpstat.us/504",
    "https://httpstat.us/505",
    "https://httpstat.us/506",
    "https://httpstat.us/507",
    "https://httpstat.us/508",
    "https://httpstat.us/510",
    "https://httpstat.us/511",
    "https://httpstat.us/419",
    "https://httpstat.us/420",
    "https://httpstat.us/440",
    "https://httpstat.us/444",
    "https://httpstat.us/449",
    "https://httpstat.us/450",
    "https://httpstat.us/460",
    "https://httpstat.us/463",
    "https://httpstat.us/494",
    "https://httpstat.us/495",
    "https://httpstat.us/496",
    "https://httpstat.us/497",
    "https://httpstat.us/498",
    "https://httpstat.us/499",
    "https://httpstat.us/520",
    "https://httpstat.us/521",
    "https://httpstat.us/522",
    "https://httpstat.us/523",
    "https://httpstat.us/524",
    "https://httpstat.us/525",
    "https://httpstat.us/526",
    "https://httpstat.us/527",
    "https://httpstat.us/530",
    "https://httpstat.us/561"
]

def check_urls(urls):
    results = []
    for url in urls:
        try:
            response = requests.get(url, allow_redirects=True, headers={"Cache-Control": "no-cache"})
            final_url = response.url.rstrip('/')
            original_url = url.rstrip('/')

            if response.history and final_url != original_url:
                redirect_info = f"{url} (· 重定向到 {response.url} ·)\n(· 重定向过程"
                for resp in response.history:
                    redirect_info += f" ---> 状态码: {resp.status_code}, URL: {resp.url}"
                redirect_info += f" ---> 最终请求状态码: {response.status_code}, URL: {response.url} ·)"
                results.append(redirect_info)
            elif response.status_code != 200:
                results.append(f"{url} (· 无效，状态码: {response.status_code} ·)")
            # 注释掉正常的输出
            # elif response.status_code == 200:
            #     results.append(f"{url} (· 有效 ·)")
        except requests.RequestException as e:
            results.append(f"{url} (· 检查时出错: {e} ·)")
    return results

if __name__ == "__main__":
    results = check_urls(urls)
    with open("check_results.md", "w", encoding="utf-8") as f:
        for result in results:
            f.write(result + "\n")
