#!/usr/bin/env python3

__author__ = "Alan Veloso (alantsv@gmail.com)"

import re

def auth_name(name):
    if re.match(r'[A-Z]{1}[a-z]* [A-Z]{1}[a-z]*$', name):
        return True
    return False


def auth_email(email):
    if re.match(rw'[a-z]+@[a-z]+.br$', email):
        return True
    return False

def auth_passwd(passwd):
    if re.match(r'[A-Za-z0-9]*([A-Z]{1}[A-Za-z0-9]*[0-9]{1}[A-Za-z0-9]*|[0-9]{1}[A-Za-z0-9]*[A-Z]{1}[A-Za-z0-9]*)$', passwd) and len(passwd) == 8:
        return True
    return False

def auth_cpf(cpf):
    if re.match(r'[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}$', cpf):
        return True
    return False

def auth_rg(rg):
    if re.match(r'[0-9]{6}-[0-9]{1}$', rg):
        return True
    return False

def auth_phone(phone):
    if re.match(r'\([0-9]{2}\) [0-9]{5}-[0-9]{4}$', phone):
        return True
    return False

def auth_cep(cep):
    if re.match(r'[0-9]{2}.[0-9]{3}-[0-9]{3}$', cep):
        return True
    return False

def auth_date_and_time(date_and_time):
    if re.match(r'[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}$', date_and_time):
        return True
    return False

def auth_float(float):
    if re.match(r'[+-]?[0-9]+([.,]?[0-9]+|[0-9]*)$', float):
        return True
    return False

def main():
    names = ["Alan Turing", "Alan", "Alan TurinG", ""]
    auth_names = {name: auth_name(name) for name in names}
    print(auth_names)

    emails = ['divulga@ufpa.br', 'a@.br', '@.br', '']
    auth_emails = {email: auth_email(email) for email in emails}
    print(auth_emails)

    passwds = ['518R2r5e', 'F1234567A', '12345678', 'abcdefghi', 'A2', '']
    auth_passwds = {passwd: auth_passwd(passwd) for passwd in passwds}
    print(auth_passwds)

    cpfs = ['123.456.789-10', '12345678910', '123.456.78910', '']
    auth_cpfs = {cpf: auth_cpf(cpf) for cpf in cpfs}
    print(auth_cpfs)

    rgs = ['875467-2', '8754672', '']
    auth_rgs = {rg: auth_rg(rg) for rg in rgs}
    print(auth_rgs)

    phones = ['(91) 99363-1167', '(91) 993631167', '99363-1167', '']
    auth_phones = {phone: auth_phone(phone) for phone in phones}
    print(auth_phones)

    ceps = ['66.645-225', '66645-225', '66645225', '']
    auth_ceps = {cep: auth_cep(cep) for cep in ceps}
    print(auth_ceps)

    dates_and_times = ['31/08/2019 20:14:55', ' 31/08/2019 20:14:55 ', '']
    auth_dates_and_times = {date_and_time: auth_date_and_time(date_and_time) for date_and_time in dates_and_times}
    print(auth_dates_and_times)

    floats = ['-25,467', '-25,4.67', '+-65.2', '']
    auth_floats = {float: auth_float(float) for float in floats}
    print(auth_floats)

if __name__ == "__main__":
    main()
