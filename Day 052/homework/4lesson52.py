def find_it(seq):
     for num in seq:
            x = seq.count(num)
            if x % 2 == 0:
                continue
            return num
        
                
print(find_it([1,1,3,4,555, 5,6,67,7,7,8,9,10,9]))