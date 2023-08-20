"""Задание 1.
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в ее выводе
и False в противном случае.
Передаваться должна только одна строка,
разбиение вывода использовать не нужно.

Задание 2. (повышенной сложности).
Доработать функцию из предыдущего задания таким образом,
чтобы у нее появился дополнительный режим работы,
в котором вывод разбивается на слова с удалением всех знаков пунктуации
(их можно взять из списка string.punctuation модуля string).
В этом режиме должно проверяться наличие слова в выводе.

"""
import subprocess
import string

MENU_TASK1 = 1
MENU_TASK2 = 2
MENU_QUIT = 0


def check_action_and_text_1 (action: str, text: str):

    result = subprocess.run(action, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    print(out)
    if text in out:
        print('SUCCESS')
    else:
        print('FALSE')

def check_action_and_text_2 (action: str, text: str):

    result = subprocess.run(action, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    translator = str.maketrans("", "", string.punctuation)
    res = result.stdout.translate(translator)
    print(res)
    if text in res:
        print('SUCCESS')
    else:
        print('FALSE')


if __name__ == '__main__':

    while True:
        print(f'Введите: \n'
              f'{MENU_TASK1} для решения задачи 1 \n'
              f'{MENU_TASK2} для решения задачи 2 \n'
              f'{MENU_QUIT} или любую клавишу для выхода из меню')
        num = float(input("Ваш выбор: "))

        if num == MENU_TASK1:
            check_action_and_text_1('cat /etc/os-release', 'PRETTY_NAME="Ubuntu 22.04.1 LTS"')
            check_action_and_text_1('cat /etc/osrelease', 'PRETTYNAME="Ubuntu 22.04.1 LTS"')

        elif num == MENU_TASK2:
            check_action_and_text_2('cat /etc/os-release', 'Ubuntu')
            check_action_and_text_2('cat /etc/os-release', 'NOME')

        else:
            break





