def dir_reduc(arr):
    opposite = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    for i in range(len(arr)-1):
        if arr[i+1] == opposite[arr[i]]:
            del arr[i], arr[i]
            return dir_reduc(arr)

    return arr

print(["NORTH", "SOUTH", "WEST", "EAST"])