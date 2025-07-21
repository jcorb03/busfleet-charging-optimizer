from scipy.optimize import linprog
import numpy as np

def scheduler(dt, prices, N, E_required, P_bus_max, P_depot_max, availability, efficiency=0.9):
    T = len(prices)
    c = np.tile(prices, N) * dt

    

    A_ub = []
    b_ub = []

    # Bus energy need constraints
    for i in range(N):
        row = np.zeros(N * T)
        for t in range(T):
            row[i*T + t] = -dt * efficiency
        A_ub.append(row)
        b_ub.append(-E_required[i])

    # Depot max power constraints per timestep
    for t in range(T):
        row = np.zeros(N * T)
        for i in range(N):
            row[i*T + t] = 1.0
        A_ub.append(row)
        b_ub.append(P_depot_max)

    # Bounds for each variable (charging power at each time)
    bounds = []
    for i in range(N):
        for t in range(T):
            if availability[i][t] == 1:
                bounds.append((0, P_bus_max[i]))  # Bus is present → allow charging
            else:
                bounds.append((0, 0))             # Bus is away → force zero

    result = linprog(c=c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

    if result.success:
        return result.x.reshape((N, T))
    else:
        raise RuntimeError(f"Optimization failed: {result.message}")
