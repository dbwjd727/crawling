import os
from pathlib import Path

# BASE_DIR을 프로젝트의 최상위 디렉토리로 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# host
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Debug
DEBUG = False

# logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "debug.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

# database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # SQLite 엔진 사용
        "NAME": BASE_DIR
        / "db.sqlite3",  # 데이터베이스 파일 경로 (프로젝트 디렉토리에 db.sqlite3 파일이 생성됨)
    }
}

# root
ROOT_URLCONF = "myproject.urls"

# templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # Django 템플릿 엔진 사용
        "DIRS": [],  # 템플릿 디렉토리 (필요하면 추가)
        "APP_DIRS": True,  # 앱 내 템플릿을 자동으로 검색
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",  # 세션 미들웨어 추가
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # 인증 미들웨어 추가
    "django.contrib.messages.middleware.MessageMiddleware",  # 메시지 미들웨어 추가
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]

INSTALLED_APPS = [
    "django.contrib.admin",  # 관리자 앱 추가
    "django.contrib.auth",  # 사용자 인증 관련 앱
    "django.contrib.contenttypes",  # 콘텐츠 유형 앱
    "django.contrib.sessions",  # 세션 앱
    "django.contrib.messages",  # 메시지 프레임워크 앱
    "django.contrib.staticfiles",  # 정적 파일 처리 앱
    "myproject",  # 여러분의 앱 (예시: myproject 앱)
]

# static
STATIC_URL = "/static/"

# secret key
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "your-default-secret-key-here")