#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # 환경 변수에 Django 프로젝트의 설정 파일을 지정합니다.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # 명령줄에서 실행한 명령을 처리합니다.
    execute_from_command_line(sys.argv)
