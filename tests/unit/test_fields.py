from unittest import TestCase

from src.form.fields import BaseField, SelectField, FieldFactory, InputField

__author__ = 'jslvtr'


class TestFields(TestCase):
    def setUp(self):
        self.field_attrs = {
            "id": "sample_field",
            "class": [
                "test_class",
                "test_class2"
            ],
            "name": "my_sample_field",
            "type": "text"
        }

    def test_create_base(self):
        field = BaseField(self.field_attrs)
        self.assertEqual(field.tag, "input")
        self.assertEqual(field.attrs, self.field_attrs)

    def test_set_get_item(self):
        field = BaseField(self.field_attrs)
        self.assertEqual(field['id'], "sample_field")
        field['id'] = "my_changed_id"
        self.assertEqual(field['id'], "my_changed_id")

    def test_build_base_field(self):
        field = BaseField(self.field_attrs)
        field_html = field.build()
        self.assertTrue('id="{}"'.format(self.field_attrs['id']) in field_html)
        self.assertTrue('class="{}"'.format(" ".join(self.field_attrs['class'])) in field_html)
        self.assertTrue('name="{}"'.format(self.field_attrs['name']) in field_html)
        self.assertTrue('type="{}"'.format(self.field_attrs['type']) in field_html)

    def test_build_select_field(self):
        select_attrs = {
            "id": "my_select_id",
            "class": "select_sample"
        }
        children = ["RESX", "JSON"]
        field = SelectField(select_attrs, children=children)
        field_html = field.build()

        self.assertTrue('id="{}"'.format(select_attrs['id']) in field_html)
        self.assertTrue('class="{}"'.format(select_attrs['class']) in field_html)
        for val in children:
            self.assertTrue('<option value="{val}">{val}</option>'.format(val=val) in field_html)

    def test_create_from_factory(self):
        json = {
            "tag": "input",
            "element": {
                "attrs": {
                    "id": "some_field",
                    "class": [
                        "class1",
                        "class2"
                    ],
                    "type": "text"
                }
            }
        }

        element = FieldFactory.create(json)
        self.assertEqual(element.attrs['id'], json['element']['attrs']['id'])
        self.assertIsInstance(element, InputField)