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
        self.HP -= abs(dmg - self.DEF) + 1
        if self.HP>0:
            self.enemy.battle()
        else:
            print("Победил:", self.enemy.get_name())

    def get_name(self):
        return self.name


    def set_enemy(self, enemy):
        self.enemy = enemy

    def lvl_up(self):
        self.lvl+=1
        self.HP*=1.1
        self.ATK*=1.1

    def Battle(self):
        if self.HP>0:
            self.enemy.get_dmg(self.ATK)
