from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student_1 = Student("Yosko", {"Python": ["n1", "n2", "n3"], "JS": ["n1", "n2"]})
        self.student_2 = Student("Gosho")

    def test_init_with_courses(self):
        self.assertEqual("Yosko", self.student_1.name)
        self.assertEqual({"Python": ["n1", "n2", "n3"], "JS": ["n1", "n2"]}, self.student_1.courses)

    def test_init_without_courses(self):
        self.assertEqual("Gosho", self.student_2.name)
        self.assertEqual({}, self.student_2.courses)

    def test_existing_courses(self):
        result = self.student_1.enroll("Python", ["n4", "n5"], add_course_notes="N")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3", "n4", "n5"], "JS": ["n1", "n2"]}, self.student_1.courses)

        result = self.student_1.enroll("Python", ["n6", "n7"], add_course_notes="Y")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": ["n1", "n2", "n3", "n4", "n5", "n6", "n7"], "JS": ["n1", "n2"]},
                         self.student_1.courses)

    def test_enroll_not_existing_course_with_y(self):
        result = self.student_1.enroll("C#", ["n1", "n2"], "Y")
        self.assertTrue("C#" in self.student_1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.student_1.courses["C#"])

    def test_test_enroll_not_existing_course_with_empty_string(self):
        result = self.student_1.enroll("C#", ["n1", "n2"], "")
        self.assertTrue("C#" in self.student_1.courses)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["n1", "n2"], self.student_1.courses["C#"])

    def test_test_enroll_not_existing_course_with_not_adding_notes(self):
        result = self.student_1.enroll("C#", ["n1", "n2"], "N")
        self.assertTrue("C#" in self.student_1.courses)
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student_1.courses["C#"])

    def test_add_notes_to_existing_course(self):
        self.student_2.enroll("C#", ["n1", "n2"])
        result = self.student_2.add_notes("C#", "n3")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["n1", "n2", "n3"], self.student_2.courses["C#"])

    def test_add_notes_to_not_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_2.add_notes("C#", "n3")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing(self):
        result = self.student_1.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Python", self.student_1.courses)

    def test_leave_not_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("C#")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()

