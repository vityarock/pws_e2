from django import forms
from .models import Message


class EmailForm(forms.ModelForm):
    body = forms.CharField(
            widget=forms.Textarea(attrs={"rows":2, "cols":30})
    )
    class Meta:
        model = Message
        fields = ('receiver', 'subject', 'body', 'delay')
