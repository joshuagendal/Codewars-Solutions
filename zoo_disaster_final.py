# Story

# A freak power outage at the zoo has caused all of the electric cage doors to malfunction and swing open...

# All the animals are out and some of them are eating each other!
# It's a Zoo Disaster!

# Here is a list of zoo animals, and what they can eat

#     antelope eats grass
#     big-fish eats little-fish
#     bug eats leaves
#     bear eats big-fish
#     bear eats bug
#     bear eats chicken
#     bear eats cow
#     bear eats leaves
#     bear eats sheep
#     chicken eats bug
#     cow eats grass
#     fox eats chicken
#     fox eats sheep
#     giraffe eats leaves
#     lion eats antelope
#     lion eats cow
#     panda eats leaves
#     sheep eats grass

# Kata Task
# INPUT

# A comma-separated string representing all the things at the zoo
# TASK

# Figure out who eats who until no more eating is possible.
# OUTPUT

# A list of strings (refer to the example below) where:

#     The first element is the initial zoo (same as INPUT)
#     The last element is a comma-separated string of what the zoo looks like when all the eating has finished
#     All other elements (2nd to last - 1) are of the form X eats Y describing what happened

# Notes

#     Animals can only eat things beside them

#     Animals always eat to their LEFT before eating to their RIGHT

#     Always the LEFTMOST animal capable of eating will eat before any others

#     Any other things you may find at the zoo (which are not listed above) do not eat anything and are not edible

# Example
#   INPUT   
# "fox,bug,chicken,grass,sheep"
# 1 fox can't eat bug   
# "fox,bug,chicken,grass,sheep"
# 2 bug can't eat anything  
# "fox,bug,chicken,grass,sheep"
# 3 chicken eats bug    
# "fox,chicken,grass,sheep"
# 4 fox eats chicken    
# "fox,grass,sheep"
# 5 fox can't eat grass 
# "fox,grass,sheep"
# 6 grass can't eat anything    
# "fox,grass,sheep"
# 7 sheep eats grass    
# "fox,sheep"
# 8 fox eats sheep  
# "fox"
#   OUTPUT  
# ["fox,bug,chicken,grass,sheep", "chicken eats bug", "fox eats chicken", "sheep eats grass", "fox eats sheep", "fox"]


def who_eats_who(zoo):
    animal_chain = {
        'antelope': 'grass',
        'big-fish': 'little-fish',
        'bug': 'leaves',
        'bear': [
            'big-fish',
            'bug',
            'chicken',
            'cow',
            'leaves',
            'sheep'
        ],
        'chicken': 'bug',
        'cow': 'grass',
        'fox': [
            'chicken',
            'sheep'
        ],
        'giraffe': 'leaves',
        'lion': [
            'antelope',
            'cow'
        ],
        'panda': 'leaves',
        'sheep': 'grass'
    }
    zoo_lst = zoo.split(',')
    final = []
    final_item_str = ''
    eating_actions = []
    restart_loop = False
    while restart_loop == False:
        for i in range(len(zoo_lst)):
            if i == 0:
                if len(zoo_lst) == 1:
                    restart_loop = True
                else:    
                    if animal_chain.has_key(zoo_lst[i]) and zoo_lst[i + 1] in animal_chain[zoo_lst[i]]:
                        eating_actions.append(zoo_lst[i] + ' eats ' + zoo_lst[i + 1])
                        zoo_lst.pop(i + 1)
                        break
            # NOTE: Below is condition where there is only 1 item left in zoo_lst, where all other animals have been eaten except one.
            elif i == len(zoo_lst) - 1:                             
                if animal_chain.has_key(zoo_lst[i]) and zoo_lst[i - 1] in animal_chain[zoo_lst[i]]:
                    eating_actions.append(zoo_lst[i] + ' eats ' + zoo_lst[i - 1])
                    zoo_lst.pop(i - 1)
                    break
                else:  
                    restart_loop = True                             
            else:                                                                   
                if animal_chain.has_key(zoo_lst[i]) and zoo_lst[i - 1] in animal_chain[zoo_lst[i]]: 
                    eating_actions.append(zoo_lst[i] + ' eats ' + zoo_lst[i - 1])
                    zoo_lst.pop(i - 1)   
                    break
                elif animal_chain.has_key(zoo_lst[i]) and zoo_lst[i + 1] in animal_chain[zoo_lst[i]]:
                    eating_actions.append(zoo_lst[i] + ' eats ' + zoo_lst[i + 1])
                    zoo_lst.pop(i + 1)
                    break
    # Pack final (list variable) w/ proper text according to codewars problem specifics
    final.append(zoo)
    for i in eating_actions:
        final.append(i)
    for i in zoo_lst:
        final_item_str += i + ','
    final.append(final_item_str)
    final[-1] = final[-1][:-1]
    return final