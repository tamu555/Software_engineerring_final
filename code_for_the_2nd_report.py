# プログラムの説明:
# このプログラムは、複数の学生の成績を管理し、合計点と平均点を計算し、
# 最も成績の良い学生を見つけます。

#各生徒の総合点と平均点を計算
def calculate_score(grades):
    total = 0
    count = 0
    for g in grades:
        total += g
        count += 1
    avg = total / count
    return total, avg

#runからsearch_topにrename
def search_top(students):
    top_score = 0
    top_student = ""

    for s in students:
        total, avg = calculate_score(students[s])

        if total > top_score:
            top_score = total
            top_student = s

        print(f"Student: {s}, Total: {total}, Average: {avg}")

    return top_student, top_score

students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [70, 75, 80],
    "David": [95, 85, 90]
}

top_student, top_score = search_top(students)
print(f"Best student: {top_student} with total score: {top_score}")