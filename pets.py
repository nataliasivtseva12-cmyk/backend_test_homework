animals = ['Барсик', 'Мурка', 'Боня', 'Рекс', 'Белка', 'Шарик', 'Бим']
long_names=[]

for animal in animals:
    if len(animal) > 4 and animal[0] == 'Б':
        long_names.append(animal)
        print(f'{animal} — длинное имя на букву Б')
    elif len(animal) > 4 :
        long_names.append(animal)
        print(f'{animal} — длинное имя ')
    

print (long_names)
print(f'кол-животных в списке:{len(long_names)}')