import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):

    def test_id_increment(self):
        """
        Test if the id is incremented correctly when no id is provided.
        """
        base_obj1 = Base()
        base_obj2 = Base()
        self.assertEqual(base_obj1.id, 1)
        self.assertEqual(base_obj2.id, 2)

    def test_id_assigned(self):
        """
        Test if the provided id is correctly assigned.
        """
        base_obj = Base(10)
        self.assertEqual(base_obj.id, 10)

    def test_id_mixed(self):
        """
        Test if the id is correctly incremented when both provided and not provided.
        """
        base_obj1 = Base()
        base_obj2 = Base(5)
        base_obj3 = Base()
        self.assertEqual(base_obj1.id, 1)
        self.assertEqual(base_obj2.id, 5)
        self.assertEqual(base_obj3.id, 2)

    def test_id_negative(self):
        """
        Test if the id can be a negative value.
        """
        base_obj = Base(-3)
        self.assertEqual(base_obj.id, -3)

    def test_id_type(self):
        """
        Test if the id is an integer.
        """
        base_obj = Base("string_id")
        self.assertIsInstance(base_obj.id, int)

    def test_to_json_string_empty_list(self):
        """
        Test if to_json_string returns "[]" for an empty list.
        """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        """
        Test if to_json_string returns the correct JSON string for a non-empty list of dictionaries.
        """
        result = Base.to_json_string([{'key': 'value'}, {'key2': 'value2'}])
        self.assertEqual(result, '[{"key": "value"}, {"key2": "value2"}]')

    def test_save_to_file(self):
        """
        Test if save_to_file writes the correct JSON string to a file.
        """
        base_obj = Base()
        Base.save_to_file([base_obj])
        with open("Base.json", 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1}]')

    def test_from_json_string_empty_string(self):
        """
        Test if from_json_string returns an empty list for an empty string.
        """
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty_string(self):
        """
        Test if from_json_string returns the correct list of dictionaries for a non-empty string.
        """
        result = Base.from_json_string('[{"key": "value"}, {"key2": "value2"}]')
        expected = [{'key': 'value'}, {'key2': 'value2'}]
        self.assertEqual(result, expected)

    def test_create_rectangle(self):
        """
        Test if create method creates an instance of Rectangle with the correct attributes.
        """
        result = Base.create(width=3, height=4, x=1, y=2, id=5)
        self.assertEqual(result.width, 3)
        self.assertEqual(result.height, 4)
        self.assertEqual(result.x, 1)
        self.assertEqual(result.y, 2)
        self.assertEqual(result.id, 5)

    def test_create_square(self):
        """
        Test if create method creates an instance of Square with the correct attributes.
        """
        result = Base.create(size=3, x=1, y=2, id=5)
        self.assertEqual(result.size, 3)
        self.assertEqual(result.x, 1)
        self.assertEqual(result.y, 2)
        self.assertEqual(result.id, 5)

    def test_load_from_file(self):
        """
        Test if load_from_file returns a list of instances from the file.
        """
        base_obj = Base()
        Base.save_to_file([base_obj])
        result = Base.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Base)

if __name__ == '__main__':
    unittest.main()

