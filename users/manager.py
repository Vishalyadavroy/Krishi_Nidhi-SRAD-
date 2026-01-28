from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self , password = None, **extra_fields):
        if not extra_fields.get("email") and not extra_fields.get("phone"):
            raise ValueError('user must have email or phone')
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, password = None, **extra_fields):
        extra_fields.setdefault("is_staff" , True)
        extra_fields.setdefault("is_superuser",True)
        return self.create_user(password=password, **extra_fields)
