"""Задание 1.

Условие:
Дополнить проект тестами, проверяющими команды вывода списка файлов (l)
и разархивирования с путями (x).

*Задание 2. *

• Установить пакет для расчёта crc32
sudo apt install libarchive-zip-perl
• Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32."""

from checker import checkout, checkout_hash_h, checkout_hash_32

source = '/home/user/source'
archive = '/home/user/archive'
result = '/home/user/result'



def test_step1():
    # Проверяем отображение и наличие файлов test2 и test3 в директории source
    assert checkout("ls -l {}".format(source), "test2" and "test3"), 'test 1 for DZ2 is FAIL'


def test_step2():
    # Создаем архив в директории archive и затем распаковываем архив DZ2.7z в директории result
    # Проверяем наличие файлов test2 и test3 в директории result
    res1 = checkout("cd {}; 7z a {}/DZ2".format(source, archive), "Everything is Ok")
    res2 = checkout("cd {}; 7z x DZ2.7z -o{} -y".format(archive, result), "Everything is Ok")
    res3 = checkout("ls -l {}".format(source), "test2" and "test3")
    assert res1 and res2 and res3, 'test 2 for DZ2 is FAIL'

def test_step3():
    # Примечание: Код на Windows подсвечитвает result_32 в 37й строке как несуществующий параметр, в то время как в линуксе данный код запускается.
    result_32 = checkout_hash_32("cd {}; crc32 DZ2.7z".format(archive).replace('\n', '').upper()
    result_h = checkout_hash_h("cd {}; 7z h DZ2.7z".format(archive), result_32)
    assert result_h == True, 'test 3 for DZ2 is FAIL'
