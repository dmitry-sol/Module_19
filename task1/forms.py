from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="Введите логин",
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}),
        error_messages={'required': 'Поле "Логин" обязательно для заполнения.'}
    )
    password = forms.CharField(
        min_length=8,
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )
    confirm_password = forms.CharField(
        min_length=8,
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
    )
    age = forms.IntegerField(
        label="Введите свой возраст",
        widget=forms.NumberInput(attrs={'placeholder': 'Введите свой возраст'}),
        min_value=8,
        error_messages={
            'invalid': 'Возраст должен быть числом',
            'min_value': 'Вы должны быть старше 8 лет.'
        }
    )

    def __init__(self, *args, existing_users=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.existing_users = existing_users or []

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if self.existing_users.filter(name=username).exists():
            raise forms.ValidationError(f"Пользователь {username} уже существует.")
        return username

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     if hasattr(self.existing_users, 'filter'):  # Проверяем, QuerySet ли это
    #         if self.existing_users.filter(name=username).exists():
    #             raise forms.ValidationError(f"Пользователь {username} уже существует.")
    #     elif username in self.existing_users:  # Если это список
    #         raise forms.ValidationError(f"Пользователь {username} уже существует.")
    #     return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают.")

        return cleaned_data
