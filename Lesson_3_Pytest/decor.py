import time

def retry(func):
    def wrapper():
        try:
            func()
        except:
            print('retry....')
            time.sleep(1)
            func()
    return wrapper()

@retry
def might_fail():
    print('might_fail')
    raise Exception

might_fail()
