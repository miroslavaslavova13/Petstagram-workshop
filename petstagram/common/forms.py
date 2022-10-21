from django import forms

from petstagram.common.models import PhotoComment


class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add comment...'
                }
            )
        }


class SearchPhotoForm(forms.Form):
    pet_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by pet name...'
            }
        ),
        required=False)
