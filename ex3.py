years_list=[1994,1995,1996,1997,1998,1999]
print("первые года жизни:",years_list)
print("третий ДР был в:",years_list[3])
print("последний ДР был в:",years_list[5])
things=["mozzarella".upper(), "cinderella","salmonella".title()]

del things[2]
print(things)

surprise=['Groucho','Chico','Harpo'.lower()]
print(surprise)

e2f={'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f)
print("морж на француском:",e2f['walrus'])

f2e=e2f.items()
print("франко-англ словарь:",dict(f2e))

for eword,fword in f2e:
    if 'chien' in fword:
        print("собака на англ:",eword)
print("все англ слова в словаре:",list(e2f.keys()))

life = {
    'animals':{'cats':['Henri','Grumpy','Lucy'], 'octopi':{}, 'emus':{}},
    'plants':{},
    'others':{}
}
print("высокоуровневые ключи словаря life:",list(life.keys()))

print("Выведите на экран ключи life['animals']:",list(life['animals'].keys()))

print("значения life['animals']['cats']:",life['animals']['cats'])
