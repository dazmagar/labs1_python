import json


def sort_by_marks_descending(json_string):
    students = json.loads(json_string)
    students.sort(key=lambda s: (-s["mark"], s["name"]))
    return json.dumps(students)

if __name__ == "__main__":
    print(sort_by_marks_descending('[{"name": "John", "mark": 85},{"name": "Alice", "mark": 90}, {"name": "Bob", "mark": 88}]'))
