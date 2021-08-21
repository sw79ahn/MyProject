# def hap(x,y):
#     return x+y


# print(hap(10,20))

# from functools import reduce
# print(reduce(lambda x,y : x+y, 'abcde')
# 
# c=10
# d=20
# c,d = d,c
# print(c,d)
class babarian:
    strength = 500
    dex =10
    vital = 8000
    energy = 15

    def attack(self):
        return 'Bang!!'

class person:
    eyes = 2
    nose = 1
    mouse =1

    def eat(self):
        print 'yami yami\n'

    def sleep(self)    :
        print'꿀꿀'

    def talk(self)    :
        print'wal wal wal'

class student(person) :
    def study(self):
        print 'Study Hard!!!'
