from django import forms
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    review_rating = forms.ChoiceField(choices=Review.RATING, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Review
        fields = ['comment', 'review_rating']
