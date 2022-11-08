import json
def get_data():
    with open('text.json', 'r', encoding='utf-8') as f: # открыть файл
        text = json.load(f) # внесли в переменную
        return text # вывели на экран