import pickle

with open("test1", "rb") as f:
    my_list = list(range(1, 11))
    pickle.dump(my_list, f)
