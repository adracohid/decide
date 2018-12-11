from django import forms
from voting.models import Question, QuestionOption


#TODO: agrupar en un solo formulario
class QuestionForm(forms.Form):
    name_voting = forms.CharField()
    desc_voting = forms.CharField()

    name_auth = forms.CharField()
    url_auth = forms.URLField()

    desc_question = forms.CharField()


class QuestionOptionsForm(forms.ModelForm):
    class Meta:
        model = QuestionOption

        fields = [
            'question',
            'number',
            'weight',
            'option'
        ]
        labels = {
            'question': 'Question',
            'number': 'Number',
            'weight': 'Weight',
            'option': 'Option Text'
        }
        widgets = {
            'weight': forms.TextInput(),
            'option': forms.TextInput(),
            'number': forms.HiddenInput(),
            'question': forms.HiddenInput()
        }


class someQuestionsOptions(forms.Form):
    description = forms.CharField()
    number = forms.CharField(widget=forms.HiddenInput)
    lista = list()
    option = QuestionOptionsForm()
    for i in range(0, 3):
        lista.append(option)
