import yaml
from checker import checkout

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestPositive:


    def test_step1(self, make_folders, clear_folders, make_files):
        # Создаем архив arx2 и проверяем его наличие  в директории out
        res1 = checkout("cd {}; 7z a {}arx2".format(data['tst'], data['out']), "Everything is Ok")
        res2 = checkout("ls {}".format(data['out']), "arx2.7z")
        assert res1 and res2, 'test FAIL'


    def test_step2(self, clear_folders, make_files):
        # Разархивируем архив arx2.7z в директории folder1
        # и проверяем наличие файлов test2 и test3 в данной директории folder1

        res = []
        res.append(checkout("cd {}; 7z a {}arx2".format(data['tst'], data['out']), "Everything is Ok"))
        res.append(checkout("cd {}; 7z e arx2.7z -o{} -y".format(data['out'], data['folder']), "Everything is Ok"))
        for item in make_files:
            res.append(checkout("ls {}".format(data['folder']), item))
        assert all(res), 'test FAIL'


    def test_step3(self):
        # проверяем целостность архива arx2.7z
        assert checkout("cd {}; 7z t arx2.7z".format(data['out']), "Everything is Ok"), 'TEST_STEP3 FAIL'


    def test_step4(self):
        # проверяем возможность обновить файлы  в архиве arx2.7z
        assert checkout("cd {}; 7z u {}/arx2.7z".format(data['tst'], data['out']), "Everything is Ok"), 'TEST_STEP4 FAIL'


    def test_step5(self, clear_folders, make_files):
        # удаляем файлы из архива arx2.7z (очищаем его)
        res = []
        res.append(checkout("cd {}; 7z a {}/arx2".format(data['tst'], data['out']), "Everything is Ok"))
        for item in make_files:
            res.append(checkout("cd {}; 7z l {}arx2".format(data['tst'], data['out']), item))
        assert all(res), 'test_step5 FAIL'


    def test_step6(self, clear_folders, make_files, make_subfolder):
        res = []
        res.append(checkout("cd {}; 7z a {}/arx2".format(data['tst'], data['out']), "Everything is Ok"))
        res.append(checkout("cd {}; 7z x arx2.7z -o{} -y".format(data['tst'], data['out']), "Everything is Ok"))

        for item in make_files:
            res.append(checkout("ls {}".format(data['folder']), item))

        res.append(checkout("ls {}".format(data['folder']), make_subfolder[0]))
        res.append(checkout("ls {}/{}".format(data['folder'], make_subfolder[0]), make_subfolder[1]))
        assert all(res), 'test_step6 FAIL'

    def test_step7(self):
        # проверяем возможность обновить файлы  в архиве arx2.7z
        assert checkout("cd {}; 7z d arx2.7z".format(data['out']), "Everything is Ok"), 'TEST_STEP7 FAIL'


    def test_step8(self, clear_folders,make_files):
        res = []
        for item in make_files:
            res.append(checkout("cd {}; 7z h {}".format(data['folder'], item), "Everything is Ok"))
            #hash = getout("cd {}; crc32 {}".format(data['folder'], item).upper()
            res.append(checkout("cd {}; 7z h {}".format(data['folder'], item), hash))
        assert all(res), 'test_step8 FAIL'









