from django import forms
from multiuploader.forms import MultiuploaderField
class MixTapeUploadForm(forms.Form):
    mix_name = forms.CharField(
        label='Title of Mixtape'
    )

    album_art = forms.FileField(
        label='Album Artwork'
    )
    uploadedFiles = MultiuploaderField()
