from flask import Flask, render_template, jsonify, request, session
import random
import time
import json

app = Flask(__name__)
app.secret_key = 'braintrainer_secret_2024'

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

# ── FLASHCARDS ─────────────────────────────────────────────────
FLASHCARDS = [
    {"front": "O que é Neuroplasticidade?", "back": "A capacidade do cérebro de reorganizar conexões neurais ao longo da vida."},
    {"front": "Método Feynman", "back": "Aprenda → Simplifique → Ensine como se fosse para uma criança → Revise as lacunas."},
    {"front": "O que é Repetição Espaçada?", "back": "Técnica de estudo que revisa o conteúdo em intervalos crescentes para reforçar a memória de longo prazo."},
    {"front": "Teorema de Pitágoras", "back": "a² + b² = c² — em todo triângulo retângulo, o quadrado da hipotenusa é igual à soma dos quadrados dos catetos."},
    {"front": "O que é Flow State?", "back": "Estado de imersão total em uma atividade, onde o desafio e a habilidade estão em equilíbrio perfeito."},
    {"front": "Memória de Trabalho", "back": "Sistema cognitivo que mantém informações temporariamente para uso imediato. Capacidade: ~7 itens simultaneamente."},
    {"front": "O que é Dopamina?", "back": "Neurotransmissor associado à motivação, recompensa e aprendizado. Essencial para formar novos hábitos."},
    {"front": "Técnica Pomodoro", "back": "25 minutos de foco total + 5 minutos de pausa. Após 4 ciclos, pausa longa de 15–30 min."},
    {"front": "O que é Sono REM?", "back": "Fase do sono onde ocorre consolidação de memórias e processamento emocional. Essencial para aprendizado."},
    {"front": "Inteligência Fluida vs Cristalizada", "back": "Fluida: raciocinar sobre novos problemas. Cristalizada: conhecimento acumulado e experiência. Ambas se complementam."},
]

# ── WORD LIST (memory training) ────────────────────────────────
WORD_LISTS = [
    ["elefante", "foguete", "biblioteca", "oceano", "violão", "cristal", "névoa", "tsunami"],
    ["algoritmo", "constelação", "fotossíntese", "melanina", "gravidade", "paradoxo", "sinfonia", "equilíbrio"],
    ["labirinto", "hemisférios", "neurônio", "katana", "horizonte", "bússola", "frequência", "espectro"],
]

# ── TYPING TEXTS ───────────────────────────────────────────────
TYPING_TEXTS = [
    "O cérebro humano contém aproximadamente 86 bilhões de neurônios conectados.",
    "A prática deliberada é o segredo do alto desempenho em qualquer área.",
    "Dormir bem é tão importante quanto estudar para consolidar o aprendizado.",
    "O exercício físico libera BDNF, uma proteína que estimula o crescimento neural.",
    "Leia, resuma, ensine e aplique — este é o ciclo do aprendizado profundo.",
]

# ── ROUTES ────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

#https://www.flaticon.com/authors/hajicon

@app.route('/api/math/question')
def math_question():
    return jsonify(generate_math_question())

@app.route('/api/flashcards')
def flashcards():
    cards = FLASHCARDS.copy()
    random.shuffle(cards)
    return jsonify(cards)

@app.route('/api/memory/wordlist')
def word_list():
    words = random.choice(WORD_LISTS)
    return jsonify({'words': words, 'duration': 15})

@app.route('/api/typing/text')
def typing_text():
    return jsonify({'text': random.choice(TYPING_TEXTS)})

@app.route('/api/breathing/start')
def breathing_start():
    return jsonify({'phases': [
        {'name': 'Inspire', 'duration': 4, 'color': '#4FC3F7'},
        {'name': 'Segure', 'duration': 4, 'color': '#81C784'},
        {'name': 'Expire', 'duration': 6, 'color': '#FF8A65'},
        {'name': 'Pause', 'duration': 2, 'color': '#CE93D8'},
    ], 'cycles': 10})

@app.route('/api/sudoku')
def sudoku():
    # Simple pre-generated sudoku puzzle
    puzzle = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9],
    ]
    solution = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9],
    ]
    return jsonify({'puzzle': puzzle, 'solution': solution})

@app.route('/api/creativity/challenge')
def creativity_challenge():
    challenges = [
        "Liste 10 usos alternativos para um clipe de papel.",
        "Invente 10 formas de melhorar um guarda-chuva.",
        "Crie 10 nomes para uma startup de tecnologia cognitiva.",
        "Pense em 10 soluções para reduzir a procrastinação.",
        "Imagine 10 formas de tornar o aprendizado mais divertido.",
    ]
    return jsonify({'challenge': random.choice(challenges)})

@app.route('/api/stats/save', methods=['POST'])
def save_stats():
    data = request.json
    return jsonify({'status': 'ok', 'message': 'Progresso salvo!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)