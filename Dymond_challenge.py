# Augstums
aug = int(input("romba(dimants) augstums: "))
print(aug)

for i in range(aug):
    print(" "*(aug-i), "&"*(i*2+1))


for i in range(aug-2, -1, -1):
    print(" "*(aug-i), "&"*(i*2+1))
# Augstuma  tiek nemts no vertikālās ass , kas sadala rombu, ieskaitot ass līniju..