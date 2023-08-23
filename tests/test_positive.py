import subprocess
import pytest

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    res1 = checkout("cd /home/user/tst; 7z a /home/user/out/arx2", "Everything is Ok")
    res2 = checkout("ls /home/user/out", "arx2.7z")
    assert res1 and res2, 'test FAIL'


def test_step2():
    res1 = checkout("cd /home/user/out; 7z e arx2.7z -o /home/user/folder1 -y", "Everything is Ok")
    res2 = checkout("ls /home/user/folder1", "test2")
    res3 = checkout("ls /home/user/folder1", "test3")
    assert res1 and res2 and res3, 'test FAIL'


def test_step3():
    assert checkout("cd /home/user/out; 7z t arx2.7z", "Everything is Ok"), 'TEST_STEP3 FAIL'












