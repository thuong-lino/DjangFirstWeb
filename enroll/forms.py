from django import forms
from .models import ClassInfo
class EnrollForm(forms.ModelForm):
    class Meta:
        model = ClassInfo
        fields = [
            'name' , 'phone_number', 'district',
            'address', 'email', 'subjects', 'lop',
            'num_student', 'date_start' , 'fee_expected',
            'frequency', 'teaching_time', 'sex_require',
            'note'
        ]
        widgets = {
            'date_start': forms.DateInput(attrs={'type':'date'}),
            'note' : forms.Textarea(attrs={'class':'input--style-1', 'cols':'60', 'rows':'5'})
        }
