import requests
import json
import random
import time  # For quick pauses

# --- STARTER CODE (DO NOT CHANGE) ---
# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))
# --- END OF STARTER CODE ---


# Game start
# Function to get more detailed Pokémon data for the game
def get_game_pokemon_data(pokemon_name):
    """Gets detailed Pokémon data for battle."""
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        data = json.loads(response.text)
        # Extract name, HP, Attack, Defense, Speed
        stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}
        return {
            'name': data['name'].capitalize(),
            'current_hp': stats.get('hp', 50),  # Default HP if missing
            'attack': stats.get('attack', 50),  # Default Attack
            'defense': stats.get('defense', 50),  # Default Defense
            'speed': stats.get('speed', 50)  # Default Speed
        }
    except requests.exceptions.RequestException as e:
        print(f"Error getting data for {pokemon_name}: {e}")
        return None


# Function to simulate an attack
def calculate_damage(attacker, defender):
    """Calculates basic damage."""
    damage = max(1, attacker['attack'] - defender['defense'] // 2)  # Simple formula
    return damage

#Rubaet
# Main game function
def play_game():
    """Runs the simple Pokémon battle."""
    print("\n--- Starting the Battle! ---")

    # Get a list of all Pokémon names for selection
    all_pokemon_names = [p['name'] for p in
                         requests.get('https://pokeapi.co/api/v2/pokemon/?limit=1000').json()['results']]

    # Player's Pokémon (using the 'choice' from starter code, or let them pick again)
    print("\n--- Your Pokémon ---")
    player_pokemon_name = input("Enter your chosen Pokémon name (or type 'random'): ").strip().lower()
    if player_pokemon_name == 'random':
        player_pokemon_name = random.choice(all_pokemon_names)
        print(f"You got: {player_pokemon_name.capitalize()}!")

    player_pokemon = get_game_pokemon_data(player_pokemon_name)
    if not player_pokemon:
        print("Couldn't load your Pokémon. Exiting.")
        return

#Abubaker
    # CPU's Pokémon random selection
    print("\n--- CPU's Pokémon ---")
    cpu_pokemon_name = random.choice(all_pokemon_names)
    cpu_pokemon = get_game_pokemon_data(cpu_pokemon_name)

#print cpu stats
    print(f"\n{player_pokemon['name']} HP: {player_pokemon['current_hp']}")
    print(f"{cpu_pokemon['name']} HP: {cpu_pokemon['current_hp']}")
    time.sleep(1)

# Determine who goes first based on hp
    if player_pokemon['speed'] >= cpu_pokemon['speed']:
        attacker = player_pokemon
        defender = cpu_pokemon
        print(f"\n{player_pokemon['name']} is faster!")
    else:
        attacker = cpu_pokemon
        defender = player_pokemon
        print(f"\n{cpu_pokemon['name']} is faster!")

    # Simple battle loop conditon must always be above 0
    while player_pokemon['current_hp'] > 0 and cpu_pokemon['current_hp'] > 0:
        print(f"\n--- Turn ---")

    # Takes into account attacker and defender to find out how much damage is sustained.
        damage = calculate_damage(attacker, defender)
        #ensures 0 is always miniumum
        defender['current_hp'] = max(0, defender['current_hp'] - damage)
        #Which pokemon attacked who and how damage was sustained.
        print(f"{attacker['name']} attacks {defender['name']} for {damage} damage!")
        #Shows defenders damage after sustained damage
        print(f"{defender['name']} HP: {defender['current_hp']}")
        time.sleep(1)

        # Check if defender fainted
        if defender['current_hp'] <= 0:
            print(f"\n{defender['name']} fainted!")
            print(f"The winner is {attacker['name']}!")
            break

        # Role Swapper, when one faints, positons are swapped
        attacker, defender = defender, attacker
        time.sleep(0.5)

    print("Battle End")


# Run the game
if __name__ == '__main__':
    play_game()