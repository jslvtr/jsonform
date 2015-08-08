import json
import os
from unittest import TestCase
from src.form.builder import FormBuilder

__author__ = 'jslvtr'


class TestSimpleForm(TestCase):
    def test_simple_form(self):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path, "simple_form.json")) as f:
            json_obj = json.load(f)
        form = FormBuilder(json_obj)

        self.assertEqual(form.attrs['id'], json_obj['attrs']['id'])
        self.assertEqual(form.attrs['class'], json_obj['attrs']['class'])
        self.assertEqual(form.attrs['style'], json_obj['attrs']['style'])
        self.assertEqual(form.children, json_obj['children'])

        html = form.build()

        self.assertTrue('id="my_text_field"' in html)
        self.assertTrue('id="my_select_field"' in html)
        self.assertTrue('id="form_test"' in html)
        self.assertTrue('style="display: block; background-color: #333333;"' in html)
        self.assertTrue('class="class1 class2"' in html)
