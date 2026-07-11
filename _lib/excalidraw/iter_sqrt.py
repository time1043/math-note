import matplotlib.pyplot as plt
from math import sqrt


def iterate(func, x0, n):
    values = [x0]
    x = x0
    for _ in range(n):
        x = func(x)
        values.append(x)
    return values


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left: N=10, x0=2 and 1/3
for v0 in [2, 1 / 3]:
    seq = iterate(sqrt, v0, 10)
    ax1.plot(range(len(seq)), seq, label=f"$x_0 = {v0}$", marker=".", markersize=3)

ax1.set_title("Iterating $f(x) = \\sqrt{x}$ (Fixed point $= 1$)")
ax1.set_xlabel("Iteration")
ax1.set_ylabel("Value")
ax1.legend()
ax1.axhline(y=1, color="gray", linestyle="--", alpha=0.5)
ax1.grid(True, alpha=0.3)

# Right: N=50, add x0=100
for v0 in [2, 1 / 3, 100]:
    seq = iterate(sqrt, v0, 50)
    ax2.plot(range(len(seq)), seq, label=f"$x_0 = {v0}$", marker=".", markersize=3)

ax2.set_title("Iterating $f(x) = \\sqrt{x}$ (Fixed point $= 1$)")
ax2.set_xlabel("Iteration")
ax2.set_ylabel("Value")
ax2.legend()
ax2.axhline(y=1, color="gray", linestyle="--", alpha=0.5)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("iter_sqrt.svg")
plt.show()
