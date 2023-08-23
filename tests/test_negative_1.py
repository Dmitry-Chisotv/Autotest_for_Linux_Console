from checker import checkout_negative
import pytest


badarx = '/home/user/badarx/'
tst = '/home/user/tst'
out = '/home/user/out/'
folder = '/home/user/folder1'


def test_step1():
    # Разархивируем битый архив arx2.7z в директории badarx
    assert checkout_negative("cd {}; 7z e arx2.7z -o{} -y".format(badarx, folder), "ERROR"), 'negative test1 FAIL'


def test_step2():
    # проверяем целостность битого архива arx2.7z
    assert checkout_negative("cd {}; 7z t arx2.7z".format(badarx), "ERROR"), 'negative test2 FAIL'

