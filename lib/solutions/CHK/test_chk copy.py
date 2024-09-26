import checkout_solution as sol

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

print("ABCDCBAABCABBAAAE",sol.checkout("ABCDCBAABCABBAAAE"),sol.checkout("ABCDCBAABCABBAAAE") == 535)
print("BBBB",sol.checkout("BBBB") == 90)
print("BBBBEEEEEEEEEE",sol.checkout("BBBBEEEEEEEEEE"),sol.checkout("BBBBEEEEEEEEEE") == 400)

print("FFFFFFFFFFFF",sol.checkout("FFFFFFFFFFFF"),sol.checkout("FFFFFFFFFFFF") == 80)
print("FF",sol.checkout("FF"),sol.checkout("FF") == 20)
print("FFF",sol.checkout("FFF"),sol.checkout("FFF") == 20)
print("ABCDCBAABCABBAAAFFFF", sol.checkout("ABCDCBAABCABBAAAFFFF"), sol.checkout("ABCDCBAABCABBAAAFFFF") == 525)
print("ABCDEFGHIJKLMNOPQRSTUVWXYZ", sol.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), sol.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 965)
print("UUU", sol.checkout("UUU"), sol.checkout("UUU") == 120)
print("UUUU", sol.checkout("UUU"), sol.checkout("UUU") == 120)
print("UUUUU", sol.checkout("UUU"), sol.checkout("UUU") == 160)
print("UUUUUUUU", sol.checkout("UUU"), sol.checkout("UUU") == 240)

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+



