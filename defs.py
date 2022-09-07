import re


def line_names(contacts_list):
    for contact in contacts_list:
        contact[0] = contact[0] + ' ' + contact[1] + ' ' + contact[2]
        contact[1], contact[2] = '', ''
        contact[0] = contact[0].split()
        if len(contact[0]) == 3:
            contact[1] = contact[0][1]
            contact[2] = contact[0][2]
            contact[0] = contact[0][0]
        else:
            contact[1] = contact[0][1]
            contact[0] = contact[0][0]
        if len(contact) > 7 and contact[-1] == '':
            contact.pop(-1)


def check_repeatable_names(contacts_list, repeatable_contacts):
    for contact in contacts_list:
        for suspect in contacts_list:
            if contact[0] == suspect[0] and contact[1] == suspect[1] and contact != suspect:
                repeatable_contacts.append(contact)


def add_data(repeatable_contacts):
    for repeatable_person in repeatable_contacts:
        base = -1
        for info in repeatable_person:
            base += 1
            if info == '':
                for repeatable_person_ in repeatable_contacts:
                    if repeatable_person_[0] == repeatable_person[0] and repeatable_person_[1] == repeatable_person[
                        1] and repeatable_person != repeatable_person_:
                        repeatable_person[base] = repeatable_person_[base]


def change_names(contacts_list, repeatable_contacts):
    for contact in contacts_list:
        for repeatable_person in repeatable_contacts:
            if contact[0] == repeatable_person[0] and contact[1] == repeatable_person[
                1] and contact != repeatable_person:
                contact = repeatable_person


def create_new_list(contacts_list, new_contacts_list):
    for contact in contacts_list:
        if contact not in new_contacts_list:
            new_contacts_list.append(contact)


def change_phone(pattern1, substitution1, new_contacts_list):
    for phone in new_contacts_list:
        changed_phone = re.sub(pattern1, substitution1, phone[-2])
        phone[-2] = changed_phone.strip()
