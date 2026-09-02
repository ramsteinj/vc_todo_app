# AGENTS.md

## 이 저장소의 성격

- 코드가 없는 Markdown 우선 프로젝트이다. 모든 구현은 `PROJECT.md`(기준 문서)와 `docs/` 명세에 근거한다. 명세에 없는 기능을 추측해 구현하지 않고, 필요하면 먼저 사용자에게 묻는다.
- 우선순위(PROJECT.md §2): 저장소 요구사항 > 아키텍처/기술 제약 > 개발 계획 > 기존 구현.
- 모든 문서는 한국어로 작성되어 있다. 문서를 추가하거나 수정할 때도 한국어를 유지한다.
- `README.md`는 사람 전용 문서이며 agent 지침이 아니다. MVP 완료 기준(PROJECT.md §8)에 "README에 설치/실행 방법 작성"이 포함되므로, 구현이 시작되면 README를 실제 실행 방법으로 채워야 한다.
- 문서 지도: docs/01 개요·시나리오, docs/02 아키텍처·구조, docs/03 기술 스택, docs/04 기능 요구사항(R-001~R-009), docs/05 데이터 모델, docs/06 개발 계획(Phase 1~7).

## 아키텍처와 목표 구조 (docs/02)

- Vue 3 + Vite SPA ↔ Django + Django REST Framework ↔ PostgreSQL. 통신은 REST/JSON뿐이며 Frontend에서 DB 직접 접근 금지.
- 목표 구조: `backend/`(manage.py, project/, todos/), `frontend/`(package.json, src/), `docs/`. Django 프로젝트/앱 이름은 관례에 맞게 조정할 수 있으나 세 영역의 분리는 유지한다.
- 지정된 Framework/DB를 다른 기술로 교체하지 않는다. 명시적으로 승인되지 않은 새 framework, 라이브러리, 상태관리/UI 라이브러리를 추가하지 않고, 기존 framework 기능을 우선 사용한다(docs/03).

## API와 데이터 모델 (PROJECT.md §6-7, docs/05)

- Endpoint: `/api/todos/`(GET, POST), `/api/todos/{id}/`(GET, PUT, PATCH, DELETE). 경로를 임의로 바꾸지 않는다.
- Todo 필드: id, title(필수), description(선택, 기본 빈 문자열), completed(기본 false), created_at/updated_at(서버 관리).
- 입력 검증(R-007): title이 비어 있으면 거부하고, 잘못된 입력에는 적절한 오류 응답을 반환한다. API 실패 시 Frontend에 이해하기 쉬운 오류 메시지를 표시한다.
- 인증, 회원가입, 사용자 계정, 공유, 알림, 파일 첨부, 통계, 모바일 앱은 MVP에서 제외이다. 특히 인증/권한 기능은 명시적으로 요청되지 않는 한 추가하지 않는다.

## 작업 방식

- docs/06의 Phase 순서를 따른다. 한 요청은 작고 독립적으로 검증 가능한 단위로 제한하고, 전체 앱을 한 번에 구현하지 않는다. 관련 없는 기능을 함께 구현하지 않는다.
- 여러 파일을 변경하거나 아키텍처에 영향을 주는 작업은 먼저 계획(구현 방법, 대상 파일, 검증 방법, 사용자 결정 사항)을 세운다.
- 스키마 변경은 Django migration으로만 관리한다. PostgreSQL 스키마를 수동으로 수정하지 않는다.
- 검증: Backend 변경 후 관련 Django 테스트, API 변경 후 영향받는 endpoint, Frontend 변경 후 build/check와 가능하면 실제 UI를 확인한다. 실행하지 않은 테스트를 통과했다고 보고하지 않는다.
- 오류가 발생하면 코드를 고치기 전에 실제 오류 메시지를 먼저 분석한다. 내부 정보나 Stack Trace를 사용자에게 노출하지 않는다(R-008).
- API key, 비밀번호 등 Secret은 코드에 하드코딩하지 않고 환경변수를 사용한다. `.env`는 gitignore되어 있으므로 commit하지 않는다.
- 사용자가 명시적으로 요청하지 않으면 commit을 생성하지 않는다. 사용자가 수정한 관련 없는 변경사항을 덮어쓰지 않는다.
- 요구사항이 충돌하거나 모호하면 임의로 결정하지 말고 사용자에게 질문한다.
