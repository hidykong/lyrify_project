from django import forms
from lyrify.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'updated', 'created', ]
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Put in your lyrics...'}
            ),
        }


class AnswerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(AnswerForm, self).__init__(*args, **kwargs)

        # for i, question in enumerate(extra):
        #     self.fields['custom_%s' % i] = forms.CharField(label=question)

    
	length = forms.CharField(max_length=30)