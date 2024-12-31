from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from apscheduler.triggers.interval import IntervalTrigger


def my_scheduled_task():
    print(f"실행시각 : {datetime.now()}")


# 스케줄러 설정
def start_scheduler():
    scheduler = BackgroundScheduler()

    # 예: 매일 오전 9시에 실행
    scheduler.add_job(
        my_scheduled_task,
        trigger=IntervalTrigger(seconds=60),  # 매 3초마다 실행
        id="my_task",  # 고유 ID (중복 방지)
        replace_existing=True,  # 동일 ID의 기존 작업을 교체
    )

    scheduler.start()
    print("스케쥴러 실행!")
