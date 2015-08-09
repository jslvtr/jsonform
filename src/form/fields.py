from src.common.errors import FieldFormatError

__author__ = 'jslvtr'


class FieldFactory(object):
    @staticmethod
    def create(json):
        if 'tag' not in json.keys():
            raise FieldFormatError("A field was created without a tag. This is certainly not valid!")

        if json['tag'] == "input":
            return InputField(**json['element'])
        elif json['tag'] == "select":
            return SelectField(**json['element'])


class BaseField(object):
    def __init__(self, attrs={}, parent=None, children=[]):
        self.tag = "input"
        self.attrs = {}
        self.parent = None
        self.children = []

        if attrs is not None and len(attrs) > 0:
            self.attrs.update(attrs)
        if parent is not None:
            self.parent = parent
        if children is not None and len(children) > 0:
            self.children = children

    def __getitem__(self, item):
        if item == "tag" or item == "name":
            return self.tag
        else:
            return self.attrs[item]

    def __setitem__(self, key, value):
        if key == "tag" or key == "name":
            self.tag = value
        else:
            self.attrs[key] = value


class InputField(BaseField):
    def __init__(self, attrs={}, parent=None, children=[]):
        super(InputField, self).__init__(attrs, parent, children)

    def build(self):
        html = "<{}".format(self.tag)
        for index, key in enumerate(self.attrs.keys()):
            value = self.attrs[key]
            html += ' {}="{}"'.format(key, " ".join(value) if isinstance(value, list) else value)
        html += ">"
        return html


class SelectField(BaseField):
    def __init__(self, attrs={}, parent=None, children=[]):
        super(SelectField, self).__init__(attrs, parent, children)
        self['tag'] = "select"

    def build(self):
        html = super(SelectField, self).build()
        for option in self.children:
            html += '<option value="{val}">{val}</option>'.format(val=option)
        html += "</{}>".format(self['tag'])
        return html