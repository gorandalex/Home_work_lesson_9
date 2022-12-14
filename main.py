

dict_telefones = {}


def input_error(func):
    """Обробляемо помилки, якіх міг припуститись користувач"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Ви ввели не вірне ім'я"
        except TypeError:
            return "Ви ввели не вірний форат команди"
        except IndexError:
            return "Введіть ім'я та телефон"
        except ValueError as e:
            return e.args[0]
        except Exception as e:
            return e.args

    return wrapper


@input_error
def answer_hello():
    """Привітаємо користувача"""
    return 'How can I help you?'

@input_error
def answer_add(name_telephone):
    """Додаємо телефон до словника"""
    lst_name_telefon = name_telephone.strip().split()
    name = lst_name_telefon[0]
    if name in dict_telefones:
        raise ValueError("Ім'я вже є у списку. Введіть іньше")
    telephone = lst_name_telefon[1]
    dict_telefones[name] = telephone
    return f'Для {name} записан телефон {telephone}'

@input_error
def answer_change(name_telephone):
    """Змінюємо телефон в словнику"""
    lst_name_telefon = name_telephone.strip().split()
    name = lst_name_telefon[0]
    telephone = lst_name_telefon[1]
    old_telefone = dict_telefones[name]
    dict_telefones[name] = telephone
    return f'Для {name} змінено телефон {old_telefone} на {telephone}'

@input_error
def answer_phone(name):
    """Повертаємо телефон за ім'ям"""
    telephone = dict_telefones[name.strip()]
    return telephone

@input_error
def answer_showall():
    """Виводимо всі телефони"""
    return '\n'.join([f'{name} {telephone}' for name, telephone in dict_telefones.items()])

@input_error
def answer_exit():
    return 'Good bye!'

@input_error
def command_error():
    return 'Ви ввели не вірну команду'

"""Створимо словник команд для пошуку потрібних методів"""
DICT_COMMANDS = {
                    'hello': answer_hello,
                    'add': answer_add,
                    'change': answer_change,
                    'phone': answer_phone,
                    'show all': answer_showall,
                    'exit': answer_exit,
                    'good bye': answer_exit,
                    'close': answer_exit
                }

def get_answer_function(answer):
    """Повертаємо потрибний метод для команди користувача"""
    return DICT_COMMANDS.get(answer, command_error)


@input_error
def run_command(user_command):
    command = user_command
    params = ''
    for key in DICT_COMMANDS:
        if user_command.lower().startswith(key):
            command = key
            params = user_command[len(command):]
            break
    if params:
        return get_answer_function(command)(params)
    else:
        return get_answer_function(command)()


def main():
    while True:
        user_command = input('Введіть команду для бота: ')
        answer = run_command(user_command.strip())
        print(answer)
        if answer == 'Good bye!':
            break

if __name__ == "__main__":
    main()
        