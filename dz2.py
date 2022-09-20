letters = 'Who keeps company with the wolf, will learn to howl.'
template = 'w'
exclude = 'l'

print(letters.count(template))
print(letters.count('W'))

a = []
for i in letters:
    if i != exclude :
        a.append(i)
print (a)

b = letters.split(exclude)
print(''.join(b))

#Посчитать количество символов равных значению переменной template
#Вывести все символы, не равные значению exclude