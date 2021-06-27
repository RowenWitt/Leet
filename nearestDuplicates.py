def nearestDuplicate(a):
    
    # Move through list with first iterator, get first focus. From first focus, 
    # Move through list with second iterator 
    # print(a)
    best = [None]
    for i in range(len(a)):
        try:
            z = a.index(a[i], i+1)
            # print(f"Iter:{i}", f"Value:{a[i]}", f"Location:{z}", f"Diff:{z - i}")
            if best[0] == None:
                best = (a[i], z-i)
            # print(best)
            elif z - i < best[1]:
                best = (a[i], z-i)
            # print(best)
        except ValueError:
            pass
            
    if best[0] == None:
        return(-1)
    else:
        return(best[0])
    