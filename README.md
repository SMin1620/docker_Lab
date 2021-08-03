# Docker_Practice
Django-MariaDB 프로그램을 Docker를 통해 로컬에서 구동해보는 template/practice codes

> docker compose up -d
> docker ps 
> django와 mariadb 컨테이너가 잘 돌아가는지 확인
> 둘 중 하나가 없다면 수동으로 재시작.
> localhost:8000/stockapp/chart/  로 접속

## 메인 화면

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/68914294/128065841-e5a07c38-1624-4bbf-b9b6-0e1d4a2af098.png">


- django 파일은 중요하지 않다.
* host에 bind된 database 폴더에 테이블과 데이터베이스가 잘 생성되었는지 확인 가능
* docker exec을 통해서 mariadb의 데이터가 원활히 추가되고 삭제되는지 확인 가능


> produced by hyun98
