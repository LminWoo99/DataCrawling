#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 14:39:53 2023

@author: imin-u
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from bs4 import BeautifulSoup


# ChromeDriver 경로 설정
path_to_chromedriver = '/usr/local/bin/chromedriver'

# Chrome WebDriver 생성
driver = webdriver.Chrome(path_to_chromedriver)

# 웹 페이지로 이동
driver.get('https://taas.koroad.or.kr/sta/acs/exs/typical.do?menuId=WEB_KMP_OVT_UAS_ASA#')

# Selenium을 사용하여 JavaScript 실행을 기다림
driver.implicitly_wait(10)

# 웹 페이지의 HTML 가져오기
html = driver.page_source

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 테이블 찾기
table = soup.find('table', class_='tbl_st02')

if table:
    # 테이블 내용 출력
    print(table.prettify())
else:
    print("테이블을 찾을 수 없습니다.")

# WebDriver 종료
driver.quit()




df=pd.read_csv("/Users/imin-u/Desktop/school/23년 1학기/기계학습/도로교통공단_요일별 시간대별 교통사고 통계_20211231.csv", encoding='cp949')
df
df.head()
df.info()
#데이터 전처리
df2=df.copy()
df2.isnull().sum()

label={'월':'Mon','화':'Tue','수':"Wen",'목':'Thur','금': 'Fri','토':'Sat', '일':'Sun'}
df["요일"]=df["요일"].map(label)
car=df.groupby("요일").sum()

car=car.sort_values(by='사고건수', ascending=False)
car_time=df.groupby("시간대").sum()
car_time=car_time.sort_values(by='사고건수', ascending=False)

friday_data = df[df["요일"] == 'Fri']

friday_data.sort_values(by='사고건수', ascending=False)

wendseday_data = df[df["요일"] == 'Wen']
wendseday_data.sort_values(by='사고건수', ascending=False)

ctable=df.groupby("요일")["사고건수"].sum()

#데이터 시각화
#요일별 사고건수
plt.pie(ctable.values, labels=ctable.index, autopct='%1.1f%%' )
plt.title("Number of accidents by day of the week")

plt.figure()
'''
'''
sns.barplot(x="요일", y="사고건수", data=df)
plt.figure()
'''
'''

sns.barplot(x="시간대", y="사고건수", data=friday_data)
plt.title("Friday Number of accidents by time")
plt.xlabel("Time Zone")
plt.ylabel("Number of accidents")
plt.figure()

sns.barplot(x="시간대", y="사고건수", data=wendseday_data)
plt.title("Wenseday Number of accidents by time")
plt.xlabel("Time Zone")
plt.ylabel("Number of accidents")
car
'''