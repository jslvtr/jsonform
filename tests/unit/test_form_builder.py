from unittest import TestCase
from src.common.errors import NoChildrenInFormError
from src.form.builder import FormBuilder

__author__ = 'jslvtr'


class TestFormBuilder(TestCase):
    def test_build_form(self):
        json = {
            "attrs": {
                "id": "some_id",
                "class": [
                    "class1",
                    "class2"
                ]
            },
            "children": []
        }

        form = FormBuilder(json)
        html = form._build_form()
        self.assertTrue('id="{}"'.format(json['attrs']['id']) in html)
        self.assertTrue('class="{}"'.format(" ".join(json['attrs']['class'])) in html)

    def test_build_form_no_children(self):
        json = {
            "attrs": {
                "id": "some_id",
                "class": [
                    "class1",
                    "class2"
                ]
            }
        }

        with self.assertRaises(NoChildrenInFormError):
            FormBuilder(json)

    def test_build_form_one_child(self):
        json = {
            "attrs": {
                "id": "some_id",
                "class": [
                    "class1",
                    "class2"
                ]
            },
            "children": [
                {
                    "tag": "input",
                    "element": {
                        "attrs": {
                            "id": "my_text_field",
                            "type": "text"
                        },
                        "parent": "some_id"
                    }
                }
            ]
        }

        form = FormBuilder(json)
        html = form.build()
        self.assertTrue('id="my_text_field"' in html)
        self.assertTrue('id="some_id"' in html)
        self.assertTrue('class="class1 class2"' in html)