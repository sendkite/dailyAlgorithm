## 알고리즘 연습 🔥🔥🔥

+ python
  + 1215 : 백준 2884 - if 문 (알림시계)
    + 출처 : https://www.acmicpc.net/problem/2884
    + 풀이
      1) 두개 값 입력 받기
      2) 두개 값 유효성 확인
      3) 45분 이전 시간 연산 (입력 분 - 45분가 음수면? 시간이 0이면?) 
      4) 출력
    + 소요시간 : 32분 
    + 기록하고 싶은 것 : 
      + Map 함수 이용해서 입력 받기
      + input() 2번 각각 입력 받으니 런타임 에러로 한참 고민. 
      ```python
      a, b = map(int, input().split())
      ```
  + 1216: 백준 2588- 곱셈
    + 풀이
      + 세자리수 2개 입력 
      + 두번째 입력값 100의 자리, 10의 자리, 1의 자리 분리
      + 각 자리수의 곱셈 결과값 출력
    + 소요시간 : 50분
    + 기록하고 싶은 것 
      + 처음 입력값을 아래로 받고 //, % 연산자를 이용해서 자리수 분리 시도함
      ```python
      a, b = map(int, input().split())
      ```
      + IDE에서는 정상 작동했지만 백준 web에서는 런타임 오류.
      + 연산을 바꿔보고 변수 선언을 없애보고 다양하게 시도
      + 결과적으로는 2번째 입력값을 string으로 받아서 글짜로 접근한 뒤에 형변환하여 성공.
    
    
    

