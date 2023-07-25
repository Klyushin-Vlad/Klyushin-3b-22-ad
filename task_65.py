class Character():
    def __init__(self, name, lvl, maxHP, ATK, DEF):
        self.name = name
        self.lvl = lvl
        self.maxHP = maxHP
        self.HP = maxHP
        self.ATK = ATK
        self.DEF = DEF
        self.enemy = 0

    def get_dmg(self, dmg):
        r = dmg - self.DEF
        if r>=0:
            self.HP-=r
        else:
            self.HP-=1
        print(self.name, self.HP)
        if self.HP > 0:
            self.enemy.get_dmg(self.ATK)
        else:
            print("Победил:", self.enemy.get_name())

    def get_name(self):
        return self.name

    def set_enemy(self, enemy):
        self.enemy = enemy

    def lvl_up(self):
        self.lvl += 1
        self.HP *= 1.1
        self.ATK *= 1.1

    def Battle(self):
        self.HP = self.maxHP
        self.enemy.HP = self.enemy.maxHP
        self.enemy.get_dmg(self.ATK)


first = Character("1",2,40,5,2)
second = Character("2",4,50,5,8)
first.set_enemy(second)
second.set_enemy(first)
win1 = 0
win2 = 0
for i in range(0,3):
    first.Battle()
    if first.HP<=0:
        win2+=1
    else:
        win1+=1
if win1>win2:
    print(first.name, "сильнее ", second.name)
else:
    print(second.name, "сильнее ", first.name)