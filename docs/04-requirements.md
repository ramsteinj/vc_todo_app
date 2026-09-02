# 04. 기능 요구사항

## R-001 Todo 생성

사용자는 새로운 Todo를 생성할 수 있어야 한다.

입력:
- title: 필수
- description: 선택

결과:
- Todo가 PostgreSQL에 저장된다.
- 새 Todo가 목록에 표시된다.

## R-002 Todo 목록 조회

사용자는 전체 Todo 목록을 볼 수 있어야 한다.

결과:
- 데이터는 Django REST API에서 가져온다.
- 각 Todo의 제목과 완료 상태를 표시한다.
- 필요한 경우 설명도 표시할 수 있다.

## R-003 Todo 상세 조회

Backend API는 특정 Todo 하나를 조회할 수 있어야 한다.

## R-004 Todo 수정

사용자는 다음 항목을 수정할 수 있어야 한다.

- title
- description

수정 결과는 PostgreSQL에 저장되어야 한다.

## R-005 완료 상태 변경

사용자는 Todo를 다음 상태 사이에서 변경할 수 있어야 한다.

- 완료
- 미완료

변경된 상태는 API를 통해 저장되어야 한다.

## R-006 Todo 삭제

사용자는 기존 Todo를 삭제할 수 있어야 한다.

삭제 결과는 PostgreSQL에 반영되어야 한다.

## R-007 입력 검증

최소한 다음을 검증한다.

- title은 비어 있으면 안 된다.
- 잘못된 API 입력에는 적절한 오류 응답을 반환한다.
- API 요청 실패 시 Frontend에 이해하기 쉬운 오류 메시지를 표시한다.

## R-008 오류 처리

다음 상황을 처리해야 한다.

- API 요청 실패
- 입력값 검증 실패
- 존재하지 않는 Todo 조회
- Backend/Database 오류

사용자에게 내부 서버 정보나 Stack Trace를 그대로 노출하지 않는다.

## R-009 Responsive UI

Desktop과 Mobile 크기의 화면에서 기본적인 사용이 가능해야 한다.

## 비기능 요구사항

- 코드는 이해하기 쉽게 작성한다.
- Framework 관례를 따른다.
- 불필요한 의존성을 추가하지 않는다.
- API 동작은 예측 가능해야 한다.
- 중요한 Backend/API 기능에 테스트를 작성한다.
