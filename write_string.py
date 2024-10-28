import os

def write(a0):

    with open('index','r') as file:
        index = file.read()

    if not os.path.exists('cashe/file' + index):
        with open('cashe/file' + index,'w') as fp:
            fp.write(a0)
        

    else:

        with open('cashe/file' + index,'w') as fp:
            fp.write(a0)