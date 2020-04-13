# 1
zoo = ("elephant", "tiger", "snake", "turtle", "flamingo", "gorilla", "komodo dragon", "polar bear", "Kitty Baby", "praying mantis")

# 2
print(zoo.index("Kitty Baby"))

# 3
animal_to_find = "tiger"
if animal_to_find in zoo:
    print(f"Yes a {animal_to_find} is in the zoo")

# 4
(pachyderm, big_cat, limbless_reptile, shelled_reptile, vibrant_long_legs_ass_having_bird, swole_primate, scary_reptile, big_white_bear, kitty, insect) = zoo
print(pachyderm)
print(big_cat)
print(limbless_reptile)
print(shelled_reptile)
print(vibrant_long_legs_ass_having_bird)
print(swole_primate)
print(scary_reptile)
print(big_white_bear)
print(kitty)
print(insect)

# 5
listified_zoo = list(zoo)

# 6
listified_zoo.extend(["lemur", "zebra", "cheeta"])

# 7
tuplified_listified_zoo = tuple(listified_zoo)
print(f"Final tuple {tuplified_listified_zoo}")