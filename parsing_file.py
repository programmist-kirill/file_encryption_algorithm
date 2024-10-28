import os

import parsing_stroka

directory_to_file_for_encrypt = input('Введите директорию где находится файл для шифрования: ')

class File_parsing:
    def main(directory_to_file_for_encrypt):

        parsing_stroka.count_number_of_characters(directory_to_file_for_encrypt)

        with open(directory_to_file_for_encrypt, 'r') as file:
            data = file.readlines()

        index = 0
        while index != len(data):
            stroka = data[index]

            parsing_stroka.simwol_in_stroka.__init__(input_string = stroka)
            
            if index != len(data):
                index += 1
                continue
            else:
                break

class Data_verification:
    def check_directory(directory_to_file_for_encrypt):
        directory = directory_to_file_for_encrypt

        if os.path.exists(directory):
            if os.path.isfile(directory):
                print('Директория указана верно')
                File_parsing.main(directory_to_file_for_encrypt)
        else:
            a = True
            while a == True:
                directory = input('Директория не существует. Введите директорию где находится файл для шифрования: ')
                if os.path.exists(directory):
                    if os.path.isfile(directory):
                        a = False
                        print('Директория указана верно')
                        File_parsing.main(directory_to_file_for_encrypt)
                        break
                
                else:
                    a = True
                    continue
Data_verification.check_directory(directory_to_file_for_encrypt)