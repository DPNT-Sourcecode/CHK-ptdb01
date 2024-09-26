import checkout_solution as sol
print(sol.checkout("2ABCBABCBABCBAC2222")==395)
print(sol.checkout("A, B, C, D, E, A, B, C")==200)
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
print(sol.checkout("AxA") == 100)
print(sol.checkout("ABCD") == 115)
print(sol.checkout("A") == 50)
print(sol.checkout("AA") == 100)
print(sol.checkout("AAA") == 130)
print(sol.checkout("AAAA") == 180)
print(sol.checkout("AAAAA") == 230)
print(sol.checkout("AAAAAA") == 260)
print(sol.checkout("B") == 30)
print(sol.checkout("BB") == 45)
print(sol.checkout("BBB") == 75)
print(sol.checkout("BBBB") == 90)
print(sol.checkout("ABCDABCD") == 215)
print(sol.checkout("BABDDCAC") == 215)
print(sol.checkout("AAABB") == 175)
print(sol.checkout("ABCDCBAABCABBAAA") == 505)
