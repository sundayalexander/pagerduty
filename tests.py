import unittest
# Import Unit to test.
from main import save_incident_to_csv


# Incident Test Case class definition.
class IncidentTestCase(unittest.TestCase):
    def test_save_incident_to_csv(self):
        self.assertEqual(save_incident_to_csv(), 'incidents.csv', 'Should return the exported file name: "incidents.csv"')


if __name__ == '__main__':
    unittest.main()
