import unittest
from name_function import get_formated_name


class NamesTestCase(unittest.TestCase):
    """Test for 'name_funciton.py.'"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formated_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()
