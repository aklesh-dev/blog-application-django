from django import forms
from .models import Comments

# ------Email Form--------|
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    # Each field type has a default widget that determines how the field is render in HTML.
    # The default widget can be overridden with the widget attribute.
    # using textarea widget to display it as a <textarea> HTML element instead of the default <input > element
    # comment is optional with required=False.
    comments = forms.CharField(required=False, widget=forms.Textarea)

# --------Comments Form---------|
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'body')

# ------Search View-------|
class SearchForm(forms.Form):
    query = forms.CharField()
