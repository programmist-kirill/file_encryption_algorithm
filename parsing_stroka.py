import os

import check_eng
import check_simwol
import check_rus

class simwol_in_stroka:

    def __init__(input_string):
        if os.path.exists('cashe/file'):
            
            if os.path.exists('index'):
                with open('index','r') as file:
                    index = file.read()
                
                index = int(index)

                index =+ 1

            else:
                with open('index','w') as fp:
                    fp.write('0')
                
                index = 0

            index = str(index)
        else:
            print('')
        
        simwol_in_stroka.extract_characters(input_string)

    def extract_characters(input_string):
        for char in input_string:
            characters = char
            check_eng.check_english(characters)
            check_simwol.main.check_simwol(characters)
            check_rus.check_russian(characters)

def count_number_of_characters(directory_to_files):
    total_count = 0

    with open(directory_to_files, 'r') as file:
        data = file.readlines()

        count_simwol_in_stroka = len(data)
        total_count += count_simwol_in_stroka

    with open('count_characters','w') as fp:
        fp.write(str(total_count))