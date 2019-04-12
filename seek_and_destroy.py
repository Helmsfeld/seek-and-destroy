import sys
import itertools


def z_to_zz(z):
    n = 0
    while n * (n + 1) // 2 <= z:
        n += 1
    n -= 1
    x = z - (n * (n + 1) // 2)
    y = n - x

    return x, y


def gt(t, v):
    return t * (v + 1)


def lt(t, v):
    return -gt(t, v)


def get_v_and_c(i):
    c = i % 6
    vabs = 1 + i // 6
    if c == 0:
        return 0, gt
    if c == 1:
        return -vabs, gt
    if c == 2:
        return vabs, gt
    if c == 3:
        return 0, lt
    if c == 4:
        return vabs, lt
    if c == 5:
        return -vabs, lt


def shoot_at(t):
    strategy_nr, time = z_to_zz(t)
    v, c = get_v_and_c(strategy_nr)
    wanted_shot = c(time, v)
    fixed_shot = wanted_shot + v * (t - time)
    return fixed_shot, v, c, wanted_shot, time


if len(sys.argv) == 3:
    x = sys.argv[1]
    v = sys.argv[2]
else:
    x = 413
    v = 5

print("Position: {}".format(x))
print("Velocity: {}".format(v))

# for i in range(10000):
# print(i, shoot_at(i)[0])

for t in itertools.count():
    xt = x + v * t
    shot = shoot_at(t)
    i = shot[0]
    # print(xt, shot)
    if xt == i:
        print("Found at t={}".format(t))
        break
