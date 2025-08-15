import requests

# 创建会话
session = requests.Session()

# 访问目标网页
response = session.get('https://www.goofish.com/')

# 获取Cookies(字典形式)
cookies_dict = session.cookies.get_dict()
print(cookies_dict)

# 获取原始Cookies字符串
cookies_str = '; '.join([f'{k}={v}' for k, v in cookies_dict.items()])
print(cookies_str)