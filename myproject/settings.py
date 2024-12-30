import os
from pathlib import Path
from dotenv import load_dotenv

# .env 파일을 로드합니다.
load_dotenv()

# BASE_DIR을 프로젝트의 최상위 디렉토리로 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# secret key
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# host
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Debug
DEBUG = False

# database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # SQLite 엔진 사용
        "NAME": BASE_DIR
        / "db.sqlite3",  # 데이터베이스 파일 경로 (프로젝트 디렉토리에 db.sqlite3 파일이 생성됨)
    }
}

# logging
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "[{levelname}] {asctime} {module} {message}",  # 디버그 메시지, 일반적인 메시지에 대한 포맷
#             "style": "{",
#         },
#         "detailed": {
#             "format": "[{levelname}] {asctime} {module} {message} | {pathname} {funcName} | {lineno}",  # 오류 시 자세한 정보 포함
#             "style": "{",
#         },
#     },
#     "handlers": {
#         "console": {
#             "level": "INFO",  # 기본 레벨은 INFO
#             "class": "logging.StreamHandler",
#             "formatter": "verbose",  # INFO, DEBUG, WARNING 메시지에는 간단한 포맷 사용
#         },
#         "error_console": {
#             "level": "ERROR",  # ERROR 레벨 이상의 메시지는 ERROR 콘솔 핸들러로 출력
#             "class": "logging.StreamHandler",
#             "formatter": "detailed",  # ERROR 메시지에 대해서는 상세 포맷 사용
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console", "error_console"],
#             "level": "INFO",  # 기본적으로 INFO 이상의 메시지를 출력
#             "propagate": True,
#         },
#         "django.db.backends": {
#             "level": "ERROR",  # DB 관련 쿼리에서 ERROR 이상만 출력
#             "handlers": ["error_console"],
#             "propagate": False,
#         },
#     },
# }
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",  # 로그 레벨을 설정
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],  # 로그를 출력할 핸들러 지정
            "level": "INFO",  # 로그 레벨을 설정
            "propagate": True,  # 부모 로거에게 전달
        },
    },
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
    "user",  # user 앱 추가
]

# static
# STATIC_URL = "/static/"
