from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError("El usuario no puede estar vacio.")
        user=self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user  

    def create_superuser(self, username, password):
        user=self.create_user(username=username, password=password)
        user.is_admin=True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def save(self, **kwargs):
        some_salt = '8IuovGYnhnqA9vpWg8BvgmcoT'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'