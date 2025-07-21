from simulation.buses_generator import load_sample_buses
from simulation.tariff import load_tariff
from simulation.scheduler import scheduler
from simulation.depot import Depot
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

buses = load_sample_buses()
prices = load_tariff()
dt = 1  # hours
T = len(prices)
N = len(buses)
P_depot_max = 300

efficiency = 0.9
E_required = [bus.e_required - bus.soc for bus in buses]
P_bus_max = [bus.p_charging_max for bus in buses]

#availability for charging

availability = np.zeros((N,T))
for i, bus in enumerate(buses):
    for t in range(bus.arrive_time, bus.depart_time):
        if t < T:
            availability[i, t] = 1  # Bus is at depot

schedule = scheduler(dt, prices, N, E_required, P_bus_max, P_depot_max,availability, efficiency)

# Apply schedule to update SOCs
Depot(buses, P_depot_max).apply_schedule(schedule, dt)

# Print results
print("\nCharging Schedule (kW):")
for i in range(N):
    row = ", ".join(f"{p:.1f}" for p in schedule[i])
    print(f"Bus {i+1}: [{row}]  -> Final SoC: {buses[i].soc:.1f} kWh")

# Export to CSV
df = pd.DataFrame(schedule, index=[f"Bus {i+1}" for i in range(N)])
df.columns = [f"Hour {t+1}" for t in range(T)]
df.to_csv("results/charging_schedule.csv")
print("Saved")

# Report total energy and cost
total_energy_kwh = np.sum(schedule) * dt
total_cost = np.sum(schedule * prices) * dt
print(f"\nTotal Energy Delivered: {total_energy_kwh:.2f} kWh")
print(f"Total Charging Cost: £{total_cost:.2f}")

# Plot results
time = range(T)
plt.stackplot(time, schedule, labels=[f"Bus {i+1}" for i in range(N)])
plt.legend(loc='upper right', ncol=2)
plt.xlabel('Hour')
plt.ylabel('Charging Power (kW)')
plt.title('Bus Charging Schedule')
plt.tight_layout()
plt.show()
