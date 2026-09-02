# 02. 아키텍처

## 시스템 아키텍처

Vue.js SPA
    |
    | HTTP / JSON
    v
Django REST Framework
    |
    | Django ORM
    v
PostgreSQL

## Frontend

### 담당 기능

- Todo UI 표시
- 사용자 입력 처리
- REST API 호출
- 로딩 상태 표시
- 오류 상태 표시
- API 결과에 따른 화면 갱신

Frontend는 데이터베이스에 직접 접근하지 않는다.

## Backend

### 담당 기능

- REST API 제공
- 입력값 검증
- 애플리케이션 로직 처리
- Todo 데이터 조회 및 저장
- 적절한 HTTP 상태 코드 반환
- JSON 응답 제공

## Database

PostgreSQL을 영구 데이터 저장소로 사용한다.

애플리케이션에서는 Django ORM을 통해 PostgreSQL에 접근한다.

## 초기 프로젝트 구조

backend/
  manage.py
  project/
  todos/

frontend/
  package.json
  src/

docs/
PROJECT.md
AGENTS.md
README.md

실제 생성되는 Django 프로젝트/앱 이름은 Django 관례에 따라 조정할 수 있다. 단, Frontend, Backend, docs의 논리적 분리는 유지한다.

## 아키텍처 원칙

- MVP는 단순하게 유지한다.
- 각 프레임워크의 일반적인 관례를 우선한다.
- 불필요한 추상화를 만들지 않는다.
- API 계약을 명확하게 유지한다.
- Vue 컴포넌트가 Django 내부 구현에 직접 의존하지 않도록 한다.
- Frontend와 Backend 사이의 통신은 REST/JSON API로 제한한다.
