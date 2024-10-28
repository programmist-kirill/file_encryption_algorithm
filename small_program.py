import check_eng
import check_simwol
import check_rus

directory_to_file_for_encrypt = input('Введите директорию где находится файл для шифрания: ')

with open(directory_to_file_for_encrypt,'r') as file:
  data = file.readlines()

index = 0
while len(data) != index:
    stroka = data[index]
    print(f"index = {index}")
    
    index = str(index)

    with open('index','w') as fp:
       fp.write(index)

    index = int(index)

    #parsing_stroka
    for characters in stroka:
        check_eng.check_english(characters)
        check_simwol.main.check_simwol(characters)
        check_rus.check_russian(characters)

    if len(data) != index:
       index += 1
       continue
    else:
       break