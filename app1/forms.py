from django import forms


class DynamicForm(forms.Form):
    text = forms.CharField(label='Text ', max_length=10)

    # def __init__(self, *args, **kwargs):
    #     extra = kwargs.pop('extra')
    #     super(DynamicForm, self).__init__(*args, **kwargs)
    #
    #     for i, question in enumerate(extra):
    #         self.fields['fieldname_%s' % i] = forms.CharField(label=question)
    #
    # def extra_fields(self):
    #     for name, value in self.cleaned_data.items():
    #         if name.startswith('fieldname_'):
    #             yield (self.fields[name].label, value)