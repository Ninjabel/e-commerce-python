class User:
    users_db = []

    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        User.users_db.append(self)
    @classmethod
    def get_all_users(cls):
        return cls.users_db

    @classmethod
    def get_user_by_id(cls, user_id):
        for user in cls.users_db:
            if user.user_id == user_id:
                return user
        return None

    @classmethod
    def delete_user(cls, user_id):
        user_to_delete = cls.get_user_by_id(user_id)
        if user_to_delete:
            cls.users_db.remove(user_to_delete)
            return True
        return False

    @classmethod
    def update_user(cls, user_id, username=None, email=None):
        user = cls.get_user_by_id(user_id)
        if user:
            if username:
                user.username = username
            if email:
                user.email = email
            return True
        return False