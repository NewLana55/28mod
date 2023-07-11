from faker import Faker

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    first_name_1_char = 'С'
    first_name_31_char = 'СветланаСветланаСветланаСвкетланаСветланаСветлана'
    last_name_1_char = 'И'
    last_name_31_char = 'ИвановаСветланаСветланаСвкетланаСветланаСветлана'
    password_21_char = 'Qwerty1Qwerty1Qwerty1'
    password_no_Lower = 'qwertyu1'
    password_9_char = 'Qwertyu15'
    password_not_contain_digit = "Qwertyui"
    xss = '<script>alert(321)</script>'
    email_without_domain = 'test@.ru'
    invalid_phoneNumber = '++70000000000'


class Valid_Data:
    valid_first_name = 'Иван'
    valid_last_name = 'Иванов'
    valid_password = 'Qwertyu0'
    valid_phoneNumber = '+79178105395'