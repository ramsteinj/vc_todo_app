# 05. 데이터 모델

## Todo

| 필드 | 타입 | 필수 | 기본값 / 동작 |
|---|---|---|---|
| id | Integer | 예 | 자동 생성 Primary Key |
| title | String | 예 | 필수 |
| description | Text | 아니오 | 빈 문자열 |
| completed | Boolean | 예 | false |
| created_at | DateTime | 예 | 자동 생성 |
| updated_at | DateTime | 예 | 자동 수정 |

## 제약사항

- `title`은 필수이다.
- `completed`의 기본값은 `false`이다.
- `created_at`은 서버에서 자동으로 설정한다.
- `updated_at`은 데이터가 수정될 때 자동으로 갱신한다.

## ORM

Django ORM을 사용한다.

## Migration

데이터베이스 스키마 변경은 Django migration으로 관리한다.

## 샘플 데이터

개발 편의를 위한 샘플/초기 데이터는 선택 사항이다.

샘플 데이터가 없어도 애플리케이션은 정상적으로 실행되어야 한다.
