#2) შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან ---> (["vano" , "nika" , "bubazi" , "zauri"....)], დამატებით შექმენით ორი სია odd = [] და even = [], გადაუარეთ ორიგინალ სიას for ციკლით და გაიგეთ რომელი ელემენტი შედგება კენტი ასოებისგან და რომელი ლუწი, საბოლოოდ ჩაამატეთ შესაბამისი სტრინგები შესაბამის სიებში (odd / even) დიდ ასოებათ (upper) და ბოლოს დაბეჭდეთ.
def list():
    strings = ["aleqsi", "niko", "luka", "gio", "nugzari", "shokoladiani blini"]
    even = []
    odd = []
    for i in strings:
        if len(i) % 2 == 0:
            even.append(i)
             
        if len(i) % 2 != 0 :
            odd.append(i)
    print(odd)    
    print(even)
       
        
list()