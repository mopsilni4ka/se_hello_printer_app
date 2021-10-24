import unittest
from hello_world import app
from hello_world.formater import SUPPORTED
import json


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{ "imie": "Kseniya", \
"msg": "Hello World!" }', rv.data)

    # def test_msg_with_output_xml(self):
    #    rv = self.app.get('/?output=xml')
    #    expected = (b"<greetings><msg>Hello World!</msg>" +
    #                b"<name>Natalia</name</greetings>")
    #    print(rv.data)
    #    self.assertEqual(expected, rv.data)

    def test_msg_with_output_json_with_name(self):
        expected_name = "Amelia"
        expected_msg = "Hello World!"
        rv = self.app.get('/?output=json&name=' + expected_name)
        rd = json.loads(rv.data)
        # print(rd['imie'])
        self.assertEqual(expected_name, rd['imie'])
        self.assertEqual(expected_msg, rd['msg'])
