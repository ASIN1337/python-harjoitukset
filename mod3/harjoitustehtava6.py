import random

koodi3=[random.randint(100,999) for _ in range(1)]
print(koodi3)

koodi1="".join(str(random.randint(1,6)) for _ in range(4))

print(koodi1)

