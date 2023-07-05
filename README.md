# DataCrawling
네이버 항공권 크롤링을 통해 가격 조회
# 웹 크롤링 (ver 1.0)

<p>주요 동작</p>
<p>네이버 항공권 조회 접속 -> 출발지, 도착지 변경 -> 날짜 변경 -> 항공기 번호, 날짜, 시간, 임시저장</p>
<hr>
<p>사용 라이브러리</p>
<p>pandas 1.5.3<br>matplotlib 3.7.0<br>selenium  4.9.1</p>
<hr>
<h3><p>동작 설명</p></h3>
<p>1. 드라이버 경로</p>

```
driver = webdriver.Chrome(path_to_chromedriver)
```


<p>2. URL 이동</p>

```
driver.get(url)
```

<p>3. 클릭</p>

```
driver.find_element(By.CSS_SELECTOR, '.tabContent_route__1GI8F.select_City__2NOOZ.start').click()  
```

<p>4. 입력</p>

```
driver.find_element(By.XPATH, '//button[text() = "국내"]').click()
driver.find_element(By.XPATH, '//i[text() = "김해국제공항"]').click()  # 출착지
```

<p>5. 입력 </p>

```
driver.find_element(By.XPATH, '//button[text() = "국내"]').click()
driver.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]').click() #도착지
```
<p>6. 입력 </p>

```
driver.find_element(By.XPATH, '//button[text() = "가는 날"]').click()
driver.find_element(By.XPATH, '//b[text() = "20"]').click()
driver.find_element(By.XPATH, '//b[text() = "24"]').click()  #날짜 선택

```

<p>7. 자바스크립스 사용(스크롤 제)</p>

```
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if last_height == new_height:
        break
    last_height = new_height
```


<p>8. 파일첨부</p>

```
flight_list = driver.find_elements(By.CSS_SELECTOR, '.domestic_Flight__sK0eA.result')
```
<p>9. 크롤링한 데이터 전처라</p>

```
def preprocess_price(price):
    numbers = re.findall(r'\d+', price)
    
    if len(numbers) > 0:
        price_number = ''.join(numbers)
        
        try:
            price_int = int(price_number)
            return price_int
        except ValueError:
            return None
    else:
        return None
df['가격'] = df['가격'].apply(preprocess_price)
```
<p>10.비행기 종류별로 그룹화</p>

```
grouped_df = cheap_air.groupby('항공사').head(10)
airline_avg=df.groupby('항공사')
plt.rcParams['font.family'] = 'AppleGothic'


```
<p>11.상위 10개 비행기표 막대 그래프 그리기</p>

```
grouped_df = cheap_air.groupby('항공사').head(10)
airline_avg=df.groupby('항공사')
plt.rcParams['font.family'] = 'AppleGothic'
# x축 레이블 설정
plt.xticks(x, range(len(grouped_df)))

# 그래프 제목 및 축 레이블 설정
plt.title('상위 10개 비행편')
plt.xlabel('비행기 인덱스 번호')
plt.ylabel('가격')

# 그래프 출력
plt.show()


```
<p>12.원도표 시각화</p>

```
# 항공사별 비행편 수 계산
flight_counts = df['항공사'].value_counts()
print(flight_counts)
plt.figure()

# 시각화
plt.pie(flight_counts, labels=flight_counts.index, autopct='%1.1f%%')
plt.title('항공사별 비행편 수')

# 항공사명 추가
plt.legend(flight_counts.index, loc='upper right')

plt.axis('equal')  # 원을 원형으로 유지
plt.show()


```
<h2>시각화 자료(링크 참조)</h2>

[막대그래프](https://github.com/LminWoo99/DataCrawling/blob/main/그래프.png)
<br>
[원도표](https://github.com/LminWoo99/DataCrawling/blob/main/원도표.png)
 
