# Mutation Mystery
def deep_copy(lst):
    """Returns a new list that is a deep copy of lst.
    >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
    >>> y = deep_copy(x)
    >>> y[0][1] = 'z'
    >>> y
    [[0, 'z'], [1, 'b'], [2, 'c']]
    >>> x
    [[0, 'a'], [1, 'b'], [2, 'c']]
    >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
    >>> z = deep_copy(x)
    >>> z[0][1] = 'z'
    >>> z
    [[0, 'z'], [1, 'b'], [2, 'c']]
    >>> x       #x should not change
    [[0, 'a'], [1, 'b'], [2, 'c']]
    """
    return [list(l) for l in lst]

import copy
def dict_cycle(dictionary):
    """Write a function that cycles each of the key-value pair such that the key becomes the last
        item in the value list, and the first item of the list becomes the new key. 

    >>> hamster = {"a":["b","c","d"], "w":["x","y","z"]}
    >>> dict_cycle(hamster)
    >>> sorted(hamster.items()) # items return list of tuples that are key value pairs
    [('b', ['c', 'd', 'a']), ('x', ['y', 'z', 'w'])]
    """
    dic = dictionary.copy()
    for key in dic:
        new_key = dic[key][0]
        dictionary[key].pop(0)
        dictionary[key].append(key)
        dictionary[new_key] = dictionary[key]
        dictionary.pop(key)







    # new_dict ={}
    # dict_keys = dictionary.keys()
    # for i in dictionary:
    #     new_dict[dictionary[i][0]]= [dictionary[i].pop(1), dictionary[i].pop(),i ]
    # for i in new_dict:
    #     dictionary[i] = new_dict[i]
    # for i in dictionary:
    #     new_dictionary = list(dictionary.keys())
    # for i in new_dictionary:
    #     temp = dictionary.pop(i)
    #     temp.append(i)
    #     dictionary[temp.pop(0)] = temp


# dic = dictionary
# for key in dic:
# new_key = dic[key][0]
# dictionary[key].pop(0)
# dictionary[key].append(key)
# dictionary[new_key] = dic[key]

    # dic = dictionary.items()
    # for key, value in dic:
    #     new_key = value[0]
    #     value.pop(0)
    #     value.append(key)
    #     dictionary[new_key] = value
    # dictionary.pop(0)
    # dictionary.pop(0)

    


# Reverse
def todo():
    """Returns add and reverse, which add to and reverse the list
    >>> add, get_list, reverse = todo()
    >>> add("clean")
    >>> add("homework")
    >>> add("cook")
    >>> add("sleep")
    >>> get_list()
    ['clean', 'homework', 'cook', 'sleep']
    >>> reverse()
    >>> get_list()
    ['sleep', 'cook', 'homework', 'clean']
    >>> add("wake up")
    >>> get_list()
    ['sleep', 'cook', 'homework', 'clean', 'wake up']
    >>> reverse()
    >>> get_list()
    ['wake up', 'clean', 'homework', 'cook', 'sleep']
    """
    lst = []
    def get_list():
        return lst
    def add(item):
        lst.append(item)
    def reverse():
        l = lst.copy()
        for i in range(len(l)):
            lst.append(l[-i-1])
            lst.pop(0)
    return add, get_list, reverse
    


# Mailbox

def mailbox():
    """
    >>> get_mail, deliver_mail = mailbox()
    >>> get_mail("Sophia")
    >>> deliver_mail("Sophia", ["postcard"])
    >>> get_mail("Sophia")
    ['postcard']
    >>> get_mail("Sophia")
    >>> deliver_mail("Lyric", ["paycheck", "ads"])
    >>> get_mail("Lyric")
    ['paycheck', 'ads']
    >>> deliver_mail("Lyric", ["bills"])
    >>> get_mail("Lyric")
    ['bills']
    >>> deliver_mail("Julia", ["survey"])
    >>> get_mail("Julia")
    ['survey']
    >>> get_mail("Julia")
    >>> get_mail("Amir")
    >>> deliver_mail("Amir", ["postcard", "paycheck"])
    >>> deliver_mail("Amir", ["ads"])
    >>> get_mail("Amir")
    ['postcard', 'paycheck', 'ads']
    """
    mailbox = {}
    def get_mail(name):
        if name not in mailbox:
            return None
        else:
            return _get_mail(mailbox,name)        
        
    def deliver_mail(name, mail):
        return _deliver_mail(mailbox,name,mail)
        
        
    return get_mail, deliver_mail

def _deliver_mail(mailbox, name, mail):
    if name in mailbox:
        mailbox[name] += mail
    else:
        mailbox[name] = mail

def _get_mail(mailbox, name):
    user = mailbox[name]
    if user != []:
        mailbox[name] = []
        return user

# Optional

def make_gym(a, b, c, d):
    """Returns a pokemon gym (represented by list) of the four pokemons a, b, c, d."""
    return [a, b, c, d]

def gym_size(gym):
    """Returns the size of the gym."""
    return len(gym)

def make_pokemon_set():
    """Returns a dictionary of pokemon methods.

    >>> my_pokemons = make_pokemon_set()
    >>> my_pokemons["add"]("pikachu", "raichu")
    >>> my_pokemons["evolve"]("charmander")
    'charizard'
    >>> my_pokemons["evolve"]("celebi")
    'celebi'
    >>> my_gym = make_gym("charmander", "celebi", "pikachu", "rattata")
    >>> my_pokemons["evolve_all"](my_gym)
    >>> my_gym
    ['charizard', 'celebi', 'raichu', 'raticate']

    """
    pokemons = {"charmander":"charmeleon",
            "charmeleon":"charizard",
            "squirtle":"wartortle",
            "wartortle":"blastoise",
            "rattata":"raticate",
            "sandshrew":"sandslash"}

    def add(pokemon, evolution):
        _add_pokemon(pokemons, pokemon, evolution)

    def evolve(pokemon):
        return _evolve(pokemons, pokemon)

    def evolve_all(gym):
        _evolve_all(pokemons, gym)
        

    return {"add":add, "evolve":evolve, "evolve_all":evolve_all}

def _add_pokemon(pokemon_set, pokemon, evolution):
    pokemon_set[pokemon] = evolution 

def _evolve(pokemon_set, pokemon):
    while pokemon in pokemon_set:
        pokemon = pokemon_set[pokemon]
    return pokemon

def _evolve_all(pokemon_set, gym):
    team =[_evolve(pokemon_set,x) for x in gym]    
    for i in range(len(gym)):
        gym[i] = team[i]