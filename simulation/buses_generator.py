def load_sample_buses():
    from .bus import Bus
    return [
        Bus(bus_id=1, soc=100),
        Bus(bus_id=2, soc=120),
        Bus(bus_id=3, soc=140),
        Bus(bus_id=4, soc=150),
        Bus(bus_id=5, soc=60),
        Bus(bus_id=6, soc=40),
        Bus(bus_id=7, soc=230),
        Bus(bus_id=8, soc=200),
    ]