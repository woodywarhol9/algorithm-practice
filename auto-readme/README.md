# Github Actions을 활용한 README 업데이트 자동화
알고리즘 풀이 내역을 `README`로 저장하고 관리합니다.
`README`에 활용될 문제 정보는 필요에 따라 비동기 크롤링됩니다.
최초 `README` 생성 이후 풀이가 추가될 경우, `Github Actions`을 통해 자동으로 `README`가 업데이트됩니다.

### Project Structure
---
```
|-- crawler.py
|-- create_readme.py
|-- problem_info
|-- src
|   |-- 0.svg
|   |-- 1.svg
...
|   |-- 30.svg
|   |-- 31.svg
`-- update_readme.py
```

- `crawler.py` : Baekjoon, Programmers 등 에서 문제 정보를 받아옵니다.
- `create_readme.py` : 문제 정보를 바탕으로 초기 `README` 파일을 작성합니다.
- `update_readme.py` : 새로 `push`된 파일로 `README` 파일을 업데이트합니다.

</br>

### How to use
---
1. 초기 `README` 작성
`create_readme.py`를 실행 해, 기존 저장된 풀이를 활용해 `README`를 작성합니다. 
이후 작성이 끝난 `README`를 원격 저장소에 `push`합니다.

</br>


2. `README` 업데이트
새로운 풀이 파일을 `push` 하면 `README`업데이트가 자동으로 진행됩니다.
`Github Actions`가 `update_readme.py`가 자동으로 실행합니다.