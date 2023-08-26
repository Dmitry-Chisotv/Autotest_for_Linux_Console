import random
import string
import subprocess
import pytest
from checkout import checkout_positive, checkout_statistics
import yaml
from datetime import datetime

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return checkout_positive(
        "mkdir {} {} {} {}".format(data['folder_in'], data['folder_out'], data['folder_ext'], data['folder_badarx']),
        "")


'''create new directories'''


@pytest.fixture()
def clear_folders():
    return checkout_positive(
        "rm -rf {}/* {}/* {}/* {}/*".format(data['folder_in'], data['folder_out'], data['folder_ext'],
                                            data['folder_badarx']), "")


'''delete data (files) from the directories'''


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(data['count_file']):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout_positive(
                "cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data['folder_in'], filename,
                                                                                       data['size_file']),
                ""):
            list_off_files.append(filename)
    return list_off_files


'''create(generate) new files'''


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout_positive("cd {}; mkdir {}".format(data['folder_in'], subfoldername), ""):
        return None, None
    if not checkout_positive(
            "cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data['folder_in'], subfoldername,
                                                                                      testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


'''create new subdirectories'''


@pytest.fixture()
def make_badarx():
    '''create bad archive for negative tests'''
    checkout_positive("cd {}; 7z a {}/badarx.7z".format(data['folder_in'], data['folder_badarx']), "Everything is Ok")
    checkout_positive("truncate -s 1 {}/badarx.7z".format(data['folder_badarx']), "Everything is Ok")
    yield 'badarx'
    checkout_positive("rm -f {}/badarx.7z".format(data['folder_badarx']), "")


@pytest.fixture()
def update_log():
    statistics = checkout_statistics('pidstat -p `pgrep -x tar` 60')
    print(datetime.now().strftime('%H:%M:%S.%f'))
    print(data['count_file'])
    print(data['size_file'])
    print(statistics)

    f = open('stat.txt', 'a')
    f.write(f"Время завершения теста: {datetime.now().strftime('%H:%M:%S.%f')} \n"
            f"Количество файлов: {data['count_file']}  \n"
            f"Размер файлов: {data['size_file']}\n"
            f"Cтатистика загрузки процессора: \n"
            f"{statistics}\n\n")
    f.close()
