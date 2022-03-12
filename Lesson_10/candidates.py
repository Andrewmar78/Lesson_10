import json
from flask import Flask
app = Flask(__name__)

# Получение списка кандидатов из файла
with open("candidates.json", "rt", encoding="utf-8") as file:
    candidates_datas = list(json.load(file))
# Вспомогательная печать
print(candidates_datas)


def candidate_list():
    """Функция печати списка кандидатов"""
    candidates_all = []
    for candidate in range(len(candidates_datas)):
        # print("Имя кандидата -", candidates_datas[candidate]["name"])
        # print("Позиция кандидата -", candidates_datas[candidate]["position"])
        # print(f"Навыки - {candidates_datas[candidate]['skills']}\n")
        candidate_sheet = f'Имя кандидата - {candidates_datas[candidate]["name"]}\n' \
                          f'Позиция кандидата - {candidates_datas[candidate]["position"]}\n' \
                          f'Навыки - {candidates_datas[candidate]["skills"]}\n'
        candidates_all.append(candidate_sheet)
    return "<pre>" + "\n".join(candidates_all) + "<pre>"


def profile(candidate_number):
    """Функция печати данных кандидата"""
    candidates_datas_all =[]
    # print("img src = ", candidates_datas[candidate_number]["picture"])
    # print("Имя кандидата -", candidates_datas[candidate_number]["name"])
    # print("Позиция кандидата -", candidates_datas[candidate_number]["position"])
    # print(f"Навыки - {candidates_datas[candidate_number]['skills']}\n")
    candidates_datas_sheet = f'img src = {candidates_datas[candidate_number]["picture"]}\n' \
                             f'Имя кандидата - {candidates_datas[candidate_number]["name"]}\n' \
                             f'Позиция кандидата - {candidates_datas[candidate_number]["position"]}\n' \
                             f'Навыки - {candidates_datas[candidate_number]["skills"]}'
    candidates_datas_all.append(candidates_datas_sheet)
    return "<pre>" + "\n".join(candidates_datas_all) + "<pre>"


def skills_list(skill):
    """Функция печати списка кандидатов по их навыкам"""
    candidates_skills_all = []
    for candidate in range(len(candidates_datas)):
        if skill.lower() in candidates_datas[candidate]["skills"] or skill in candidates_datas[candidate]["skills"] or\
                skill.title() in candidates_datas[candidate]["skills"]:
            # print("Имя кандидата -", candidates_datas[candidate]["name"])
            # print("Позиция кандидата -", candidates_datas[candidate]["position"])
            # print(f"Навыки - {candidates_datas[candidate]['skills']}\n")
            candidates_skills_sheet = f'img src = {candidates_datas[candidate]["picture"]}\n' \
                                     f'Имя кандидата - {candidates_datas[candidate]["name"]}\n' \
                                     f'Позиция кандидата - {candidates_datas[candidate]["position"]}\n' \
                                     f'Навыки - {candidates_datas[candidate]["skills"]}\n'
        candidates_skills_all.append(candidates_skills_sheet)
    return "<pre>" + "\n".join(candidates_skills_all) + "<pre>"


@app.route("/")
def main_page():
    return candidate_list()


@app.route("/candidate/<int:candidate_number>")
def profile_page(candidate_number):
    return profile(candidate_number)


@app.route("/skill/<skill_chosen>")
def skill_page(skill_chosen):
    return skills_list(skill_chosen)


# Запуск сервера
app.run()
