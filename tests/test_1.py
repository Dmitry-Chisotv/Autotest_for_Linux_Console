import subprocess
import pytest

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

def test_step1():
    assert checkout("cd /home/user/tst; 7z a /home/user/out/arx2"), 'TEST1 FAIL'

@pytest.mark.run_this
def test_step2():
    assert checkout("cd/home1/......"), 'TEST2 FAIL'

def test_step3():
    assert checkout("cd/1home/......"), 'TEST3 FAIL'












