def phi_inverse(t):
    n = 0
    while n*(n+1) / 2 <= t:
        n += 1
    n -= 1
    time = n
    strategy_nr = t - (n*(n+1)/2)
    time -= strategy_nr

    return strategy_nr, time

def get_v_and_c(i):
    c = i % 4
    vabs = 1 + i / 4
    if c == 0:
        return -vabs, '>'
    if c == 1:
        return vabs, '>'
    if c == 2:
        return vabs, '<'
    if c == 3:
        return -vabs, '<'

def gt(t, v):
    return t*(v+1)

def lt(t, v):
    return -gt(t, v)

def route(c):
    if c == '>': return gt
    if c == '<': return lt

def shoot_at(t):
    strategy_nr, time = phi_inverse(t)
    v, c = get_v_and_c(strategy_nr)
    wanted_shot = route(c)(time, v)
    fixed_shot = wanted_shot + v * (t-time)
    return fixed_shot, v, c, wanted_shot, time

for i in range(100):
    print(i, shoot_at(i))
