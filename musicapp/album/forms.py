from django import forms

from musicapp.album.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'genre', 'description', 'image_url', 'price']
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'genre': forms.Select(attrs={'placeholder': 'Genre'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price'}),
        }


class EditAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'genre', 'description', 'image_url', 'price']
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'genre': forms.Select(attrs={'placeholder': 'Genre'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price'}),
        }

class DeleteAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'genre', 'description', 'image_url', 'price']
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name', 'readonly': True}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist', 'readonly': True}),
            'genre': forms.Select(attrs={'placeholder': 'Genre', 'readonly': True}),
            'description': forms.TextInput(attrs={'placeholder': 'Description', 'readonly': True}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL', 'readonly': True}),
            'price': forms.TextInput(attrs={'placeholder': 'Price', 'readonly': True}),
        }
