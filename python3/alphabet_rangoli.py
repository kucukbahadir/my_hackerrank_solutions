############################## MY CODE ########################
def print_rangoli(size):
    character_a = 97 # in ASCI
    base = character_a + size - 1
    characters = [chr(base)]
    current_characters = base
    temperory_list = [chr(base)]

    for i in range(0, size * 2 - 1):

        if i != 0:
            temperory_list = characters + characters[len(characters)-2::-1]
        

        if i >= size - 1:
            characters = characters[:-1]

        else:
            current_characters -= 1
            characters.append(chr(current_characters))
        
        if i == size * 2 - 2:
            temperory_list = [chr(base)] 

        print("-".join(temperory_list).center(4 * size - 3 , "-"))
        
        temperory_list = []
        
############################## END OF MY CODE ########################