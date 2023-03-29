from django.contrib.auth.base_user import BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')


        user = self.model(
            email = self.normalize_email(email),
        )
        user.is_active  = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_user(self, username, email):
    #   return self.model._default_manager._create_user(username=username)

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 