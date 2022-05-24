# pyscript_ex
## 파이 스크립트 예제

**1. 개요**  

아나콘다에서 JS를 대체할 수 있는 새로운 파이썬 프로젝트를 시작한것 같다.


WASM 기반 인것 같으며, HTML에서 기존 파이썬의 문법을 그대로 쓸 수 있다.

파이썬으로 HTML의 DOM 을 제어 할 수 있어, 테스트 구현에 용이할 것으로 생각한다.

아직까지 알파버젼의 단계라 부족한 점이 분명히 있지만 꾸준히 지속성을 가지며 발전하면 재미있는 생태계가 만들어질것 같다.

함수 호출은 크게 두 가지 방식 모두 적용 될 수 있는걸 확인했다.  

로컬 환경에서 테스트시 python -m http.server 를 통해 서버를 열어놓고 테스트 하는것이 좋다.
  
<br>

**2. 사용법**

***1) head 태그 안에 두 태그를 삽입***
```html
        <link rel="stylesheet" href="https://unpkg.com/@picocss/pico@latest/css/pico.min.css" />
        <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> # css는 취향껏 설정 두번째가 파이스크립트 공식 css
        
        <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
```

<br>

***2) body 태그 안에 py-script 태그를 삽입***

```html
<body>
  <py-script> # 시작
    print('hello world') # 이 태그 안에선 파이썬의 문법이 적용된다.
  </py-script> # 끝
</body
```

<br>

***3) 기존 라이브러리 임포트***

```html
<body>
  <py-script>
     from datetime import datetime # py-scrpit 태그 내에서 임포트 할 수 있다.
  </py-script>
</body>
```

***4) py-env 태그의 사용법***  

기존의 파이썬 파일을 가져오거나 다른 모듈을 가져올 수 있다  
```html
<head>
  <py-env>
    - numpy
    - paths:
      - ./test.py
  </py-env>
</head>
```

<br>

***5) py-script 태그 내 src 삽입

html 내에 코딩을 하면 안 될때엔 아래와 같이 사용 된다.

```html
<body
  <py-script src='./test.py'></py-script>
</body>
```


**3. 함수 호출**

***1) pys-onClick 을 통한 html 에서 직접 함수 호출***
```html
<button id = 'input_btn' pys-onClick='test_func1' >전송</button>
```
<br>  


***2) .py 파일 내에서 함수 호출***
```python
def test_func1(*args):
    result.element.innerText = 'test'

number_input = Element('number_input')

result = Element('result')
input_btn = Element('input_btn')

input_btn.element.onclick = test_func
```
