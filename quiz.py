# q = {
#     "question":"toi co dep trai khong ?",
#     "choices":["A.Dep trai vailon","B.Khong"],
#     "right_choice":"A"
# }
question_pack = [
    {
        "question":"co nhan ra giang vien ko",
        "choice": {"A.co","B.khong","C.anh la ai","D.giang vien con chua den"},
        "right choice":"D"
    },
    {
        "question":"co di muon ko",
        "choice": ["A.co", "B.khong"],
    }
]

print(q["question"])
print()

choices = q["choice"]
print(*q["choice"], sep= "\n")

print()
user_choice = input("your answer ?").upper()
if user_choice == q["right_choice"]:
    print("chuan cmnr")
else:
    print("Nope")
