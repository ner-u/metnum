# untuk soal 2, dy/dt = a + y, a = 2
# 2026-04-23 21:16


def f(t, y):
    return 2 + y;

def rk4(t, t_fin, dt, y):
    i = 0
    while round(t, 5) < t_fin: # round() for avoiding any floating point arithmetic errs
        
        print(f"y{i} = {y}")
        print(f"saat t = {round(t+dt, 5)}")

        k1 = f(t, y)
        print(f"k1 = f({round(t, 5)}, {y}) = {k1}")

        k2 = f(t + dt / 2, y + (k1 * dt) / 2)
        print(f"k2 = f({round(t + dt / 2, 5)}, {y + (k1 * dt) / 2}) = {k2}")

        k3 = f(t + dt / 2, y + (k2 * dt) / 2)
        print(f"k3 = f({round(t + dt / 2, 5)}, {y + (k2 * dt) / 2}) = {k3}")
        
        k4 = f(t + dt, y + k3 * dt)
        print(f"k4 = f({round(t + dt, 5)}, {y + k3 * dt}) = {k4}")
        
        y = y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4) 
        print(f"y{i+1} = {y}\n")

        i += 1
        t += dt

def main():
    t = 0.0
    dt = 0.3
    y0  = 100.0
    t_fin = 0.6

    rk4(t, t_fin, dt, y0)

if __name__ == "__main__":
    main()
