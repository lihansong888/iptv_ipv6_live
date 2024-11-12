import requests

def fetch_and_filter():
    url = 'https://iptv.b2og.com/txt/fmml_ipv6.txt'
    
    # 获取文件内容
    response = requests.get(url)
    content = response.text
    
    # 过滤掉包含 "ipv6" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv4' not in line.lower()]
    
    # 保存到新文件
    with open('live_ipv4.txt', 'w') as file:
        file.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    fetch_and_filter()
