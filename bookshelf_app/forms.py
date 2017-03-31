from django import forms
from django.core.exceptions import ValidationError
from bookshelf_app.models import Book, BookID

# 册数验证器
def validate_amount(value):
    if value > 99 or value < 1:
        raise ValidationError('册数应为1-99' ) 


class BookForm(forms.ModelForm):
    amount = forms.IntegerField(validators=[validate_amount],)

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'autofocus': "autofocus", }), # 设置焦点
        }


# 一个只读状态的表单，用于展示书目详情
class BookFormReadOnly(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    publisher = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    ISBN = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    CLC = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    pub_date = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

