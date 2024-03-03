from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Define placeholders for form fields
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'phone': 'Phone number',
            'message': 'message',
        }

        # Loop through form fields and set placeholders
        for field in self.fields:
            if field != 'contact_reason':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
