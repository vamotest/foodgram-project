from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from foodgram import settings

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
    
    def clean(self):
        
        data = self.data
        for key in data.keys():
            
            if 'username' in key:
                user_exists = User.objects.filter(username=data[key]).exists()
                
                if data[key] in settings.FORBIDDEN_USERNAMES or user_exists:
                    self.add_error(
                        'username',
                        'К сожалению, это имя пользователя уже используется.'
                    )
