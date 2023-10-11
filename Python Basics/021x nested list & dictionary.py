# Dictionary example

var = {"0": [0, 1, 2, 3],
       "1": [0, 1, 2, 3],
       "2": [0, 1, 2, 3]
}

for k, v in var.items():
    print(k, v)
    for i in v:
        print(k, i)