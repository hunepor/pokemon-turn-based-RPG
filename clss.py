from random import choice

class Pokemon():

    def __init__(self, name:str="Undefined"):
        self.max_health = 100
        self.heal_range = [25, 32]
        self.name = name

        self.health = self.max_health
        self.low_range_damage_range = [25, 30]
        self.high_range_damage_range = [22, 35]
    
    
    def get_damage(self, DMG):
        """
        Provides getting damage by Pokemon
        """
        print(f"{self.name} got {DMG} damage!")
        self.health -= DMG
        self.check_health()

    def deal_damage(self, hit):
        """
        Return amount of damage in dependance of *kwarg to deal to opponent
        hit = "hit" or "bam"
        """
        
        if hit == "hit":
            dmg = self.low_range_damage_range
        
        if hit == "bam":
            dmg = self.high_range_damage_range        
        
        dealed = choice(range(dmg[0], dmg[1]))

        print(f"\n{self.name} {hit.upper()}ed {dealed} DMG")
        
        return dealed

    def heal(self): 
        """
        Provides restoring health with ability
        """
        regen = choice(range(self.heal_range[0], self.heal_range[1]+1))
        self.health += regen

        print(f"{self.name} restored {regen} HP!")
        self.check_health()
        
    def check_health(self):
        """
        Checks current HP:
            0 < health <= self.max_health
            if 0 => dead
        """
        if self.health > self.max_health:
            self.health = self.max_health
            print(f"{self.name} now has maximum HP!")
        elif self.health <= 0:
            self.health = 0