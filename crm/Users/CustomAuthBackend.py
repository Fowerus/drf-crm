from django.contrib.auth import get_user_model
from django.contrib.auth.models import check_password

class AuthBackend(object):

    def authenticate(self, email=None, number=None, password=None):
        my_user_model = get_user_model()
        try:
            if email != None:
                user = my_user_model.objects.get(email=email)
            else:
                user = my_user_model.objects.get(number=number)

            if user.check_password(password):
                return user

        except my_user_model.DoesNotExist:
            return None
        except:
            return None