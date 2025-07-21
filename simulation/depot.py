
# simulation/depot.py
class Depot:
    def __init__(self, buses, max_power_kw):
        self.buses = buses
        self.max_power_kw = max_power_kw

    def apply_schedule(self, schedule, dt):
        N, T = schedule.shape
        total_energy_kwh = 0
        for i, bus in enumerate(self.buses):
            for t in range(T):
                energy = bus.charge(schedule[i][t], dt)
                total_energy_kwh += energy
        return total_energy_kwh

