ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
print(stuff)
print(len(stuff))

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

i = 0

while len(stuff) < 10:
    item = more_stuff[i]
    i += 1
    print("Adding: ", item)
    stuff.append(item)
    print(f"Now there is {len(stuff)} items!")


print(stuff)


print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
