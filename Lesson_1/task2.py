"""Доработать тест из предыдущего задания таким образом,
чтобы вывод сохранялся построчно в список и в тесте проверялось,
что в этом списке есть строки VERSION="22.04.1 LTS (Jammy Jellyfish)"
и VERSION_CODENAME=jammy .
Проверка должна выполняться только если код возврата равен 0.
"""

import subprocess

if __name__ == '__main__':
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    print(out)
    if result.returncode ==0:
        lst = out.split('\n')
        if 'PRETTY_NAME="Ubuntu 22.04.1 LTS"' in lst and 'VERSION="22.04.1 LTS" (Jammy Jellyfish)"' in lst:
            print('SUCCESS')
        else:
            print('FALSE')
    else:
        print('FALSE! Code != 0')








