import unittest
from src.student_management import StudentManagement


class StudentManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManagement()
        self.manager.add_student("1", "John Doe", 20)
        self.manager.add_student("2", "Jane Smith", 21)
        self.manager.add_grade("1", "Math", 4.0)
        self.manager.add_grade("1", "Math", 5.0)
        self.manager.add_grade("2", "Math", 3.0)
        self.manager.add_grade("1", "Physics", 3.5)

    def test_add_student_valid(self):
        result = self.manager.add_student("3", "Alice Brown", 22)
        self.assertTrue(result)
        self.assertIn("3", self.manager.students)
        self.assertEqual(self.manager.students["3"]["name"], "Alice Brown")
        self.assertEqual(self.manager.students["3"]["age"], 22)

    def test_add_student_existing_id(self):
        result = self.manager.add_student("1", "Duplicate Student", 25)
        self.assertFalse(result)

    def test_add_student_invalid_age(self):
        result1 = self.manager.add_student("4", "Invalid Age", -5)
        result2 = self.manager.add_student("5", "Invalid Age", "twenty")
        self.assertFalse(result1)
        self.assertFalse(result2)

    def test_update_student_valid(self):
        result = self.manager.update_student("1", "John Updated", 22)
        self.assertTrue(result)
        self.assertEqual(self.manager.students["1"]["name"], "John Updated")
        self.assertEqual(self.manager.students["1"]["age"], 22)

    def test_update_student_nonexistent(self):
        result = self.manager.update_student("999", "Nobody", 30)
        self.assertFalse(result)

    def test_update_student_invalid_age(self):
        result = self.manager.update_student("1", "John Doe", -10)
        self.assertFalse(result)

    def test_remove_student_valid(self):
        result = self.manager.remove_student("1")
        self.assertTrue(result)
        self.assertNotIn("1", self.manager.students)
        self.assertNotIn("1", self.manager.grades)

    def test_remove_student_nonexistent(self):
        result = self.manager.remove_student("999")
        self.assertFalse(result)

    def test_add_grade_valid(self):
        result = self.manager.add_grade("1", "Chemistry", 4.5)
        self.assertTrue(result)
        self.assertIn("Chemistry", self.manager.grades["1"])
        self.assertIn(4.5, self.manager.grades["1"]["Chemistry"])

    def test_add_grade_invalid(self):
        result = self.manager.add_grade("1", "Math", 6.0)
        self.assertFalse(result)
        result = self.manager.add_grade("1", "Math", 2.5)
        self.assertFalse(result)

    def test_add_grade_nonexistent_student(self):
        result = self.manager.add_grade("999", "Math", 5.0)
        self.assertFalse(result)

    def test_avg_grades_with_grades(self):
        avg = self.manager.avg_grades("Math")
        expected_avg = (4.0 + 5.0 + 3.0) / 3
        self.assertAlmostEqual(avg, expected_avg)

    def test_avg_grades_no_grades(self):
        avg = self.manager.avg_grades("Biology")
        self.assertEqual(avg, 0.0)

if __name__ == '__main__':
    unittest.main()