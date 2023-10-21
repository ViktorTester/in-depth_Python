"""There is 'names' list containing names in English.
The program displays all names that begin with the letters
A and M (regardless of case) and have a length greater than 4.
The names are arranged in lexicographical order
 separated by spaces, each with a capital letter."""

names = ['Ulyana', 'Arina', 'Dmitry', 'Sergey', 'Yana', 'Mila', 'Olga', 'Sofia', 'Semyon', 'Nikita', 'Margarita',
         'Vasilisa', 'Kirill', 'Alexander', 'Alexandra', 'Ivan', 'Andrei', 'Rodion', 'Maxim', 'Alisa', 'Artyom',
         'Sofia', 'Vladimir', 'Damir', 'Valery', 'Stepan', 'Alexey', 'Mark', 'Oleg', 'Irina', 'Milana', 'Miya',
         'denis', 'Fyodor', 'Elizaveta', 'Aileen', 'Varvara', 'Valeria', 'Alyona', 'Nikol', 'Yulia', 'Ksenia', 'Peter',
         'George', 'Maria', 'Gleb', 'Ilya', 'Zakhar', 'Daria', 'Evgenia', 'Matvey', 'Seraphim', 'Ekaterina', 'Timofey',
         'Victor', 'Egor', 'Nika', 'Anna', 'Daniel', 'Tikhon', 'Vera', 'Kira', 'Emilia', 'Victoria', 'Igor', 'Polina',
         'Alina', 'David', 'Anastasia', 'Veronika', 'Yaroslav', 'Ruslan', 'Tatiana', 'Demid', 'Amelia', 'Elina',
         'Arsen', 'Eugene', 'Madina', 'Darina', 'Savelius', 'Plato', 'Adelina', 'Diana', 'Aisha', 'Pavel', 'Stephania',
         'Timur', 'Eva', 'Elisey', 'Artemiy', 'Grigory', 'Miron', 'Miroslava', 'Mira', 'Marat', 'Lilia', 'Roman',
         'Vladislav', 'Leonid']

filter1 = filter(lambda x: x.lower().startswith('а') or x.lower().startswith('м'), names)

filter2 = filter(lambda y: len(y) > 4, filter1)

map1 = sorted(map(lambda z: z.title(), filter2))

print(*map1)
