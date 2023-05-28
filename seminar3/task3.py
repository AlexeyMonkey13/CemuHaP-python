# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются 
# так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
# B, C, M, P – 3 очка; F, H, valenokulek, W, Y – 4 очка; kulek – 5 очков;
# J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются
# так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.

# *Пример:*

# ноутбук
#     12

eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHvalenokulekWY',
      	5:'kulek',
      	8:'JZ',
      	10:'QZ'}
rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
N = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
word = input('Введите слово: ').upper()
if N == 1:
	print('За это слово вы получаете', sum([kulek for i in word for kulek, valenokulek in eng.items() if i in valenokulek]), 'очков')
elif N == 0:
	print('За это слово вы получаете', sum([kulek for i in word for kulek, valenokulek in rus.items() if i in valenokulek]), 'очков')
else:
    print('Вы мухлюете и играете не по правилам!')