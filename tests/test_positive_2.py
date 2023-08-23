from checker import checkout
import pytest

tst = '/home/user/tst'
out = '/home/user/out/'
folder = '/home/user/folder1'



def test_step1():
    # Создаем архив arx2 и проверяем его наличие  в директории out
    res1 = checkout("cd {}; 7z a {}arx2".format(tst, out), "Everything is Ok")
    res2 = checkout("ls {}".format(out), "arx2.7z")
    assert res1 and res2, 'test FAIL'


def test_step2():
    # Разархивируем архив arx2.7z в директории folder1
    # и проверяем наличие файлов test2 и test3 в данной директории folder1
    res1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(out, folder), "Everything is Ok")
    res2 = checkout("ls {}".format(folder), "test2")
    res3 = checkout("ls {}".format(folder), "test3")
    assert res1 and res2 and res3, 'test FAIL'


def test_step3():
    # проверяем целостность архива arx2.7z
    assert checkout("cd {}; 7z t arx2.7z".format(out), "Everything is Ok"), 'TEST_STEP3 FAIL'


def test_step4():
    # проверяем возможность обновить файлы  в архиве arx2.7z
    assert checkout("cd {}; 7z u {}/arx2.7z".format(tst, out), "Everything is Ok"), 'TEST_STEP4 FAIL'


def test_step5():
    # удаляем файлы из архива arx2.7z (очищаем его)
    assert checkout("cd {}; 7z d arx2.7z".format(out), "Everything is Ok"), 'test_step5 FAIL'





