from fastapi import FastAPI
import uvicorn

app = FastAPI()


grades = {
    "1": {"name": "Moshe", "grade": 88},
    "2": {"name": "Yaakov", "grade": 75},
    "3": {"name": "David", "grade": 92},
}

@app.get("/students")
def get_students():
    all_students = []
    for g in grades.values():
        all_students.append(g)
    return all_students


@app.get("/students/top")
def top_student():
    highest = dict()
    maxi = max([s["grade"] for s in grades.values()])
    for s in grades.values():
        if s["grade"] == maxi:
            highest = s.copy()
    return highest


@app.get("/students/average")
def get_average():
    total = [s["grade"] for s in grades.values()]
    average = round(sum(total)/len(grades), 2)
    return {"Average": average}


@app.get("/students/count")
def count_students():
    count = len(grades)
    return {"Count students:": count}



@app.get("/students/{student_id}")
def student_by_id(student_id):
    stud = dict()
    for g in grades:
        if g == student_id:
            stud = grades[g]
    return stud


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)




