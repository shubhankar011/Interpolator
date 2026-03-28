def babylonian_convergence(S):
    x = S / 2.0
    history = []
    for i in range(10):
        last_x = x
        x = 0.5 * (x + S / x)
        error = abs(x - (S**0.5))
        history.append(error)
    return history

i = int(input("Enter number: "))
s = babylonian_convergence(i)
j = 0
for error in s:
    j+=1
    print(f"After trying {j} time, error is {error}")