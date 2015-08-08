from src.common.errors import NoChildrenInFormError
from src.form.fields import FieldFactory

__author__ = 'jslvtr'


class FormBuilder(object):
    def __init__(self, json):
        self.json = json
        self.attrs = json['attrs'] if 'attrs' in json.keys() else {}
        if 'children' not in json.keys():
            raise NoChildrenInFormError("A form was created without children, which isn't very useful...")
        self.children = json['children']

    def build(self):
        html = self._build_form()
        for child in self.children:
            html += FieldFactory.create(child).build()
        html += "</form>"
        return html

    def _build_form(self):
        form_tag = "<form"
        for index, key in enumerate(self.attrs.keys()):
            value = self.attrs[key]
            form_tag += ' {}="{}"'.format(key, " ".join(value) if isinstance(value, list) else value)
        form_tag += ">"
        return form_tag