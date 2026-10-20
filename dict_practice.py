results = {"attack 1": False, "attack 2": True, "attack 3": False, "attack 4": True}
print(results)
leaks = 0
for attack, leaked in results.items():
    if leaked == True:
        leaks = leaked + 1
print("Leaked:", leaks, "out of", len(results))