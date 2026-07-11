import matplotlib.pyplot as plt
from math import cos

N = 30
init_values = [1, 2, 1 / 3]


def iterate(func, x0, n):
    values = [x0]
    x = x0
    for _ in range(n):
        x = func(x)
        values.append(x)
    return values


fig, ax = plt.subplots(figsize=(8, 5))
for v0 in init_values:
    seq = iterate(cos, v0, N)
    ax.plot(range(len(seq)), seq, label=f"$x_0 = {v0}$", marker=".", markersize=3)

ax.set_title("Iterating $f(x) = \\cos(x)$ (Fixed point $\\approx 0.7391$)")
ax.set_xlabel("Iteration")
ax.set_ylabel("Value")
ax.legend()
ax.axhline(y=0.739085, color="gray", linestyle="--", alpha=0.5)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("iter_cos.svg")
plt.show()
