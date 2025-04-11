import smtplib
from email.message import EmailMessage

def send_reminder_email(user_email: str):
    sender_email = "gayatrijayan2003@gmail.com"
    app_password = "hglt yibi whtl yraz"  # use Gmail App Password (not your login password)

    msg = EmailMessage()
    msg.set_content("Hi 👋\n\nThis is your monthly reminder to do a quick breast self-exam. Stay aware. Stay healthy 💖")
    msg["Subject"] = "🩺 Breast Self-Exam Reminder"
    msg["From"] = sender_email
    msg["To"] = user_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
