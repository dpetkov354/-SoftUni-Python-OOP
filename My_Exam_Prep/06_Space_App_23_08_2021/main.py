from project.space_station import SpaceStation

station = SpaceStation()

station.add_astronaut('Biologist', 'Pesho')
station.add_astronaut('Geodesist', 'Gosho')
station.add_astronaut('Meteorologist', 'Stamat')
print(station.report())

for _ in range(3):
    for a in station.astronaut_repository.astronauts:
        a.breathe()

print(station.report())
print(station.find_suitable_astronauts())
print(station.add_astronaut('Biologist', 'Gosho'))