import re
import csv
from defs import line_names, check_repeatable_names, add_data, change_names, create_new_list

repeatable_contacts = []
base = 0
new_contacts_list = []
contacts = ''
pattern1 = r"(\+7|8)[\s]?\(?(\d+)\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})[ ]\(?доб. (\d+)"
substitution1 = r"+7(\2)\3-\4-\5 доб.\6"
result = []

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    line_names(contacts_list)
    check_repeatable_names(contacts_list, repeatable_contacts)
    add_data(repeatable_contacts)
    change_names(contacts_list, repeatable_contacts)
    create_new_list(contacts_list, new_contacts_list)
    for new_contact in new_contacts_list:
        changed_phone = re.sub(pattern1, substitution1, new_contact[-2])
        new_contact[-2] = changed_phone.strip()

    with open("phonebook.csv", "w", encoding='1251') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)
