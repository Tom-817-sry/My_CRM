from rbac import models
from django import forms
from django.core.exceptions import ValidationError

class UserModeForm(forms.ModelForm):
    confirm_password = forms.CharField(label='确认密码')
    class Meta:
        model = models.UserInfo
        fields = ['name','email','password','confirm_password']

        # error_messages = {'name'}     手动设置错误信息

    def __init__(self,*args,**kwargs):
        super(UserModeForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_confirm_password(self):
        '''
        检测密码是否一致
        :return:
        '''
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise ValidationError('两次密码不一致！')

        return confirm_password

class UpdateUserModeForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name','email']

    def __init__(self,*args,**kwargs):
        super(UpdateUserModeForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ResetPasswordUserModeForm(forms.ModelForm):
    confirm_password = forms.CharField(label='确认密码')
    class Meta:
        model = models.UserInfo
        fields = ['password','confirm_password']

    def __init__(self,*args,**kwargs):
        super(ResetPasswordUserModeForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_confirm_password(self):           # 设置钩子检测两个密码是否一致
        '''
        检测密码是否一致
        :return:
        '''
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise ValidationError('两次密码不一致！')

        return confirm_password
