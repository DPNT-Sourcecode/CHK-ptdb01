import checkout_solution as sol

print(sol.checkout("2ABCBABCBABCBAC2222")==-1)
print(sol.checkout("A, B, C, D, E, A, B, C")==-1)
print(sol.checkout(420)==-1)
print(sol.checkout(["A","B","C","D"])==-1)

print(sol.checkout("") == 0)
print(sol.checkout("A") == 50)
print(sol.checkout("B") == 30)
print(sol.checkout("C") == 20)
print(sol.checkout("D") == 15)
print(sol.checkout("a") == -1)
print(sol.checkout("-") == -1)
print(sol.checkout("ABCa") == -1)
print(sol.checkout("AxA") == -1)
print(sol.checkout("ABCD") == 115)
print(sol.checkout("A") == 50)
print(sol.checkout("AA") == 100)
print(sol.checkout("AAA") == 130)
print(sol.checkout("AAAA") == 180)
print(sol.checkout("AAAAA") == 200)
print(sol.checkout("AAAAAA") == 250)
print(sol.checkout("B") == 30)
print(sol.checkout("BB") == 45)
print(sol.checkout("BBB") == 75)
print(sol.checkout("BBBB") == 90)
print(sol.checkout("ABCDABCD") == 215)
print(sol.checkout("BABDDCAC") == 215)
print(sol.checkout("AAABB") == 175)
print(sol.checkout("ABCDCBAABCABBAAA") == 505)

print(sol.checkout("ABCDCBAABCABBAAAEEE") == 505)
print(sol.checkout("ABCDCBAABCABBAAAE") == 505)
print(sol.checkout("BBBB") == 505)
print(sol.checkout("BBBBEEEEEEEEEE") == 240)

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+
