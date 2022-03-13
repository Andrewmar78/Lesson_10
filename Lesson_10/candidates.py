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
    for candidate in range(len(candidates_datas)):
        if candidates_datas[candidate]["id"] == int(candidate_number):
            # print("img src = ", candidates_datas[candidate_number]["picture"])
            # print("Имя кандидата -", candidates_datas[candidate_number]["name"])
            # print("Позиция кандидата -", candidates_datas[candidate_number]["position"])
            # print(f"Навыки - {candidates_datas[candidate_number]['skills']}\n")
            candidates_datas_sheet = f'<img src = {candidates_datas[candidate_number-1]["picture"]}>\n' \
                                     f'Имя кандидата - {candidates_datas[candidate_number-1]["name"]}\n' \
                                     f'Позиция кандидата - {candidates_datas[candidate_number-1]["position"]}\n' \
                                     f'Навыки - {candidates_datas[candidate_number-1]["skills"]}'
            candidates_datas_all.append(candidates_datas_sheet)
    if not candidates_datas_all:
        candidates_datas_all = [f'<img src = https://clipart-best.com/img/skeleton/skeleton-clip-art-60.png'
                                f' width="200" height="300">\n' f'Такого кандидата нет!']
    return "<pre>" + "\n".join(candidates_datas_all) + "<pre>"


def skills_list(skill):
    """Функция печати списка кандидатов по их навыкам"""
    candidates_skills_all = []
    for candidate in range(len(candidates_datas)):
        skill_check = candidates_datas[candidate]["skills"].split(", ")
        # print("Все навыки кандидата", candidate, "- ", skill_check)
        if skill.lower() in skill_check or skill in skill_check or\
                skill.title() in skill_check:
            candidates_skills_sheet = f'<img src={candidates_datas[candidate]["picture"]}>\n' \
                                     f'Имя кандидата - {candidates_datas[candidate]["name"]}\n' \
                                     f'Позиция кандидата - {candidates_datas[candidate]["position"]}\n' \
                                     f'Навыки - {candidates_datas[candidate]["skills"]}\n'
            candidates_skills_all.append(candidates_skills_sheet)
            # print("Имя кандидата -", candidates_datas[candidate]["name"])
            # print("Позиция кандидата -", candidates_datas[candidate]["position"])
            # print(f"Навыки - {candidates_datas[candidate]['skills']}\n")
    if not candidates_skills_all:
        candidates_skills_all = [f'<img src =https://avatars.mds.yandex.net/get-zen_doc/1706643/'
                                 f'pub_5de27ce4118d7f00ad5ada5f_5dea964d98930900adc8b642/scale_1200>\n'
                                 f'Кандидатов с такими навыками нет!']
    return "<pre>" + "\n".join(candidates_skills_all) + "<pre>"


# Страничка всех кандидатов
@app.route("/")
def main_page():
    return candidate_list()


# Страничка данных выбранного кандидата, если он есть
@app.route("/candidate/<int:candidate_number>")
def profile_page(candidate_number):
    return profile(candidate_number)


# Страничка списка кандидатов по выбранному навыку, если такой навык есть
@app.route("/skill/<skill_chosen>")
def skill_page(skill_chosen):
    return skills_list(skill_chosen)


# Запуск сервера
app.run()
