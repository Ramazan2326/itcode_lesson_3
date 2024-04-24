"""
Суть работы программы - использование основного цикла while True, в котором
вызывается функция - основная логика программы. Я решил создать что-то типо
примитивного пользовательского меню. Main_logic - сравниваем текущее слово
имеет ли длину максимального слова в списке? Если да - тогда запоминаем индекс
нового максимума, и добавляем в список индексов максимумов (на случай если
среди введенных пользователем слов будет несколько слов с одинаковой
максимальной длиной)
"""


def output_info() -> str:
    return f"Самое длинное " \
           f"слово(-а): {' '.join([dict['source_list'][i] for i in dict['max_list_of_idx']])}"


def main_logic():
    if dict['lens_of_words_list'][i] == maximum_len:
        dict['idx_of_max'] = i
        dict['max_list_of_idx'].append(dict['idx_of_max'])


while True:
    dict = {
        'source_list': str(input('Введите слова через пробел: ')).split(' '),
        'lens_of_words_list': [],
        'max_list_of_idx': [],
        'idx_of_max': 0
    }
    dict['lens_of_words_list'] = [len(i) for i in dict['source_list']]
    maximum_len = max(dict['lens_of_words_list'])
    answer = str(
        input('\nВведите 1, если хотите решить задачу первым способом, \n'
              'Введите 2, если хотите решить задачу вторым способом: '))
    if answer == '1':
        print('\nРешение через цикл "for"')
        for i in range(len(dict['lens_of_words_list'])):
            main_logic()

        print(output_info())

    elif answer == '2':
        print('\nРешение через цикл "while"')
        i = 0
        while True:
            main_logic()
            i += 1
            if i == len(dict['lens_of_words_list']):
                break
        print(output_info())

    elif answer != '1' and answer != '2':
        print('Нет такого способа решения')

    if str(input('Если хотите продолжить, пропишите пробел'
                 ' пробел, если нет, пишете что угодно: ')) == ' ':
        print('\n')
        continue
    elif str(input('Вы точно хотите завершить работу? '
                   'Напишите "yes": ')) == 'yes':
        break
