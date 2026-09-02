# 01. 프로젝트 개요

## 프로젝트 목적

간단한 Todo 관리 Web Application을 개발한다.

이 프로젝트는 OpenCode + GLM-5.3 Flash를 이용한 Markdown 우선 Vibe Coding 개발 방식을 실제로 경험하기 위한 학습 프로젝트이다.

개발자는 Markdown 문서로 제품 요구사항과 기술적 제약을 먼저 정의한다. 이후 OpenCode + GLM-5.3 Flash가 이 문서를 기반으로 프로젝트를 단계적으로 구현한다.

## 해결하려는 문제

사용자가 일상적인 할 일을 간단한 Web UI에서 관리할 수 있어야 한다.

## 대상 사용자

개인 사용자 한 명을 대상으로 한다.

MVP에서는 로그인, 회원가입 및 다중 사용자 기능을 구현하지 않는다.

## 핵심 가치

- Todo를 빠르게 생성할 수 있다.
- 해야 할 일을 한눈에 확인할 수 있다.
- Todo를 완료 처리할 수 있다.
- Todo를 쉽게 수정하거나 삭제할 수 있다.

## 주요 사용자 시나리오

### Todo 생성

1. 사용자가 Todo 제목과 선택적인 설명을 입력한다.
2. 생성 버튼을 클릭한다.
3. Frontend가 Django REST API를 호출한다.
4. Django가 PostgreSQL에 Todo를 저장한다.
5. 새 Todo가 목록에 표시된다.

### Todo 조회

1. 사용자가 Web App에 접속한다.
2. Frontend가 Django API를 호출한다.
3. 저장된 Todo 목록을 가져온다.
4. 화면에 Todo 목록을 표시한다.

### Todo 완료

1. 사용자가 Todo의 완료 상태를 변경한다.
2. Frontend가 Django API를 호출한다.
3. Django가 completed 값을 변경한다.
4. 변경된 상태가 화면에 반영된다.

### Todo 수정

1. 사용자가 Todo의 제목 또는 설명을 수정한다.
2. Frontend가 Django API를 호출한다.
3. Django가 데이터를 저장한다.
4. 변경된 내용이 화면에 반영된다.

### Todo 삭제

1. 사용자가 삭제 버튼을 클릭한다.
2. Frontend가 DELETE API를 호출한다.
3. Django가 해당 Todo를 삭제한다.
4. 목록에서 Todo가 제거된다.

## MVP 범위

### 포함

- Todo CRUD
- 완료/미완료 변경
- PostgreSQL 데이터 저장
- Vue.js Web UI
- Django REST API

### 제외

- 인증
- 사용자 계정
- Todo 공유
- 알림
- 파일 첨부
- 통계
- Native Mobile App
