class item:
    name = ''
    position = 'start'

    def __init__(self, name):
        self.name = name


class game:
    wolf = item('wolf')
    goat = item('goat')
    cabbage = item('cabbage')
    position = 'start'

    def print_condition(self):
        print(f'Коза находится на {self.goat.position}\n'
              f'Волк находится на {self.wolf.position}\n'
              f'Капуста находится на {self.cabbage.position}\n'
              f'Крестьянин находится на {self.position}')

    def is_boat_empty(self):
        return self.wolf.position != 'boat' and self.goat.position != 'boat' and self.cabbage.position != 'boat'

    def add_to_boat(self, added_item):
        if self.is_boat_empty():
            if added_item.position == self.position:
                added_item.position = 'boat'
            else:
                print('Лодка и предмет находятся на разных берегах')
        else:
            print('Лодка уже занята!')

    def remove_from_boat(self, removed_item, place):
        if removed_item.position == 'boat':
            removed_item.position = place
        else:
            print('Предмет находится не в лодке!')

    def is_failed(self):
        return self.wolf.position == self.goat.position and self.position != self.goat.position \
               or self.goat.position == self.cabbage.position and self.position != self.goat.position

    def is_win(self):
        return self.wolf.position == 'end' and self.goat.position == 'end' and self.cabbage.position == 'end'

    def change_position(self):
        if self.position == 'start':
            self.position = 'end'
        else:
            self.position = 'start'
        if self.is_failed():
            print('Вы оставили на берегу два несовместных объекта.')


print('Игра "Волк, коза и капуста".')
my_game = game()
while not my_game.is_win() and not my_game.is_failed():
    my_game.print_condition()
    while True:
        item1 = input(
            'Введите предмет, который вы хотите положить/достать из лодки. (W, G, C) или S чтобы переправить лодку на '
            'другой берег.')
        if item1 == 'W' or item1 == 'G' or item1 == 'C' or item1 == 'S':
            break
        else:
            print('Ошибка! Введите корректный символ.')
    if item1 == 'W':
        if my_game.wolf.position == 'start' or  my_game.wolf.position =='end':
            my_game.add_to_boat(my_game.wolf)
        else:
            my_game.remove_from_boat(my_game.wolf, my_game.position)
    elif item1 == 'G':
        if my_game.goat.position == 'start' or my_game.goat.position =='end':
            my_game.add_to_boat(my_game.goat)
        else:
            my_game.remove_from_boat(my_game.goat, my_game.position)
    elif item1 == 'C':
        if my_game.cabbage.position == 'start' or my_game.cabbage.position =='end':
            my_game.add_to_boat(my_game.cabbage)
        else:
            my_game.remove_from_boat(my_game.cabbage, my_game.position)
    else:
        my_game.change_position()
if my_game.is_win():
    print("Поздравляем! Вы справились с данной головоломкой")
else:
    print("К сожалению, вы не справились с задачей!")