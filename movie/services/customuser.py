from movie.models import User


class UserService:
    def create_user(self, data=None):
        password = data.pop("password")
        user = User.objects.create(**data)
        user.set_password(password)
        user.save()
        return user
