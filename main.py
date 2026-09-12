from pathlib import Path
import random

folder = Path(__file__).parent / "frineds"
files = sorted(folder.glob("*.txt"))
if not files:
    print("Please put your frined.txt")
frined_file = random.choice(files)
lines = frined_file.read_text(encoding="utf-8-sig").splitlines()
clean_line = []
for line in lines:
    clean_line.append(line.strip())
answer = clean_line[0]
clues = clean_line[1:]
print("เพื่อนคนนี้ คือใคร ???")
print("คำตอบเป็นชื่อแคน ทายได้คำใบ้ละ 1 ครั้ง \n")

for number, clue in enumerate(clues, start=1):
    print(f"{number} คำใบ้ :  {clue} ?")
    guess = input("ทายชื่อ เพื่อนจากคำใบ้ ด้านบน ? \n").strip()

    if guess.casefold() == answer.casefold():
        print(" Correct !!!!")
        break
    print("ทายใหม่ อีกครั้ง ?")
print(f" เฉลย : เพื่อนคนนี้ คือ : {answer}")
