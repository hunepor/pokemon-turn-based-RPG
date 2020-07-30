from clss import *
from random import choices, choice
import time

class Game():
    """Class for initiating game and describing its methods
    """
    def start(self):
        """Prints starting message
        Initiates player and pc class with pokemon name as arg"""
        print("\nChoose your pokemon: ")
        name = input()
        self.player = Pokemon(name)

        opponent_names = ["Firepuh", "Jigledin", "Oleg", "Lori"]
        self.comp = Pokemon(choice(opponent_names))

        self.players = []
        self.players.append(self.comp)
        self.players.append(self.player)

    def player_turn(self):
        "Player choose action"
        print("what r u gonna do?")
        turn = input()

        options = ['hit', 'heal', 'bam', 'exit']

        if turn not in options:
            print("You have abilities to \"heal\", \"hit\" and \"bam\"")
            return self.player_turn()
        elif turn == "heal":
            self.player.heal()
        elif turn == "exit":
            self.end()
        else:
            damage = self.player.deal_damage(turn)
            self.comp.get_damage(damage)

    
    def comp_turn(self):
        "PC makes action"
        default_weight = 1 
        heal_weight = default_weight
        
        if 0 < self.comp.health < 35:
            heal_weight = 3
            
        turn = choices(["heal", "hit", "bam"], weights = [heal_weight, 1, 1], k=1)
        
        if turn[0] == "heal":
            self.comp.heal()
        else:
            damage = self.comp.deal_damage(turn[0])
            self.player.get_damage(damage)
     
    def status(self):
        """Prints current amount of HP for all players
        """
        def show_HP():
            print(f"\n{self.player.name}\'s HP: {self.player.health}")
            print(int(self.player.health)*'\u25Fb')
            print(f"{self.comp.name}\'s HP: {self.comp.health}")
            print(int(self.comp.health)*'\u25Fb',"\n")
        
        for p in self.players:
            if p.health == 0:
                print(f"{p.name} is dead now =(",'\u26b0')
                self.end()
        show_HP()

    def end(self):
        """Announces the end of the game and closes process"""
        print("Game over")
        exit()


def main():
    game = Game()
    game.start()
    game.status()
    s = time.sleep(0.8) # thinking imitation
    
    turn_num = 1 # turn counter
    while game.player.health or game.comp.health:
        print(f"Turn #{turn_num}")
        game.player_turn()
        
        game.status()
        s
        game.comp_turn()
        s
        game.status()
        turn_num+=1


if __name__ == "__main__":
    main()