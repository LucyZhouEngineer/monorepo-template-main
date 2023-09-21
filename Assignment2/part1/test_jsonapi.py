import unittest
from jsonapi import dumps, loads


class TestExtendedJSONEncoder(unittest.TestCase):
    def test_complex_serialization(self):
        # serialized complex
        c = complex(3, 2)
        serialized = dumps(c)
        self.assertIn("__type__", serialized)
        self.assertIn("complex", serialized)

        # deserialized complex
        deserialized = loads(serialized)
        self.assertEqual(c, deserialized)

    def test_range_serialization(self):
        # serialized range
        r = range(0, 21, 3)
        serialized = dumps(r)
        self.assertIn("__type__", serialized)
        self.assertIn("range", serialized)

        # deserialized range
        deserialized = loads(serialized)
        self.assertEqual(list(r), list(deserialized))


class TestDumpsAndLoadsFunctions(unittest.TestCase):
    def test_dumps_function(self):
        data = {"number": complex(3, 2)}
        serialized = dumps(data)
        self.assertIn("complex", serialized)

    def test_loads_function(self):
        serialized_data = (
            '{"number": {"__type__": "complex", "real": 3.0, "imag": 2.0}}'
        )
        deserialized = loads(serialized_data)
        self.assertEqual(deserialized["number"], complex(3, 2))


if __name__ == "__main__":
    unittest.main()
