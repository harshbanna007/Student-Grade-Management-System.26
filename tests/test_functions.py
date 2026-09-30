from functions import (
    add_student,
    update_student,
    delete_student,
    search_student
)


def test_add_student():
    students = {}

    add_student(students, "Rahul", 85)

    assert students["Rahul"] == 85


def test_update_student():
    students = {"Rahul": 85}

    update_student(students, "Rahul", 90)

    assert students["Rahul"] == 90


def test_delete_student():
    students = {"Rahul": 85}

    delete_student(students, "Rahul")

    assert "Rahul" not in students


def test_search_student():
    students = {"Rahul": 85}

    assert "Rahul" in students
    assert students["Rahul"] == 85