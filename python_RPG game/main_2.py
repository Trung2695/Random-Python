import math
import random

state = 0


class Enemy:
    def __init__(self, level):
        self.health = 15 + level * 30
        self.defense = int(level * (level + 1) / 2) + math.floor(level * (2.5 + random.uniform(-1, 1)))
        self.attack = int(level * (level + 1) / 2) + math.floor(level * (2.5 + random.uniform(-1, 1)))
        self.speed = int(level * (level + 1) / 2) + math.floor(level * (2.5 + random.uniform(-1, 1)))

    def attack_function(self, enemy):
        return max(self.attack - math.floor(enemy.defense) / 2, 1)


class PC:
    def __init__(self):
        self.total_health = 20
        self.health = 20
        self.defense = 1
        self.attack = 1
        self.speed = 1
        self.exp = 1
        self.level = 1

    def start_up(self):
        total = 4
        while total > 0:
            print("You have " + str(total) + " stat point(s) left. Where do you want to allocate it?")
            stat_choice = input("[A]ttack / [S]peed / [D]efence")
            while stat_choice not in ['a', 'A', 'S', 's', 'd', 'D']:
                stat_choice = input("Not valid input. [A]ttack / [S]peed / [D]efence")
            if stat_choice in ['a', 'A']:
                self.attack += 1
                total -= 1
            elif stat_choice in ['d', 'D']:
                self.defense += 1
                total -= 1
            elif stat_choice in ['S', 's']:
                self.speed += 1
                total -= 1

    def level_up(self):
        print("John has levelled up!")
        self.total_health += 20 * (self.level + 1)
        self.level += 1
        self.defense += math.ceil(1.5 * ((self.level + 1) / 2))
        self.attack += math.ceil(1.5 * ((self.level + 1) / 2))
        self.speed += math.ceil(2 * ((self.level + 1) / 2))
        self.health = self.total_health
        self.exp = 0

    def attack_function(self, enemy):
        return max(math.floor(self.attack - enemy.defense / 2), 1)

    def exp_gain(self, number):
        self.exp += number
        if self.exp >= 1000:
            self.level_up()

    def heal(self):
        return min(int(1 / 4 * self.total_health), self.total_health - self.health)


John = PC()


class Combat:
    def __init__(self):
        self.end_flag = 0
        self.antag = Enemy(John.level - 1)

        def combat_round():
            global state
            if self.end_flag == 0:
                if John.speed >= self.antag.speed:
                    action = input("[A]ttack or [H]eal")
                    while action not in ['a', 'A', 'h', 'H']:
                        action = input("Input not valid. [A]ttack or [H]eal")
                    if action in ['a', 'A']:
                        damage = John.attack_function(self.antag)
                        print("Kapow! John did " + str(damage) + " point(s) of damage!")
                        self.antag.health -= damage
                        if John.health < 0:
                            print("Loser :(")
                            state = - 1
                            self.end_flag = 1
                        elif self.antag.health < 0:
                            print("Winner :)")
                            John.exp += 100
                            if John.exp > 100:
                                John.level_up()
                            self.end_flag = 1
                    elif action in ['h', 'H']:
                        John.health += John.heal()
                        print("John has restored his health to: " + str(John.health) + "/" + str(John.total_health))
                    enemy_damage = self.antag.attack_function(John)
                    print("Kapow! Enemy did " + str(enemy_damage) + " point(s) of damage! John has " + str(
                        John.health) + "health left.")
                    John.health -= enemy_damage
                    if John.health < 0:
                        print("Loser :(")
                        state = - 1
                        self.end_flag = 1
                    elif self.antag.health < 0:
                        print("Winner :)")
                        John.exp += 100
                        if John.exp > 100:
                            John.level_up()
                        self.end_flag = 1
                else:
                    enemy_damage = self.antag.attack_function(John)
                    print("Kapow! Enemy did " + str(enemy_damage) + " point(s) of damage! John has " + str(
                        John.health) + "health left.")
                    John.health -= enemy_damage
                    if John.health < 0:
                        print("Loser :(")
                        state = - 1
                        self.end_flag = 1
                    elif self.antag.health < 0:
                        print("Winner :)")
                        John.exp += 100
                        if John.exp > 100:
                            John.level_up()
                        self.end_flag = 1
                    action = input("[A]ttack or [H]eal")
                    while action not in ['a', 'A', 'h', 'H']:
                        action = input("Input not valid. [A]ttack or [H]eal")
                    if action in ['a', 'A']:
                        damage = John.attack_function(self.antag)
                        print("Kapow! John did " + str(damage) + " point(s) of damage!")
                        self.antag.health -= damage
                        if John.health < 0:
                            print("Loser :(")
                            self.end_flag = 1
                            state = - 1
                        elif self.antag.health < 0:
                            print("Winner :)")
                            John.exp += 100
                            if John.exp > 100:
                                John.level_up()
                            self.end_flag = 1
                    elif action in ['h', 'H']:
                        John.health += John.heal()
                        print("John has restored his health to: " + str(John.health) + "/" + str(John.total_health))

        while self.end_flag == 0:
            combat_round()


if __name__ == '__main__':
    """John = PC()
    Steve = Enemy(0)
    John.attack_function(Steve)
    while Steve.health > 0:
        Steve.health -= John.attack_function(Steve)
        print(Steve.health)"""
    John.start_up()
    while not state:
        menu_option = input("Welcome to the Arena. Would you like to [F]ight or [R]est?")
        while menu_option not in ['f', 'F', 'R', 'r']:
            menu_option = input("Not valid input. Would you like to [F]ight or [R]est?")
        if menu_option in ['f', 'F']:
            Combat()
        elif menu_option in ['R', 'r']:
            print('John feels well-rested, and has recovered his health.')
            John.health = John.total_health
    if state == -1:
        print("Game over :(")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
