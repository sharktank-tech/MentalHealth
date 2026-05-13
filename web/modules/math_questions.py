import random


# ── MATH QUESTIONS ────────────────────────────────────────────
def generate_math_question():
    ops = ['+', '-', '*']
    op = random.choice(ops)
    if op == '*':
        a, b = random.randint(2, 12), random.randint(2, 12)
    else:
        a, b = random.randint(10, 99), random.randint(10, 99)
    if op == '-' and b > a:
        a, b = b, a
    answer = eval(f"{a}{op}{b}")
    return {'question': f"{a} {op} {b}", 'answer': answer}