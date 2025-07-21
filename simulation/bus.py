class Bus:
    def __init__(self, bus_id, soc, battery_capacity=300, e_required=250, p_charging_max=50, arrive_time=0, depart_time=8, efficiency=0.9):
        self.bus_id = bus_id
        self.battery_capacity = battery_capacity
        self.e_required = e_required
        self.soc = soc
        self.p_charging_max = p_charging_max
        self.arrive_time = arrive_time
        self.depart_time = depart_time
        self.efficiency = efficiency

    def charge(self, power_kw, dt_hr):
        actual_power = min(power_kw, self.p_charging_max)
        energy_input = actual_power * dt_hr * self.efficiency
        charge_space = self.battery_capacity - self.soc
        energy_charged = min(energy_input, charge_space)
        self.soc += energy_charged
        return energy_charged / self.efficiency

    def is_ready(self):
        return self.soc >= self.e_required

    def needs_energy(self):
        return max(0, self.e_required - self.soc)