import time
import requests
from selenium import webdriver
from fake_useragent import UserAgent

def login_selenium():
    try:
        browser = webdriver.Chrome()
        # 需要安装chrome driver, 和浏览器版本保持一致
        # http://chromedriver.storage.googleapis.com/index.html
        
        login_url = 'https://shimo.im/login?from=home'
        browser.get(login_url)
        time.sleep(1)

        browser.find_element_by_xpath('//div[@class="input"]/input[@type="text"]').send_keys('827755806@qq.com')
        # 此处密码隐藏，实测通过
        browser.find_element_by_xpath('//div[@class="input"]/input[@type="password"]').send_keys('******')
        time.sleep(1)
        browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()

        cookies = browser.get_cookies() # 获取cookies
        print(cookies)
        time.sleep(3)

    except Exception as e:
        print(e)
    finally:    
        browser.close()

def login_request():
    ua = UserAgent(verify_ssl=False)
    headers = {
    'User-Agent' : ua.random,
    'Referer' : 'https://shimo.im/login'
    }
    # 用户名和密码隐藏掉
    form_data = {
    'email':'*******',
    'mobile':'',
    'password':'*******'
    }
    s = requests.Session()

    # post数据前获取cookie
    pre_login = 'https://shimo.im/login?from=home'
    pre_resp = s.get(pre_login, headers=headers)
    print(pre_resp.status_code)
    # print(s.cookies)

    # post用户名和密码
    login_url = 'https://shimo.im/lizard-api/auth/password/login'
    response = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)
    # print(response.text)

def test():
    r = requests.get('https://shimo.im/login?from=home')
    print(r.status_code)
    print(r.headers['content-type'])

if __name__ == "__main__":
    login_request()
    login_selenium()