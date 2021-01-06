class Grade:
    def __init__(self, student_id, course_code, score):
        self.student_id = int(student_id)
        self.course_code = int(course_code)
        self.score = float(score)


class CourseUtil:
    def __init__(self):
        self.course_file = None
        pass

    def set_file(self, address):
        self.course_file = open(address, "a+")
        self.course_file.seek(0, 0)

    def save(self, grade):
        lines = self.course_file.readlines()
        print(lines)
        for line in lines:
            print(line.split(" ")[0])
            print(grade.student_id)
            if grade.student_id == int(line.split(" ")[0]) and grade.course_code == int(line.split(" ")[1]):
                return 1
        line = str(grade.student_id) + " " + str(grade.course_code) + " " + str(grade.score) + "\n"
        self.course_file.seek(0, 0)

        self.delete_last_line()

    def delete_last_line(self):
        lines = self.course_file.readlines()
        line = lines[-1]
        line = line.rstrip()
        lines[-1] = line
        self.course_file.writelines(lines)

    def load(self, line_number):
        lines = self.course_file.readlines()
        course_parameters = lines[line_number - 1].split(" ")
        return Grade(course_parameters[0], course_parameters[1], course_parameters[2])

    def calc_course_average(self, course_code):
        lines = self.course_file.readlines()
        scores = []
        for line in lines:
            if int(line.split(" ")[1]) == course_code:
                scores.append(float(line.split(" ")[2]))

        return sum(scores) / float(len(scores))

    def calc_student_average(self, student_id):
        lines = self.course_file.readlines()
        scores = []
        for line in lines:
            if int(line.split(" ")[0]) == student_id:
                scores.append(float(line.split(" ")[2]))

        return sum(scores) / float(len(scores))

    def count(self):
        return len(self.course_file.readlines())


util = CourseUtil()
util.set_file("course.txt")
util.save(Grade(9631046, 1234, 13))
