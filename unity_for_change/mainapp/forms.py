from django import forms
from .models import OrphanKid, OldAgeHome, AccidentSupport, EducationSupport

class OrphanKidForm(forms.ModelForm):
    class Meta:
        model = OrphanKid
        fields = ['name', 'age', 'description', 'image']

class OldAgeHomeForm(forms.ModelForm):
    class Meta:
        model = OldAgeHome
        fields = '__all__'

class AccidentSupportForm(forms.ModelForm):
    class Meta:
        model = AccidentSupport
        fields = '__all__'

class EducationSupportForm(forms.ModelForm):
    class Meta:
        model = EducationSupport
        fields = '__all__'

