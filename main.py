import random
import requests

pokemon_choices = []
my_pokemon = []


def get_pokemon(item):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(item)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon["name"],
        'id': pokemon["id"],
        'height': pokemon["height"],
        'weight': pokemon["weight"],
        }


def three_pokemon():
    for number in range(3):
        pokemon_number = random.randint(1, 151)
        pokemon = get_pokemon(pokemon_number)
        pokemon_choices.append(pokemon['name'])

    return pokemon_choices


def choose_your_pokemon():
    three_pokemon()
    print("Choose a pokemon from the list!")
    print(f"1: {format(pokemon_choices[0]).capitalize()}"
          f"\n2: {format(pokemon_choices[1]).capitalize()}"
          f"\n3: {format(pokemon_choices[2]).capitalize()}")
    my_pokemon_index = input("Write the number of your choice here: ")
    if my_pokemon_index == "1":
        my_pokemon.append(pokemon_choices[0])
        return my_pokemon
    elif my_pokemon_index == "2":
        my_pokemon.append(pokemon_choices[1])
        return my_pokemon
    elif my_pokemon_index == "3":
        my_pokemon.append(pokemon_choices[2])
        return my_pokemon
    else:
        print("You did not state a valid choice, please read again carefully")
        choose_your_pokemon()


def run():
    choose_your_pokemon()
    my_pokemon_formatted = f'{my_pokemon}'
    my_pokemon_formatted = my_pokemon_formatted.replace("[","")
    my_pokemon_formatted = my_pokemon_formatted.replace("]", "")
    my_pokemon_formatted = my_pokemon_formatted.replace("'", "")

    print('You chose the pokemon {}'.format(my_pokemon_formatted).capitalize())
    stat_choice = input('Which stat do you want to use? (id, height, weight): ')
    pokemon_number = random.randint(1, 151)
    opponent_pokemon = get_pokemon(pokemon_number)
    print('The opponent chose {}'.format(opponent_pokemon['name']))
    my_chosen_pokemon = get_pokemon(my_pokemon_formatted)
    my_stat = my_chosen_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    if my_stat > opponent_stat:
        print('You Win! :)')
    elif my_stat < opponent_stat:
        print('You Lose! :(')
    else:
        print('It\'s A Draw!')


run()
