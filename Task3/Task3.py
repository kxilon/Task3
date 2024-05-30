
import json


with open('values.json', 'r') as values_file:
    values_data = json.load(values_file)

with open('tests.json', 'r') as tests_file:
    tests_data = json.load(tests_file)

values_dict = {entry['id']: entry['value'] for entry in values_data['values']}

def update_tests(tests):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            update_tests(test['values'])

update_tests(tests_data['tests'])

with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=2, ensure_ascii=False)
