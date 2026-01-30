def power(x,y):
    return x**y

results = []
pairs = [[5,2],[3,-1],[4,3],[2,0]]
for x, y in pairs:
    if y < 0:
        continue
    results.append(power(x, y))       #calling the function on valid inputs and updating the result list

print(results)
