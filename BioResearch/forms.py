from django import forms

class PapersForm(forms.Form):
    title = forms.CharField(max_length=200)
    subtitle = forms.CharField(max_length=100 )
    main_theme = forms.CharField(max_length=100 )
    link = forms.URLField()
    authors = forms.CharField(max_length=100)
    published_date = forms.DateField ()
    open_access =  forms.BooleanField()

