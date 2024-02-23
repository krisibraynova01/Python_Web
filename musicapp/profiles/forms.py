from django import forms

from musicapp.profiles.models import Profile


class ProfileDeleteForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ()

        def save(self, commit=True):
            if commit:
                self.instance.delete()
            return self.instance
