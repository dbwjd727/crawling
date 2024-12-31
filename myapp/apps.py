from django.apps import AppConfig


class MyAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myapp"  # 디렉토리 이름과 동일하게 설정

    def ready(self):
        print("앱 초기화 중...")
        from .task import start_scheduler

        start_scheduler()
