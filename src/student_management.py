class StudentManagement:
    def __init__(self):
        self.students = {}
        self.grades = {}

    def add_student(self, student_id: str, name: str, age: int) -> bool:
        if student_id in self.students:
            return False

        if not isinstance(age, int) or age <= 0:
            return False

        self.students[student_id] = {"name": name, "age": age}
        self.grades[student_id] = {}
        return True

    def update_student(self, student_id: str, name: str, age: int) -> bool:
        if student_id not in self.students:
            return False

        if not isinstance(age, int) or age <= 0:
            return False

        self.students[student_id] = {"name": name, "age": age}
        return True

    def remove_student(self, id: str) -> bool:
        if id not in self.students:
            return False

        del self.students[id]
        if id in self.grades:
            del self.grades[id]
        return True

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        if student_id not in self.students:
            return False

        valid_grades = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]
        if grade not in valid_grades:
            return False

        if subject not in self.grades[student_id]:
            self.grades[student_id][subject] = []

        self.grades[student_id][subject].append(grade)
        return True

    def avg_grades(self, subject: str) -> float:
        all_grades = []

        for student_id, subjects in self.grades.items():
            if subject in subjects:
                all_grades.extend(subjects[subject])

        if not all_grades:
            return 0.0

        return sum(all_grades) / len(all_grades)