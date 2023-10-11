spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
low = 0
normal = 0
high = 0
for spending in spendings:
    if spending < 1000.0:
        low += 1
    elif 1000.0 <= spending <= 2500.0:
        normal += 1
    else:
        high +=1
print(f"Numbers of months with low spendings: {low}, normal spendings: {normal}, high spendings: {high}.")