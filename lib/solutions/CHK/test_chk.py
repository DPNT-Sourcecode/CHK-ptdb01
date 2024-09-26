import checkout_solution as sol

# print(sol.checkout("2ABCBABCBABCBAC2222")==-1)
# print(sol.checkout("A, B, C, D, E, A, B, C")==-1)
# print(sol.checkout(420)==-1)
# print(sol.checkout(["A","B","C","D"])==-1)

# print(sol.checkout("") == 0)
# print(sol.checkout("A") == 50)
# print(sol.checkout("B") == 30)
# print(sol.checkout("C") == 20)
# print(sol.checkout("D") == 15)
# print(sol.checkout("a") == -1)
# print(sol.checkout("-") == -1)
print(sol.checkout("ABCa") == -1)
print(sol.checkout("AxA") == -1)
print(sol.checkout("ABCD") == 115)
print("A",sol.checkout("A") == 50)
print(200*(1//5) + 130*((1 % 5)//3) + 50*((1 % 5) % 3))
print("AA",sol.checkout("AA") == 100)
print("AAA",sol.checkout("AAA") == 130)
print("AAAA",sol.checkout("AAAA") == 180)
print("AAAAA",sol.checkout("AAAAA") == 200)
print("AAAAAA",sol.checkout("AAAAAA") == 250)
print("B",sol.checkout("B") == 30)
print("BB",sol.checkout("BB") == 45)
print("BBB",sol.checkout("BBB") == 75)
print("BBBB",sol.checkout("BBBB") == 90)
print("ABCDABCD",sol.checkout("ABCDABCD") == 215)
print("BABDDCAC",sol.checkout("BABDDCAC") == 215)
print("AAABB",sol.checkout("AAABB") == 175)
print("ABCDCBAABCABBAAA",sol.checkout("ABCDCBAABCABBAAA") == 495)

print("ABCDCBAABCABBAAAEEE",sol.checkout("ABCDCBAABCABBAAAEEE"),sol.checkout("ABCDCBAABCABBAAAEEE") == 585)
print("ABCDCBAABCABBAAAE",sol.checkout("ABCDCBAABCABBAAAE"),sol.checkout("ABCDCBAABCABBAAAE") == 535)
print("BBBB",sol.checkout("BBBB") == 90)
print("BBBBEEEEEEEEEE",sol.checkout("BBBBEEEEEEEEEE"),sol.checkout("BBBBEEEEEEEEEE") == 400)
print(max([4 - 10//2, 0]))

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+