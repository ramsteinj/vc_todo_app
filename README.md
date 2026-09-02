# vc_todo_app

개인 사용자를 위한 Todo 관리 Web Application입니다. 프로젝트 요구사항은 `PROJECT.md`와 `docs/`를 참고하세요.

## 기술 스택

- Frontend: Vue 3 + Vite (JavaScript, SPA)
- Backend: Django + Django REST Framework
- Database: PostgreSQL

## 사전 요구사항

- Python 3.10 이상 (개발 당시 3.13 사용)
- Node.js 18 이상
- PostgreSQL 14 이상이 로컬에서 실행 중
- Git

## 1. 저장소 받기

```bash
git clone <저장소 주소>
cd vc_todo_app
```

## 2. 데이터베이스 준비

PostgreSQL 슈퍼유저 권한으로 애플리케이션용 역할과 데이터베이스를 생성합니다. 비밀번호는 직접 정해서 입력하세요.

```bash
sudo -u postgres psql -c "CREATE ROLE vc_todo LOGIN PASSWORD '여기에_비밀번호';" -c "CREATE DATABASE vc_todo_app OWNER vc_todo;"
```

Django의 자동 테스트(`manage.py test`)는 테스트용 데이터베이스를 생성하므로, 역할에 데이터베이스 생성 권한이 필요합니다.

```bash
sudo -u postgres psql -c "ALTER ROLE vc_todo CREATEDB;"
```

## 3. Backend 실행 (Django)

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

환경변수 파일을 만듭니다. `.env`는 Git에 커밋되지 않습니다.

```bash
cp .env.example .env
```

`backend/.env` 파일에서 다음 값을 채웁니다.

- `SECRET_KEY`: 아래 명령으로 생성한 값을 넣습니다.
  ```bash
  python -c "import secrets; print(secrets.token_urlsafe(64))"
  ```
- `DB_PASSWORD`: 2단계에서 정한 비밀번호

마이그레이션을 적용하고 개발 서버를 실행합니다.

```bash
python manage.py migrate
python manage.py runserver
```

- API: http://127.0.0.1:8000/api/todos/

## 4. Frontend 실행 (Vue 3 + Vite)

새 터미널에서 실행합니다.

```bash
cd frontend
npm install
npm run dev
```

- 앱: http://localhost:5173/

Backend 주소를 기본값(`http://127.0.0.1:8000`)이 아닌 곳에 띄웠다면 `frontend/.env` 파일에 다음을 추가하세요.

```
VITE_API_URL=http://백엔드주소:포트
```

CORS는 Backend의 `CORS_ALLOWED_ORIGINS` 환경변수(기본값: `http://localhost:5173,http://127.0.0.1:5173`)로 허용 목록을 관리합니다. Frontend를 다른 포트에서 띄울 경우 이 값에 포트를 추가하세요.

## 5. 테스트

Backend 자동 테스트(Model / CRUD API / Validation 16건):

```bash
cd backend
python manage.py test
```

Frontend 프로덕션 빌드:

```bash
cd frontend
npm run build
```
