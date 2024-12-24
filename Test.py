result = 0
print('Кто ты из "красная шапочка" пиши число')
print('====================')
print('Ты помогаешь бабушке?')
print('1. да 2.нет')
anwser1 = input()
print('Ты помогаешь людям?')
print('1. да 2.нет')
anwser2 = input()
print('Ты ешь бабушек?')
print('1. да 2.нет')
anwser3 = input()

if anwser1 == "1":
    result += 1
if anwser2 == "1":
    result += 1
if anwser3 == "2":
    result += 1

if result <= 1:
    print("Ты волк!")
if result == 2:
    print("Ты волк и красная шапочка одновремено!")
if result == 3:
    print("Ты красная шапочка!")