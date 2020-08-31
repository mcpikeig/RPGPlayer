#Initialize the Player Value
class Player:
        def __init__(self,hp,armor,strength,intelligence,agility):
                self.hp=hp
                self.armor=armor
                self.strength=strength
                self.intelligence=intelligence
                self.agility=agility

#The following classes define the base stats for each of the 3 professions
class Fighter(Player):
        def __init__(self):
                super().__init__(
                        hp=30,
                        armor=3,
                        strength=8,
                        intelligence=3,
                        agility=5
                        )

class Rogue(Player):
        def __init__(self):
                super().__init__(
                        hp=20,
                        armor=2,
                        strength=5,
                        intelligence=3,
                        agility=8
                        )

class Mage(Player):
        def __init__(self):
                super().__init__(
                        hp=25,
                        armor=1,
                        strength=3,
                        intelligence=8,
                        agility=5
                        )

#Choose your Class!
def profession():
        letter_to_profession = {
                'f': Fighter,
                'r': Rogue,
                'm': Mage
                }
        print("What is your class?\n")
        for letter in letter_to_profession.keys():
                print("- Press {} for {}".format(
                        letter, letter_to_profession[letter].__name__))
        pclass = input(">>>")
        return letter_to_profession[pclass]()

#Main Game Function; Choose a profession and it shows your stats
def main():
        pProf = profession()
        print("HP: {}\nArmor: {}\nStrength: {}\nIntelligence: {}\nAgility: {}".format(
                pProf.hp,pProf.armor,pProf.strength,pProf.intelligence,pProf.agility))

main()











