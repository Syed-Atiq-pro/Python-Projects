<div align="center">

```
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗███████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   ███████╗
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   ╚════██║
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   ███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝
```

### 🛠️ Real Python Projects Built While Learning — By a First-Year CS Student

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![Projects](https://img.shields.io/badge/Projects-Building%20🔨-brightgreen?style=for-the-badge)
![Beginner](https://img.shields.io/badge/Level-Beginner%20Friendly-blue?style=for-the-badge)
![Live](https://img.shields.io/badge/Live%20on-GitHub%20Pages-181717?style=for-the-badge&logo=github)

<br>

> **"Tell me and I forget. Teach me and I remember. Involve me and I learn."** — Benjamin Franklin

---

</div>

## 👨‍💻 About This Repository

I'm **Syed Atiq** — a B.Tech CSE (IoT) student from Vijayawada, India, learning Python from absolute zero.

This repo is where I **apply** what I learn. Every project here was built hands-on by me while studying Python concepts. No copy-paste, no shortcuts — just real code, real logic, real learning.

**The idea is simple:**
> Learn a concept → Build something with it → Push to GitHub → Repeat. 🔁

---

## 🚀 Projects Collection

---

### 🧮 Project 01 — Calculator

![Python](https://img.shields.io/badge/Python-Basics-3776AB?style=flat-square&logo=python&logoColor=white)
![Concepts](https://img.shields.io/badge/Concepts-Functions%20%7C%20Conditions%20%7C%20Loops-orange?style=flat-square)

**What it does:**
A clean command-line calculator that performs addition, subtraction, multiplication, and division with proper error handling (like divide-by-zero protection).

**What I learned building this:**
- Writing and calling functions
- Using if/elif/else conditions
- Handling user input safely
- Basic error handling with try/except

```python
def calculator():
    print("=" * 30)
    print("   🧮 Simple Python Calculator")
    print("=" * 30)
    
    num1 = float(input("Enter first number: "))
    op   = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == '+':   result = num1 + num2
    elif op == '-': result = num1 - num2
    elif op == '*': result = num1 * num2
    elif op == '/':
        if num2 == 0:
            return print("❌ Error: Cannot divide by zero!")
        result = num1 / num2
    else:
        return print("❌ Invalid operator!")

    print(f"\n✅ Result: {num1} {op} {num2} = {result}")

calculator()
```

---

### 🎲 Project 02 — Number Guessing Game

![Python](https://img.shields.io/badge/Python-Basics-3776AB?style=flat-square&logo=python&logoColor=white)
![Concepts](https://img.shields.io/badge/Concepts-Random%20%7C%20Loops%20%7C%20Logic-orange?style=flat-square)

**What it does:**
The computer picks a secret number between 1–100. You get hints (higher/lower) and limited attempts to guess it.

**What I learned building this:**
- Using the `random` module
- while loops with conditions
- Giving user feedback based on logic
- Counting attempts

```python
import random

def guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    max_tries = 7

    print("🎲 I'm thinking of a number between 1 and 100!")
    print(f"   You have {max_tries} attempts. Good luck!\n")

    while attempts < max_tries:
        guess = int(input(f"Attempt {attempts+1}/{max_tries} → Your guess: "))
        attempts += 1

        if guess < secret:
            print("   📈 Too LOW! Go higher.\n")
        elif guess > secret:
            print("   📉 Too HIGH! Go lower.\n")
        else:
            print(f"   🎉 CORRECT! You got it in {attempts} attempt(s)!")
            return

    print(f"   😔 Game Over! The number was {secret}.")

guessing_game()
```

---

### 📋 Project 03 — To-Do List App

![Python](https://img.shields.io/badge/Python-Intermediate-3776AB?style=flat-square&logo=python&logoColor=white)
![Concepts](https://img.shields.io/badge/Concepts-Lists%20%7C%20Functions%20%7C%20Menu%20Logic-orange?style=flat-square)

**What it does:**
A terminal-based to-do list where you can add tasks, view all tasks, mark them complete, and delete them.

**What I learned building this:**
- Managing lists dynamically
- Building a menu-driven program
- Using functions to keep code clean
- Real-world CRUD logic (Create, Read, Update, Delete)

```python
tasks = []

def show_tasks():
    if not tasks:
        print("📭 No tasks yet! Add one.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "⏳"
            print(f"   {i}. {status} {task['name']}")

def add_task():
    name = input("Enter task: ")
    tasks.append({"name": name, "done": False})
    print(f"   ✅ '{name}' added!")

def complete_task():
    show_tasks()
    idx = int(input("Enter task number to complete: ")) - 1
    tasks[idx]["done"] = True
    print("   🎉 Task marked complete!")

def delete_task():
    show_tasks()
    idx = int(input("Enter task number to delete: ")) - 1
    removed = tasks.pop(idx)
    print(f"   🗑️ '{removed['name']}' deleted!")

# Main menu loop
while True:
    print("\n" + "="*30)
    print("  📋 TO-DO LIST — MAIN MENU")
    print("  1. View Tasks")
    print("  2. Add Task")
    print("  3. Complete Task")
    print("  4. Delete Task")
    print("  5. Exit")
    choice = input("\n  Choose (1-5): ")

    if choice == "1":   show_tasks()
    elif choice == "2": add_task()
    elif choice == "3": complete_task()
    elif choice == "4": delete_task()
    elif choice == "5": print("👋 Goodbye!"); break
    else: print("❌ Invalid choice.")
```

---

### 🔐 Project 04 — Password Strength Checker

![Python](https://img.shields.io/badge/Python-Intermediate-3776AB?style=flat-square&logo=python&logoColor=white)
![Concepts](https://img.shields.io/badge/Concepts-String%20Methods%20%7C%20Logic%20%7C%20Regex-orange?style=flat-square)

**What it does:**
Checks how strong your password is — Weak, Medium, or Strong — based on length, uppercase, numbers, and special characters.

**What I learned building this:**
- String methods (`.isupper()`, `.isdigit()`, etc.)
- Writing scoring logic
- Using `any()` with conditions

```python
def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters needed")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("❌ Add numbers")

    if any(c in "!@#$%^&*()" for c in password):
        score += 1
    else:
        feedback.append("❌ Add special characters (!@#$...)")

    levels = {4: "🟢 STRONG", 3: "🟡 MEDIUM", 2: "🟠 WEAK", 1: "🔴 VERY WEAK"}
    strength = levels.get(score, "🔴 VERY WEAK")

    print(f"\n🔐 Password Strength: {strength}")
    if feedback:
        print("💡 Suggestions:")
        for tip in feedback:
            print(f"   {tip}")

password = input("Enter your password: ")
check_password(password)
```

---

## 📊 Projects at a Glance

| # | Project | Core Concepts | Difficulty |
|---|---------|--------------|------------|
| 01 | 🧮 Calculator | Functions, Conditions, try/except | ⭐ Beginner |
| 02 | 🎲 Number Guessing Game | Random, while loops, Logic | ⭐ Beginner |
| 03 | 📋 To-Do List | Lists, CRUD, Menu Logic | ⭐⭐ Easy |
| 04 | 🔐 Password Checker | Strings, any(), Scoring Logic | ⭐⭐ Easy |
| 05 | 📊 Student EDA | Pandas, NumPy, Matplotlib | ⭐⭐⭐ Intermediate |

> 📌 More projects being added as I level up!

---

## ⚡ How to Run Any Project

### Option 1 — Google Colab *(No Installation — Works on Phone!)*
```
1. Open → colab.research.google.com
2. File → Open Notebook → GitHub tab
3. Paste → github.com/Syed-Atiq-pro/Python-Projects
4. Open any .ipynb and click ▶ Run
```

### Option 2 — Run Locally
```bash
git clone https://github.com/Syed-Atiq-pro/Python-Projects.git
cd Python-Projects
python project_name.py
```

---

## 🧠 What This Repo Proves

```
✅  I learn by building — not just reading
✅  I write clean, readable, commented code
✅  I push code publicly — accountability matters
✅  I'm growing from beginner to Data Science
✅  Every project solves a real problem
```

---

## 🔗 Find Me Here

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-black?style=for-the-badge&logo=github)](https://Syed-Atiq-pro.github.io/portfolio)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/atiq-syed-159b6b372)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/Syed-Atiq-pro)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:syedatiq4953@gmail.com)

</div>

---

<div align="center">

**⭐ If you're also learning Python — star this repo and let's grow together!**

*Made with ❤️ and a lot of debugging by Syed Atiq*
*B.Tech CSE (IoT) · PSCMR College · Vijayawada · 2024–2028*

</div>
