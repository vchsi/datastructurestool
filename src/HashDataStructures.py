from datastructures import Hashmap
def get(key,new_hashmap):
	try:
		return new_hashmap.hashmapdict[key]
	except KeyError:
		print("Key does not exist")
		return
def put(key,value,new_hashmap):
	new_hashmap.hashmapdict[key] = value
	new_hashmap.size += 1
def size(new_hashmap):
	return new_hashmap.size
def delete(new_hashmap,key):
	try:
		value = new_hashmap.hashmapdict[key]
		del new_hashmap.hashmapdict[key]
		new_hashmap.size -= 1
		return value
	except KeyError:
		print("The Key doesnt exist")
def keys(new_hashmap):
	return list(new_hashmap.hashmapdict)
def hashmapEmpty(new_hashmap):
	new_hashmap.hashmapdict = {}
	new_hashmap.size = 0
def twoDListToHashMap(multidlist):
	final = Hashmap({},0)
	for i in range(len(multidlist)):
		final.hashmapdict[multidlist[i][0]] = multidlist[i][1]
	return final