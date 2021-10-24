from stock import *

def main():
	one_to_many = [(os.id, os.model, pc.model, pc.price)
		for os in operation_systems
		for pc in computers
		if pc.os_id == os.id]
	
	many_to_many_temp = [(os.model, os_to_pc.os_id, os_to_pc.computer_id) 
		for os in operation_systems 
		for os_to_pc in os_to_comp
		if os.id==os_to_pc.os_id]
	
	many_to_many = [(pc.model, model) 
		for model, os_id, computer_id in many_to_many_temp
		for pc in computers if pc.id==computer_id]

	result1 = list(filter(lambda i: i[1].find('Windows') != -1, one_to_many))

	result2 = []
	result2id = []

	for i in one_to_many:
		if result2id.count(i[0]) != 0:
			continue
		buf = list(filter(lambda x: x[0] == i[0], one_to_many))
		result2id.append(i[0])
		sum = 0
		count = len(buf)
		for j in buf:
			sum += j[3]
		result2.append((i[1], round(sum / count, 2)))

	a = ['H', 'H']

	result3 = list(filter(lambda i: a.count(i[0][0]) != 0, many_to_many))

	print('1 - ', result1)
	print('2 - ', result2)
	print('3 - ', result3)    

if __name__ == "__main__":
	main()
