from flask import  render_template, jsonify, request, Blueprint
from web.modules.math_questions import generate_math_question
import random
from config import Config  as cf

main_blueprint = Blueprint('main', __name__)

FLASHCARDS = cf.FLASHCARDS
WORD_LISTS = cf.WORD_LISTS
TYPING_TEXTS = cf.TYPING_TEXTS

# ── ROUTES ────────────────────────────────────────────────────
# === Rota para carregar a pagina principal  ====
@main_blueprint.route('/')
def index():
    return render_template('index.html')

# === Função que acessa a função que gera perguntas e respostas das perguntas de matematica
@main_blueprint.route('/api/math/question')
def math_question():
    return jsonify(generate_math_question())

# ===
@main_blueprint.route('/api/flashcards')
def flashcards():
    cards = FLASHCARDS.copy()
    random.shuffle(cards)
    return jsonify(cards)

@main_blueprint.route('/api/memory/wordlist')
def word_list():
    words = random.choice(WORD_LISTS)
    return jsonify({'words': words, 'duration': 15})

@main_blueprint.route('/api/typing/text')
def typing_text():
    return jsonify({'text': random.choice(TYPING_TEXTS)})

@main_blueprint.route('/api/breathing/start')
def breathing_start():
    return jsonify({'phases': [
        {'name': 'Inspire', 'duration': 4, 'color': '#4FC3F7'},
        {'name': 'Segure', 'duration': 4, 'color': '#81C784'},
        {'name': 'Expire', 'duration': 6, 'color': '#FF8A65'},
        {'name': 'Pause', 'duration': 2, 'color': '#CE93D8'},
    ], 'cycles': 10})

@main_blueprint.route('/api/sudoku')
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

@main_blueprint.route('/api/creativity/challenge')
def creativity_challenge():
    challenges = [
        "Liste 10 usos alternativos para um clipe de papel.",
        "Invente 10 formas de melhorar um guarda-chuva.",
        "Crie 10 nomes para uma startup de tecnologia cognitiva.",
        "Pense em 10 soluções para reduzir a procrastinação.",
        "Imagine 10 formas de tornar o aprendizado mais divertido.",
    ]
    return jsonify({'challenge': random.choice(challenges)})

@main_blueprint.route('/api/stats/save', methods=['POST'])
def save_stats():
    data = request.json
    return jsonify({'status': 'ok', 'message': 'Progresso salvo!'})