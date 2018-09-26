mass = lambda x: x & 0xffffffff
f_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
v4 = mass(f_list[10])
v5 = mass(f_list[22] + v4)
v6 = mass(f_list[22] // 2 + v5)
v7 = mass(f_list[11] + v6)
v8 = mass(f_list[9] + v7)
v9 = mass(400 * (v8 + 1337 * f_list[10]))
v10 = mass(f_list[17])
number = mass(v9 * v10)
print(number) # postive
print(number - 0x100000000) # negative

# SHA256(-366284240) = 554a58cfad51e0d7df7e8287fa96223780a249b104de60425908abf0b83c69aa
# ==> DCTF{554a58cfad51e0d7df7e8287fa96223780a249b104de60425908abf0b83c69aa}