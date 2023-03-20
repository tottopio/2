# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#import requests
#import datetime

# ブラウザを開く。
driver = webdriver.Chrome("C:/Users/cococ/OneDrive/デスクトップ/chromedriver_win32/chromedriver.exe")
# Googleの検索TOP画面を開く。
driver.get("https://std.ishikawa-nct.ac.jp/")
# 1秒待機
time.sleep(1)
#ユーザーid入力
userID = driver.find_element_by_id("login-user")
userID.clear()
userID.send_keys("userID")
# 1秒待機
time.sleep(1)
#パスワード入力
userpass = driver.find_element_by_id("login-password")
userpass.clear()
userpass.send_keys("password")
#ログインボタンをクリック
login_btn = driver.find_element_by_xpath("/html/body/form/div[2]/div[3]/input")
login_btn.click()
#36.9クリック
taicho_btn = driver.find_element_by_xpath("/html/body/main/form/div[1]/div/div[1]/label")
taicho_btn.click()

#1秒待機
#time.sleep(100)



#報告ボタンクリック
report_btn = driver.find_element_by_xpath("/html/body/main/form/div[3]/button")
report_btn.click()

#time = datetime.datetime.now()
#time = time.strftime('%Y年%m月%d日 %H:%M:%S')

#TOKEN = 'MYTOKEN'
#api_url = 'https://notify-api.line.me/api/notify'
#時刻を送る内容の変数に設定
#send_contents = time

#TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
#send_dic = {'message': send_contents}
#requests.post(api_url, headers=TOKEN_dic, data=send_dic)

#1秒待機
time.sleep(1)
driver.close()
driver.quit()
