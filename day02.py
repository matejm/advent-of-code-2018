from collections import defaultdict

with open('input') as file:
    lines = [i.strip() for i in file.readlines()]

exactly_2 = 0
exactly_3 = 0

for id_str in lines:
	d = defaultdict(int)

	for c in id_str:
		d[c] += 1

	if 2 in d.values():
		exactly_2 += 1
	if 3 in d.values():
		exactly_3 += 1

print('First star:', exactly_2 * exactly_3)

finish = False

for i in range(len(lines)):
	if finish:
		break

	for j in range(i + 1, len(lines)):

		differ = 0
		s = ''

		for a, b in zip(lines[i], lines[j]):
			if a != b:
				differ += 1
			else:
				s += a

		if differ == 1:
			print('Second star:', s)
			finish = True
			break