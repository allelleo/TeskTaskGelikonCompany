from core.celery import app


@app.task
def deleting_overdue_tasks():
    print("DELETE!")
