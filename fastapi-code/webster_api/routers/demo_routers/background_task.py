from fastapi import APIRouter, BackgroundTasks

bg_task_router = APIRouter(prefix="/background_task", tags=["background_task"])


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

        
@bg_task_router.post("/send-notification/{email}")
async def send_notification(
        email: str,
        background_tasks: BackgroundTasks,
):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
