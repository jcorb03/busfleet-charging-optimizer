EV Buses Charging Optimiser 
- Uses Linear Programming to solve for optimum charging schedule of buses to minimize energy costs
- Outplots Matplotlib stack plot and csv results/charging_schedule.csv

Problem Variables:
Bus: (simulation/bus)
- battery_capacity - Bus battery capacity (kWh)
- soc - Battery initial state of charge (kWh)
- e-required - Energy requirements by departure (kWh)
- p_charging_max - Max charging power (kW)
- P_depot_max - Depot maximum power (kW)
- arrival_time & departure_time - time window in which charging is available
- efficiency - Charging Efficiency

Depot: (simulation/depot)
- P_depot_max - Depot maximum power (kW)
- Tariffs: Varying electricity price by hour

Requirements:
Scipy Matplotlib Pandas (pip install)

Run the script:
python main.py

Example Output:

Bus 1: [50.0, 50.0, 50.0, 0.0, 0.0, 0.0, 0.0, 16.7]  -> Final SoC: 250.0 kWh
Bus 2: [50.0, 11.1, 50.0, 0.0, 0.0, 0.0, 0.0, 33.3]  -> Final SoC: 250.0 kWh
...

![alt text](image.png)