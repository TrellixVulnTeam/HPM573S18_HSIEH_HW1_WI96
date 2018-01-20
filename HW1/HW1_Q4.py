## Problem 4_1

yours = ['Yale','MIT','Berkeley']
mine = ['Yale','Harvard','UBC']

ours1 = mine + yours
print(ours1)

ours2=[] # create an empty list
ours2.append(mine) # append yours to this empty list
ours2.append(yours)
print(ours2)

print('The string ours1 gives a new list assigned to ours1 by adding yours and mine,'
      ' whereas ours2 mutates the original ours2 (mine) by appending the string called yours to the end of mine.'
      'ours1 contains only 1 string and ours2 contains 2.')

## Problem 4_2
yours[1]='Stanford'
print(yours)

print(ours1)
print(ours2)
print('Changing yours would change ours2 but not ours1 because strings are immutable. Therefore, we cannot mutate only a part of ours1 without re-assigning the entire string, '
      'but we can mutate yours or mine within ours2 without re-assigning the entire ours2 as each of yours and mine remains as separate strings in ours2.')