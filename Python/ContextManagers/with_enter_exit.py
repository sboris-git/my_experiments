from contextlib import contextmanager
# Corey Schafer at youtube tutorial: Context Managers

class OpenFile():

    def __init__(self, filename, mode):
        print('init method called')
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('enter method called')
        try:
            self.fileHandler = open(self.filename, self.mode)
        finally:
            return self.fileHandler

    def __exit__(self, exc_type, exc_val, exc_tb):
        # [the parameters in this method are used to manage exceptions]
        print('exit method called')
        self.fileHandler.close()


# with OpenFile('test.txt', 'w') as file:
#     print('with statement block')
#     file.write('Testing context mamager behaviour')

with OpenFile('test.txt', 'r') as file:
    print(file.read())

print(file.close())

# use contextmanager lib
print('Context mamager usage example')
@contextmanager
def openFile(file, mode):
    f = open(file, mode)
    yield f

# f.closed()

with openFile('test.txt', 'r') as f:
    print(f.read())

print(f.closed())

