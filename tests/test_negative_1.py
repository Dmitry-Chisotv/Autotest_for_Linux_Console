from checkout import checkout_negative
import yaml


with open('config.yaml') as f:
    data = yaml.safe_load(f)


def test_step1(make_files):
    # test1
    assert checkout_negative("cd {}; 7z e badarx.7z -o{} -y".format(data['folder_badarx'], data['folder_ext']), "ERROR"), "Test4 Fail"


def test_step2():
    # test2
    assert checkout_negative("cd {}; 7z t badarx.7z".format(data['folder_badarx']), "ERROR"), "Test5 Fail"

def test_step3():
    # test3
    assert checkout_negative("cd {}; 7z e -tzip {}/arx1.zp".format(data['folder_in'], data['folder_badarx']), "ERROR"), "Test1 Fail"

def test_step4():
    # test4
    assert checkout_negative("cd {}; 7z a -tzp {}/arx1.zip".format(data['folder_in'], data['folder_badarx']), "ERROR"), "Test1 Fail"

