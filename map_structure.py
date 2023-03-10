# map structure
mapa = {}

# add key-value pairs
mapa["key"] = "value"
mapa["key2"] = "value2"

# get value by key
print(mapa["key"])

# check if key exists
if "key" in mapa:
    print("key exists")

# remove key-value pair
del mapa["key"]

# iterate over key-value pairs
for key, value in mapa.items():
    print(key, value)

# iterate over keys
for key in mapa.keys():
    print(key)

# iterate over values
for value in mapa.values():
    print(value)

# get number of key-value pairs
print(len(mapa))

# get all keys
print(mapa.keys())

# get all values
print(mapa.values())

# get all key-value pairs
print(mapa.items())

# check if map is empty
print(len(mapa) == 0)

# clear map
mapa.clear()

# delete map
del mapa
