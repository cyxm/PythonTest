# !/usr/bin/python3

import pickle

file = open(r"e:\test\test.txt", "wb")
pickle.dump({"testobj": 1234}, file)
file.flush()
file.close()

file = open(r"e:\test\test.txt", "rb")
data = pickle.load(file)
print(data)
file.close()
