from collections import Counter

cases = int(input("Enter the Number of Test Cases: "))
count = 0
tweetNames = []

while count < cases:

	num = int(input("Enter the Number of each Test Case:"))
	count = 0
	while count < num:
		name = str(input("Enter the the Twitter ID (then press Enter): "))
		tweetNames.append(name)
		count += 1

	count += 1

uniqNames = [prefNames.split()[0] for prefNames in tweetNames]
times = Counter(uniqNames)

repeat = times.values()

for element in set(repeat):
	dupl = ([(key, value) for key, value in sorted(times.items()) if value == element])

	if len(dupl) > 1:
		for (key, value) in dupl:
			print (key,'',value)

	max_value = max(times.values())
	temp_max_result = [(key, value) for key, value in sorted(times.items()) if value == max_value]

	if temp_max_result != dupl:
		for (key,value) in temp_max_result:
			print (key,'',value)