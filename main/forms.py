from django import forms
from .models import Brand, Mobile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from colorfield.widgets import ColorWidget


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'nationality']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'ذخیره'))

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ['brand', 'model', 'price', 'color', 'screen_size', 'status', 'manufacturing_country']
        widgets = {
            'color': ColorWidget,
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'ذخیره'))