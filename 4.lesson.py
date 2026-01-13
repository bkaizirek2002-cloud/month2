class User:
    user_count = 0

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        User.user_count += 1

   @classmethod
   def get_user_count(cls):
    return cls.wser_count

   @classmethod
   def create_user(cls, name, phone):
       new_user = cls(name, phone)
       return new_user



user_1 = User("Albert", "996777111111")
print(User.user_count)
User.user_count += 1
print(User.user_count)gi


