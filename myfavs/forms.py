from django.contrib.auth.forms import (
    AuthenticationForm
)
from account import models

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    class Meta:
        model = models.User
        fields = (
            "username", "password"
        )

    def __init__(self, *args, **kwargs):
        print("init")
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
            print(field)