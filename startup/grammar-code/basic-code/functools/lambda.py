if __name__ == '__main__':
    students = [('Tom', 88), ('Jerry', 77), ('Spike', 95)]
    students.sort(key=lambda x: x[1], reverse=True)
    print(students)
