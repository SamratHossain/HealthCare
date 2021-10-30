from django.contrib.auth.models import BaseUserManager

class AccountUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("User Must Have an Email")

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user