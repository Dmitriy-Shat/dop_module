student = {'Max': [5,4,3,2,4], 'Katja': [3,4,2,4,5], 'Petr': [3,4,5,5,4]}
name = (input('Введите имя: '))
line_length = student.get(name).__len__()
average_score = sum((student.get(name)[0::1])) / line_length
name2 = (input('Введите имя: '))
line_length = student.get(name2).__len__()
average_score2 = sum((student.get(name2)[0::1])) / line_length
name3 = (input('Введите имя: '))
line_length = student.get(name3).__len__()
average_score3 = sum((student.get(name3)[0::1])) / line_length
print(f'Средний бал студентов: ', name + ':', average_score, name2 + ':', average_score2,
      name3 + ':', average_score3)
