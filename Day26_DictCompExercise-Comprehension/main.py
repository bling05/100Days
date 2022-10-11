def main():
    names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
    import random
    students_scores = {student:random.randint(1,100) for student in names}

    passed_students = {student:students_scores[student] for student in students_scores if students_scores[student] >= 65}

    print(passed_students)

if __name__ == '__main__':
    main()