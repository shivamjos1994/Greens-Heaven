from django.contrib.auth.forms import UserCreationForm     #to create built in form by using UserCreationForm
from django.contrib.auth.models import User                #inbuilt model User

class SignupForm(UserCreationForm):
       class Meta:
          model=User
          fields=['username','first_name','last_name','email','password1','password2']