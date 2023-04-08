#importing requests and working on the script to 
import requests

url_of_poke = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    poke_info = get_pokemon_info("Rockruff")
    poke_info = get_pokemon_info(123)
        
    return

def get_pokemon_info(pokemon_name):

    pokemon_name = str(pokemon_name).strip().lower()

    url = url_of_poke + pokemon_name

    print ('\n',f'Searching for the Pokemon Ability with the name  {pokemon_name}..', '\n', end='')
    resp_msg = requests.get(url)

    if resp_msg.status_code == requests.codes.ok:
        print('\n','Congratulations, the data has been fetched successfully', '\n')
        return resp_msg.json()
    else:
        print('\n','Failure, No such data is available','\n')
        print('\n',f'Error Code : {resp_msg.status_code}, Reason For Error : {resp_msg.reason}', '\n')

   
if __name__ == '__main__':
    main()
        