from hello_world.formater import plain_text_upper_case
from hello_world.formater import format_to_xml
import unittest
import hello_world.views

class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_xml(self):
        imie = "Natalia"
        r = format_to_xml("XYZ", imie)
        print (r)
