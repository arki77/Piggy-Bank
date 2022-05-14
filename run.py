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

def str_to_obj(string):
	return datetime.strptime(string, '%d/%m/%y')

def obj_to_str(object):
	return object.strftime("%d/%m/%y")

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
