# Todo App 프로젝트 명세서

## 1. 프로젝트 개요

- 프로젝트명: Todo App
- 목적: OpenCode + GLM-5.3 Flash를 이용한 Markdown 우선 Vibe Coding 개발 방식 학습
- MVP 목표: 개인이 사용할 수 있는 간단한 Todo 관리 Web Application

## 2. 기준 문서

이 저장소의 Markdown 문서는 프로젝트가 만들어야 할 제품과 기술적 제약을 정의한다.

의사결정 우선순위:
1. 이 저장소에 명시된 요구사항
2. 아키텍처 및 기술 제약
3. 개발 계획
4. 기존 구현 내용

요구사항에 없는 기능은 임의로 추가하지 않는다. 필요한 경우 먼저 사용자에게 확인한다.

## 3. 기술 요구사항

### Frontend
- Vue.js 3
- Vite
- JavaScript
- HTML5
- CSS3
- SPA(Single Page Application)

### Backend
- Python 3
- Django
- Django ORM
- Django REST Framework
- REST/JSON API

### Database
- PostgreSQL

### 개발 환경
- Git
- OpenCode
- GLM-5.3 Flash

## 4. 아키텍처

Vue.js SPA
    |
    | HTTP / JSON
    v
Django REST Framework
    |
    | Django ORM
    v
PostgreSQL

규칙:
- Vue Frontend는 REST API를 통해 Django Backend와 통신한다.
- Frontend가 PostgreSQL에 직접 접속해서는 안 된다.
- 데이터 저장 및 핵심 Backend 처리는 Django가 담당한다.
- Frontend와 Backend는 논리적으로 분리한다.

## 5. MVP 기능

- Todo 생성
- Todo 목록 조회
- Todo 상세 조회
- Todo 수정
- Todo 완료/미완료 변경
- Todo 삭제
- PostgreSQL에 데이터 저장

MVP에서 제외:
- 로그인
- 회원가입
- 사용자 계정
- 소셜 로그인
- Todo 공유
- 알림
- 파일 첨부
- 통계 및 분석
- Native Mobile App

## 6. Todo 데이터

- id
- title
- description
- completed
- created_at
- updated_at

제약사항:
- title은 필수이다.
- completed의 기본값은 false이다.
- 시간 정보는 서버에서 관리한다.

## 7. API 명세

GET    /api/todos/
POST   /api/todos/
GET    /api/todos/{id}/
PUT    /api/todos/{id}/
PATCH  /api/todos/{id}/
DELETE /api/todos/{id}/

요청 및 응답은 필요한 경우 JSON을 사용한다.

## 8. MVP 완료 기준

다음 조건을 모두 만족하면 MVP 완료로 간주한다.

- PostgreSQL 연결이 정상적으로 동작한다.
- Django migration이 정상적으로 실행된다.
- Todo CRUD API가 정상적으로 동작한다.
- Vue에서 Todo 생성, 조회, 수정, 완료/미완료, 삭제가 가능하다.
- Frontend 데이터는 Django API를 통해 가져온다.
- 기본적인 입력 검증 및 오류 처리가 구현되어 있다.
- 중요한 Backend/API 동작에 대한 자동 테스트가 통과한다.
- README에 로컬 개발환경 설치 및 실행 방법이 작성되어 있다.
- 새로 받은 프로젝트에서도 문서에 적힌 방법으로 실행할 수 있다.
