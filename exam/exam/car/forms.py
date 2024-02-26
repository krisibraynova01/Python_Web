from django import forms

from exam.car.models import Car


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']
        widgets = {
            'image_url': forms.TextInput(attrs={'placeholder': 'https://...'}),
        }

class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']

class DeleteCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True


