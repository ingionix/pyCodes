# from scipy import integrate
# def f(x):
#     return x**2+2*x+1
#
# result, error = integrate.quad(f, 0, 2)
# print(result)



import math
import matplotlib.pyplot as plt
W_values =[]
W = 0
for i in range(72):
    W += math.comb(71, i) * ((-1)**i) /  (i + 1)**5.2262
    W_values.append(W)

    print("i" + str(i), "=", W)

print("Final result" , 72 * W)

plt.plot(range(72), W_values)
plt.xlabel("i")
plt.ylabel("W")
plt.title("W vs. i")
plt.grid(True)
plt.show()

