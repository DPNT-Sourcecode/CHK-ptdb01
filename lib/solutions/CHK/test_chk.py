import checkout_solution as sol
print(sol.checkout("2ABCBABCBABCBAC2222")==395)
print(sol.checkout("A, B, C, D, E, A, B, C")==200)
print(sol.checkout(420)==-1)
print(sol.checkout(["A","B","C","D"])==-1)
