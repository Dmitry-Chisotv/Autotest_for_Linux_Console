from checkout import checkout_positive
import yaml


with open('config.yaml') as f:
    data = yaml.safe_load(f)

def test_step1(make_folders, make_files, update_log):
    # test1 - create the archive
    res1 = checkout_positive("cd {}; 7z a -t{} {}/arx1.{}".format(data['folder_in'],
                                                                  data['type_archive'], data['folder_out'], data['type_archive']
                                                                  ), "Everything is Ok"), "Test1 Fail"
    res2 = checkout_positive("ls {}".format(data['folder_out']), "arx.{}".format(['type_archive'])), "Test1 Fail"
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files, update_log):
    # test2
    res = []
    res.append(checkout_positive("cd {}; 7z a -t{} {}/arx1.{}".format(data['folder_in'],
                                                                  data['type_archive'], data['folder_out'], data['type_archive']
                                                                  ), "Everything is Ok"))
    res.append(checkout_positive("cd {}; 7z e arx1.{} -o{} -y".format(data['folder_out'], data['type_archive'],
                                                                      data['folder_ext']), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("ls {}".format(data['folder_ext']), item))
    assert all(res)


def test_step3(update_log):
    # test3 - check the status
    assert checkout_positive("cd {}; 7z t {}/arx1.{}".format(data['folder_in'], data['folder_out'],
                                                             data['type_archive']), "Everything is Ok"), "Test1 Fail"


def test_step4(update_log):
    # test4 -
    assert checkout_positive("cd {}; 7z u {}/arx1.{}".format(data['folder_in'], data['folder_out'],
                                                             data['type_archive']), "Everything is Ok"), "Test1 Fail"


def test_step5(clear_folders, make_files, update_log):
    # test5 - create new archive and show consist of the archive
    res = []
    res.append(checkout_positive("cd {}; 7z a {}/arx1.{}".format(data['folder_in'], data['folder_out'],
                                                                 data['type_archive']), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("cd {}; 7z l arx1.{}".format(data['folder_out'], data['type_archive']), item))
    assert all(res)


# def test_step6():



def test_step7(update_log):
    assert checkout_positive("7z d {}/arx1.{}".format(data['folder_out'], data['type_archive']),
                             "Everything is Ok"), "Test1 Fail"
