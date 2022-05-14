from datetime import datetime, timedelta
import json



def readJson(filename):
	with open(filename) as json_file:
		data = json.load(json_file)
	return data

def defaultconverter(o):
  if isinstance(o, datetime):
      return o.__str__()


def saveJson(filename, data):
	json_object = json.dumps(data, indent=4)
	with open(filename, "w") as outfile:
		outfile.write(json_object)


# goal = 10000

# data = {
# 	'day':[],
# 	'month':{},
# 	'allDays':[]
# }

def str_to_obj(string):
	return datetime.strptime(string, '%d/%m/%y')

def obj_to_str(object):
	return object.strftime("%d/%m/%y")


# today = datetime.now()
# today2 = datetime.date(datetime.now())

# today_str = today.strftime("%d/%m/%y")

# date_time_obj = datetime.strptime(today_str, '%d/%m/%y')

# print(date_time_obj)

# d = date_time_obj - timedelta(days=1)

# print(d)

# skarbonka = False

# while True:
# 	print('1 - Dodaj do skarbonki\n2 - Next Day')
# 	choice = input('.. ')
# 	if choice == '1':
# 		# skarbonka = True
# 		# while skarbonka:
# 		how = float(input('Ile chcesz dodac?\n'))
# 		data['day'].append(how)
# 	elif choice == '2':
# 		day_income = sum(data['day'])
# 		data['day'].clear()
# 		data['allDays'].append(day_income)
# 	elif choice == '3':
# 		print(data)


# if today_str in data:
# 	data[today_str].append(5)
# 	print('tak')
# 	saveJson('modern bank\data.json',data)
# else:
# 	data[today_str] = []

# 	saveJson('modern bank\data.json',data)



# history = data['lastupdate']

# history_obj = str_to_obj(history)

# today = datetime.now()

# delta = (today - history_obj).days

# print(delta)

# for x in range(int(delta)):
# 	actual_obj = today - timedelta(days=x)
# 	actual_str = obj_to_str(actual_obj)
# 	if actual_str in data_all:
# 		continue
# 	else:
# 		data_all[actual_str] = 0


# print(data)


# saveJson('modern bank\data.json',data)


def checkStatus(file):
	data = readJson(file)
	today_obj  = datetime.now()
	today_str = obj_to_str(today_obj)
	lastupdate_obj = str_to_obj(data['lastupdate'])
	if not today_str in data['history']:
		delta = (today_obj - lastupdate_obj).days
		for x in range(int(delta)):
			actual_obj = today_obj - timedelta(days=x)
			actual_str = obj_to_str(actual_obj)
			if actual_str in data['history']:
				continue
			else:
				data['history'][actual_str] = 0
		data['lastupdate'] = today_str
		saveJson(file, data)


checkStatus('modern bank\data.json')
saved = input('How much do you want to save?\n')


try:
	saved = float(saved)
except:
	print('You must type number [X] or [X.X]')

data = readJson('modern bank\data.json')
data_history = data['history']
lastupdate_str = data['lastupdate']
lastupdate_obj = str_to_obj(lastupdate_str)

today_obj  = datetime.now()
today_str = obj_to_str(today_obj)

data_history[today_str] += saved
lastupdate_str = today_str
saveJson('modern bank\data.json',data)
