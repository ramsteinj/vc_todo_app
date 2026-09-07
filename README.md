# vc_todo_app

개인 사용자를 위한 Todo 관리 Web Application입니다. 프로젝트 요구사항은 `PROJECT.md`와 `docs/`를 참고하세요.

## 기술 스택

- Frontend: Vue 3 + Vite (JavaScript, SPA)
- Backend: Django + Django REST Framework
- Database: PostgreSQL
- UI: Spark Admin Theme (Bootstrap 5, ThemeWagon — UI 푸터에 출처 표기)

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

## 6. Render 배포

Render Blueprint(`render.yaml`)로 Frontend(Static Site), Backend(Web Service), PostgreSQL 3개 리소스를 한 번에 생성합니다. 사전에 이 저장소가 GitHub에 푸시되어 있어야 합니다.

### 6-1. Blueprint로 생성

1. https://dashboard.render.com 에 로그인합니다.
2. **New → Blueprint** 를 선택하고 이 저장소를 연결합니다.
3. Blueprint가 감지되면 **Apply** 를 누릅니다. `render.yaml` 정의대로 3개 리소스가 생성되고 첫 배포가 시작됩니다.
   - `sync: false` 환경변수는 지금 비워 두어도 됩니다. 배포 후 입력합니다.

### 6-2. 실제 URL 확인

첫 배포가 끝나면 각 서비스 페이지 상단에서 실제 주소를 확인합니다. (서비스 이름이 이미 사용 중이면 임의 접미사가 붙을 수 있습니다.)

- Backend 예시: `https://vc-todo-backend.onrender.com`
- Frontend 예시: `https://vc-todo-frontend.onrender.com`

### 6-3. 환경변수 연결 (각 서비스 Environment 탭)

Backend(`vc-todo-backend`):

| 키 | 값 |
| --- | --- |
| `ALLOWED_HOSTS` | Backend 호스트 (예: `vc-todo-backend.onrender.com`) |
| `CORS_ALLOWED_ORIGINS` | Frontend 주소 (예: `https://vc-todo-frontend.onrender.com`) |
| `CSRF_TRUSTED_ORIGINS` | Backend 주소 (예: `https://vc-todo-backend.onrender.com`) |

Frontend(`vc-todo-frontend`):

| 키 | 값 |
| --- | --- |
| `VITE_API_URL` | Backend 주소 (예: `https://vc-todo-backend.onrender.com`) |

저장 후 두 서비스 모두 **Manual Deploy → Deploy latest commit** 으로 재배포합니다. Frontend는 빌드타임에 `VITE_API_URL`을 주입하므로 반드시 재빌드가 필요합니다.

### 6-4. 동작 확인

1. 브라우저에서 Frontend 주소에 접속해 Todo 추가/수정/삭제를 확인합니다.
2. `https://<backend 주소>/api/todos/` 에 직접 접속해 JSON 응답을 확인합니다.

### 6-5. (선택) Django admin

Render 서비스 페이지의 **Shell** 에서 슈퍼유저를 만듭니다.

```bash
python manage.py createsuperuser
```

이후 `https://<backend 주소>/admin/` 에 접속합니다.

### Free 플랜 주의사항

- 무료 Web Service는 15분간 요청이 없으면 sleep하며, 첫 요청이 수십 초 늦을 수 있습니다.
- 무료 PostgreSQL은 생성 후 약 30일 뒤 만료되어 데이터가 삭제됩니다. 장기 사용 시 유료 플랜으로 전환하거나 데이터를 백업한 뒤 DB를 재생성해야 합니다.
