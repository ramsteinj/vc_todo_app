# 06. 개발 계획

## Phase 1 — 프로젝트 기본 구조

목표:
Frontend, Backend 프로젝트를 만들고 PostgreSQL 연결을 구성한다.

작업:
- Django 프로젝트 생성
- Django REST Framework 설정
- Vue 3 + Vite 프로젝트 생성
- PostgreSQL 연결 설정
- 기본 환경 설정
- Git에 적합한 프로젝트 구조 생성

검증:
- Django 서버 실행
- Vue 개발 서버 실행
- PostgreSQL 연결 및 migration 확인

## Phase 2 — Backend Todo 모델

작업:
- Todo Model
- Migration
- Serializer
- API View
- API URL/Route
- Validation

검증:
- PostgreSQL을 대상으로 CRUD API 테스트

## Phase 3 — Backend 테스트

작업:
- 필요한 Model 테스트
- CRUD API 테스트
- Validation 테스트

검증:
- 테스트 전체 통과

## Phase 4 — Frontend 조회

작업:
- Todo 목록 화면
- API 호출 모듈
- Loading 상태
- Error 상태

검증:
- 실제 PostgreSQL 데이터가 Django API를 거쳐 화면에 표시되는지 확인

## Phase 5 — Frontend 쓰기 기능

다음 순서로 하나씩 구현한다.

1. Todo 생성
2. Todo 수정
3. 완료/미완료 변경
4. Todo 삭제

각 기능 구현 후:
- 애플리케이션 실행
- 기능 테스트
- 기존 기능 Regression 확인
- 문제 발생 시 수정

## Phase 6 — 통합 및 UX 개선

작업:
- 입력 검증 메시지 개선
- Loading 상태 개선
- 오류 처리 개선
- Responsive CSS
- 기본적인 UI/UX 정리

## Phase 7 — 최종 검증

작업:
- 전체 테스트 실행
- 전체 CRUD 흐름 검증
- 문서대로 프로젝트를 처음부터 실행할 수 있는지 확인
- 요구사항과 실제 구현 비교
- README 업데이트
- 불필요한 코드 및 의존성 제거

## Vibe Coding 규칙

전체 애플리케이션을 한 번에 구현하도록 요청하지 않는다.

하나의 요청은 작고 독립적으로 검증할 수 있는 작업 단위로 제한한다.
