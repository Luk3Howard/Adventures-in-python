person1 = "Roger Federer "
person2 = " Rafael Nadal"
person3 = "      Andy Murray "

print(person1)
print(person2)
print(person3)

person1 = person1.rstrip()
person2 = person2.lstrip()
person3 = person3.strip()

print(f"Tennis Players:\n\t{person1}\n\t{person2}\n\t{person3}")