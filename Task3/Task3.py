
import json

# Загрузка данных из файлов values.json и tests.json
with open('values.json', 'r') as values_file:
    values_data = json.load(values_file)

with open('tests.json', 'r') as tests_file:
    tests_data = json.load(tests_file)

# Формирование словаря для быстрого доступа к значениям по id
values_dict = {entry['id']: entry['value'] for entry in values_data['values']}

# Функция для обновления значений в тестах
def update_tests(tests):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            update_tests(test['values'])

# Обновление значений в тестах
update_tests(tests_data['tests'])

# Сохранение результата в файл report.json
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=2, ensure_ascii=False)