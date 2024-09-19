"""
File: student.py
Resources to manage a student's name and test scores.
"""

import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def __eq__(self, student):
        if self.name != student.name:
            return False
        return True

    def __lt__(self, student):
        if self.name < student.name:
            return False
        return True
    
    def __ge__(self, student):
        if self.name >= student.name:
            return False
        return True

def main():
    """A simple test."""
    student = Student("Ken", 5)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)

    #testing new methods
    student2 = Student("Barbie", 5)
    for i in range(1, 6):
        student2.setScore(i, 50)
    print(student2)

    print()
    print(student == student2)
    print(student < student2)
    print(student >= student2)
    print()

    #making a list to shuffle and sort
    student3 = Student("Kaylee", 5)
    for i in range(1, 6):
        student3.setScore(i, 25)
    student4 = Student("Matt", 5)
    for i in range(1, 6):
        student4.setScore(i, 75)

    students = [student, student2, student3, student4]
    random.shuffle(students)
    for i in range(0, len(students)):
        print(students[i])

    students.sort()
    print()
    for i in range(0, len(students)):
        print(students[i])

if __name__ == "__main__":
    main()


