grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Stele', 'Khendrik', 'Aaron'}
average_rating = {}
list_stud = sorted(list(students)) # сортируем студентов в алфавитном порядке
ave_rate0 = sum(grades[0]) / grades[0].__len__() # средний бал студента
ave_rate1 = sum(grades[1]) / grades[1].__len__() # средний бал студента
ave_rate2 = sum(grades[2]) / grades[2].__len__() # средний бал студента
ave_rate3 = sum(grades[3]) / grades[3].__len__() # средний бал студента
ave_rate4 = sum(grades[4]) / grades[4].__len__() # средний бал студента
average_rating.update({list_stud[0]: ave_rate0, list_stud[1]: ave_rate1,
                       list_stud[2]: ave_rate2, list_stud[3]: ave_rate3,
                       list_stud[4]: ave_rate4}) #составление словаря
print(average_rating)