from notification_base import NotificationManager, SMSNotification, EmailNotification
from user import User

def main():
    user = User("Mohammed", "9999999999")

    email_manager = NotificationManager(EmailNotification())
    sms_manager = NotificationManager(SMSNotification())

    print(email_manager.notify(f"Welcome {user.name}"))
    print(sms_manager.notify(f"OTP sent to {user.phone}"))

if __name__ == "__main__":
    main()
