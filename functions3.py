def howmany(legs,heads):
    chikens = (legs - (heads * 2))/2
    rabbits = heads - chikens
    return (int(chikens),int(rabbits))

heads = int(input("How many heads: "))
legs = int(input("How many legs: "))

chiken , rabbits = howmany(legs,heads)
print(f"We have {chiken} chickens and {rabbits} rabbits ")