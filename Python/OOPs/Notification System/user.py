
# ---------- Encapsulation ----------

class User:
    """
    User entity with encapsulated data
    """

    def __init__(self, name: str, phone: str):
        self.name = name
        self.__phone = phone   # private variable

    @property
    def phone(self) -> str:
        return self.__phone
    

