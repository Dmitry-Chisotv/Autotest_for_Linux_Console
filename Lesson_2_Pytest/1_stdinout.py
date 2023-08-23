# import subprocess
#
# result = subprocess.run(['ping', '-c', '3', '-n', 'yandex.ru'], encoding='utf-8', stdout=subprocess.DEVNULL)
# # result = subprocess.run(['ping', '-c', '3', '-n', 'yandex.ru'], encoding='utf-8', stdout=subprocess.PIPE)
# # result = subprocess.run(['ping', '-c', '3', '-n', 'ndex.ru'], encoding='utf-8', stderr=subprocess.STDOUT)
# print(result.stdout)

# import subprocess
# def checkout(cdm, text):
#     result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
#     if text in result.stdout and result.returncode == 0:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     assert checkout("cd/home/......"), print('TEST1 FAIL')
#     # if checkout("cd/home/......"):
#     #     print('TEST1 SUCCESS')
#     # else:
#     #     print('TEST1 FAIL')
#
#     assert checkout("cd/home1/......"), print('TEST2 FAIL')
#     # if checkout("cd/home1/......"):
#     #     print('TEST2 SUCCESS')
#     # else:
#     #     print('TEST2 FAIL')
#
#     assert checkout("cd/1home/......"), print('TEST3 FAIL')
#     # if checkout("cd/1home1/......"):
#     #     print('TEST3 SUCCESS')
#     # else:
#     #     print('TEST3 FAIL')












