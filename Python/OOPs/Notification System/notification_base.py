from abc import ABC, abstractmethod

class NotificationService(ABC):
    """
    Abstract base class defining the notification contract
    """
    @abstractmethod
    def send(self, message:str) -> str:
        pass

# ---------- Inheritance ----------

class EmailNotification(NotificationService):
    """
    Sends notification via Email
    """

    def send(self, message: str) -> str:
        return f"Email sent: {message}"

class SMSNotification(NotificationService):
    """
    Sends notification via SMS
    """

    def send(self, message: str) -> str:
        return f"SMS sent: {message}"
    
# ---------- Composition ----------

class NotificationManager:
    """
    Manages notification sending using composition
    """

    def __init__(self, service: NotificationService):
        self.service = service   # HAS-A relationship

    def notify(self, message: str) -> str:
        return self.service.send(message)