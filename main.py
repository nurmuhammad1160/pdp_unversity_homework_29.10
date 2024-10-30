# 1
# # son = int(input("Son kiriting: "))
# if son > 0:
#     son += 1
# print(f"Natija: {son}")


# 2
# son = int(input("Son kiriting: "))
# if son > 0:
#     son += 1
# else:
#     son -= 2
# print(f"Natija: {son}")

# 3
# son = int(input("Son kiriting: "))
# if son > 0:
#     son += 1
# elif son < 0:
#     son -= 2
# else:
#     son = 10
# print(f"Natija: {son}")


# 4
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# musbatlar_soni = 0

# if a > 0:
#     musbatlar_soni += 1
# if b > 0:
#     musbatlar_soni += 1
# if c > 0:
#     musbatlar_soni += 1

# print(f"Musbat sonlar soni: {musbatlar_soni}")


# 5
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# musbatlar_soni = 0
# manfiylar_soni = 0

# if a > 0:
#     musbatlar_soni += 1
# elif a < 0:
#     manfiylar_soni += 1

# if b > 0:
#     musbatlar_soni += 1
# elif b < 0:
#     manfiylar_soni += 1

# if c > 0:
#     musbatlar_soni += 1
# elif c < 0:
#     manfiylar_soni += 1

# print("Musbat sonlar soni:", musbatlar_soni)
# print("Manfiy sonlar soni:", manfiylar_soni)


# 6 
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))

# if a > b:
#     print("Katta son:", a)
# else:
#     print("Katta son:", b)


# 7
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))

# if a < b:
#     print("Kichik son:", a)
# else:
#     print("Kichik son:", b)


# 8
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))

# if a > b:
#     print("Katta son:", a)
#     print("Kichik son:", b)
# else:
#     print("Katta son:", b)
#     print("Kichik son:", a)


# 9 
# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))

# if a < b:
#     a, b = b, a

# print("A:", a)
# print("B:", b)


# 10
# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))

# if a != b:
#     print("Yig'indi:", a + b)
# else:
#     print("Natija:", 0)


# 11
# a = int(input("A sonini kiriting: "))
# b = int(input("B sonini kiriting: "))

# if a != b:
#     if a > b:
#         print("Katta son:", a)
#     else:
#         print("Katta son:", b)
# else:
#     print("Natija:", 0)

# 12
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# min_s = a
# if min_s > b:
#     min_s = b
# if min_s > c:
#     min_s = c

# print(f"Eng kichik son: {min_s}")

# 13
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# if (a > b and a < c) or (a > c and a < b):
#     orta = a
# elif (b > a and b < c) or (b > c and b < a):
#     orta = b
# else:
#     orta = c

# print("O'rta qiymat:", orta)


# 14
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# min_s = a

# if a < b:
#     a = b
# if a < c:
#     a = c

# if min_s > b:
#     min_s = b
# if min_s > c:
#     min_s = c

# print(min_s)
# print(a)


# 15
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# yigindi1 = a + b
# yigindi2 = a + c
# yigindi3 = b + c

# if yigindi1 >= yigindi2 and yigindi1 >= yigindi3:
#     print("Eng katta yig'indi uchun sonlar:", a, b)
# elif yigindi2 >= yigindi1 and yigindi2 >= yigindi3:
#     print("Eng katta yig'indi uchun sonlar:", a, c)
# else:
#     print("Eng katta yig'indi uchun sonlar:", b, c)


# 16 
a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))

if a < b < c:
    a *= 2
    b *= 2
    c *= 2
else:
    a = -a
    b = -b
    c = -c

print(f"{a} {b} {c}")

# # 17
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# if a > b > c and a < b < c:
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a = -a
#     b = -b
#     c = -c

# print(f"{a} {b} {c}")

# # 18
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# if a == b:
#     print("Tartib raqami:", 3)
# elif a == c:
#     print("Tartib raqami:", 2)
# elif b == c:
#     print("Tartib raqami:", 1)
# else:
#     print("Hech biri teng emas")

# # 19
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
# d = int(input("4-sonni kiriting: "))

# if a == b == c:
#     print("Tartib raqami:", 4)
# elif a == b == d:
#     print("Tartib raqami:", 3)
# elif a == c == d:
#     print("Tartib raqami:", 2)
# elif b == c == d:
#     print("Tartib raqami:", 1)
# else:
#     print("Hech biri teng emas")

# # 20
# A = float(input("A nuqtasi: "))
# B = float(input("B nuqtasi: "))
# C = float(input("C nuqtasi: "))

# masofa_B = abs(A - B)
# masofa_C = abs(A - C)

# if masofa_B < masofa_C:
#     print("A nuqtasiga eng yaqin nuqta: B, masofa:", masofa_B)
# else:
#     print("A nuqtasiga eng yaqin nuqta: C, masofa:", masofa_C)

# # 21
# x = int(input("X koordinatasi: "))
# y = int(input("Y koordinatasi: "))

# if x == 0 and y == 0:
#     print(0)
# elif y == 0:
#     print(1)
# elif x == 0:
#     print(2)
# else:
#     print(3)

# # 22
# x = int(input("X koordinatasi: "))
# y = int(input("Y koordinatasi: "))

# if x > 0 and y > 0:
#     print("1-chorak")
# elif x < 0 and y > 0:
#     print("2-chorak")
# elif x < 0 and y < 0:
#     print("3-chorak")
# elif x > 0 and y < 0:
#     print("4-chorak")

# # 23
# x1, y1 = int(input("1-uch X: ")), int(input("1-uch Y: "))
# x2, y2 = int(input("2-uch X: ")), int(input("2-uch Y: "))
# x3, y3 = int(input("3-uch X: ")), int(input("3-uch Y: "))

# if x1 == x2:
#     x4 = x3
# elif x1 == x3:
#     x4 = x2
# else:
#     x4 = x1

# if y1 == y2:
#     y4 = y3
# elif y1 == y3:
#     y4 = y2
# else:
#     y4 = y1

# print(f"To‘rtinchi uch koordinatalari: ()")