from django import forms
class MixTapeUploadForm(forms.Form):
    mix_name = forms.CharField(
        label='Title of Mixtape'
    )
    album_art = forms.FileField(
        label = 'Album Art'
    )
    mixtape = forms.FileField(
        label='Zip File:',
    )

