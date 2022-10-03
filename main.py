def encodeLZ(FileIn, FileOut):#сжатие
    input_file = open(FileIn, 'r') #открываем файл который нужно сжать
    encoded_file = open(FileOut, 'w') #в этот файл будет записываться сжатая информация
    text_from_file = input_file.read() #метод считывания всей информации из файла
    dict_of_codes = {text_from_file[0]: '1'} #присваевыем ключ 1ого символа значение 1
    encoded_file.write('0' + text_from_file[0])#записываем в файл код первой комбинации (она всегда будет 0)
    text_from_file = text_from_file[1:]#идем дальше по строке начиная со 2 символа
    combination = ''#переменная в которую будут записываться комбинации
    code = 2#нумерается кодов
    for char in text_from_file:#бежим по строке посимвольно
        combination += char#увеличиваем каждый раз комбинацию пока ее не будет в словаре
        if combination not in dict_of_codes:#проверяем есть ли комбинация в словаря
            dict_of_codes[combination] = str(code)#записываем в словарь комбинацию и ее номер
            if len(combination) == 1:#проверяем если комбинации состоит из 1 символа
                encoded_file.write('0' + combination)#записываем в файл 0 и символ
            else:#если комбинация больше чем 1 символ
                encoded_file.write(dict_of_codes[combination[0:-1]] + combination[-1])#записываем в файл номер комбинации и последний символ в ней
            code += 1#увеличиваем номер кода
            combination = ''#обнуляем комбинацию чтобы записать новую
    input_file.close()#закрываем файл считывания
    encoded_file.close()#закрываем файл записи
    return True


def decodeLZ(FileIn, FileOut):#декодирование
    coded_file = open(FileIn, 'r')#тоже что и выше
    decoded_file = open(FileOut, 'w')#тоже что и выше
    text_from_file = coded_file.read()#тоже что и выше
    dict_of_codes = {'0': '', '1': text_from_file[1]}#присваевыем ключу 0 значение пустоты (далее будем прис)
    decoded_file.write(dict_of_codes['1'])#записываем в файл первую комбинацию
    text_from_file = text_from_file[2:]#идем по строчке со 2 символа
    combination = ''#тоже шо выше
    code = 2#тоже шо выше
    for char in text_from_file:#цикл в котором бежим посимвольно по строчке
        if char in '1234567890':#проверяем является ли символ цифрой
            combination += char#увеличиваем комбинацию из цифр (потому что они могут быть многозначными)
        else:#если символ это буква
            dict_of_codes[str(code)] = dict_of_codes[combination] + char#записываем в словарь номер комбинации
            decoded_file.write(dict_of_codes[combination] + char)#записываем в файл комбинацию символов с полученым номером
            combination = ''#обнуляем комбинацию
            code += 1#увеличиваем номер комбинации
    coded_file.close()#тоже что и выше
    decoded_file.close()#тоже что и выше



q = "q"
while q == "q":#запускаем бесконечный цикл чтобы программа работала пока мы сами ее не остановим
    print("1 - сжать файл\n2 - декодировать файл ")#выбираем действие нужное нам
    v = int(input())#вводим нужное нам действие
    if (v == 1):#исполнение сжатия
        encodeLZ('input.txt', 'encoded.txt')
    else:#исполнение декода
        decodeLZ('encoded.txt', 'decoded.txt')