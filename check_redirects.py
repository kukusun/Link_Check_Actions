import requests

# 在这里添加你收藏的链接
urls = [
    "https://potplayer.daum.net"
]

def check_urls(urls):
    results = []
    for url in urls:
        try:
            response = requests.head(url, allow_redirects=True)
            if response.status_code == 200:
                if response.url.rstrip('/') != url.rstrip('/'):
                    results.append(f"{url} redirects to {response.url} (重定向到 {response.url})")
                # 有效我注释掉了，我只需要它向我输出有问题的结果
                # else:
                    # results.append(f"{url} is valid. (有效)")
            else:
                results.append(f"{url} is not valid. Status code: {response.status_code} (无效，状态码: {response.status_code})")
        except requests.RequestException as e:
            results.append(f"Error checking {url}: {e} (检查 {url} 时出错: {e})")
    return results

if __name__ == "__main__":
    results = check_urls(urls)
    with open("check_results.md", "w") as f:
        for result in results:
            f.write(result + "\n")
