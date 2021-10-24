from Class import *

computers = [
	Computer(1, 'Dell XPS 17', 10000, 1),
	Computer(2, 'iMac MHK23RU/A', 18000, 1),
	Computer(3, 'CoolerMaster COSMOS C700P', 14000, 3),
	Computer(4, 'Gygabite Aero 17 HDR YD-94RU548SP', 23000, 5),
	Computer(5, 'Nvidia GeForce RTX 3080', 27000, 2),
	Computer(6, 'HyperPC Lumen M4', 33000, 6),
	Computer(7, 'Acer ASPIRE 3', 47000, 4),
	Computer(8, 'HyperPC CONCEPT 4', 42000, 7),
	Computer(9, 'MacBook Air M1', 52000, 2),
	Computer(10, 'HP 470 G8', 59000, 5)
]

operation_systems = [
	OperatingSystem(1, 'Windows XP', 2001),
	OperatingSystem(2, 'Windows Vista', 2007),
	OperatingSystem(3, 'Windows 7', 2009),
	OperatingSystem(4, 'Windows 10', 2015),
	OperatingSystem(5, 'Linux', 1991),
	OperatingSystem(6, 'Ubuntu', 2004),
	OperatingSystem(7, 'MacOS', 2000)
]

os_to_comp = [
	OSC(1, 1),
	OSC(1, 4),
	OSC(1, 6),
	OSC(1, 8),
	OSC(2, 1),
	OSC(2, 5),
	OSC(2, 7),
	OSC(2, 8),
	OSC(3, 1),
	OSC(3, 6),
	OSC(3, 10),
	OSC(4, 1),
	OSC(4, 3),
	OSC(5, 2),
	OSC(5, 9),
	OSC(6, 2),
	OSC(6, 5),
	OSC(6, 8),
	OSC(7, 2),
	OSC(7, 6),
	OSC(7, 10)
]
