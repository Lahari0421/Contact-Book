#Contact
names =[]
phone_numbers=[]
num=7
for i in range(num):
    Name=input("Enter The Name: ")
    Phone_Number= int(input("Enter The Phone Number:"))
    names.append(Name)
    phone_numbers.append(phone_numbers)
    print("+"*50)
    print("Name:{}\nPhone_Number:{}".format(Name,Phone_Number))
    print("+"*50)
    for i in range(num):
        search_term=input("Search The Name:")
        print("+"*50)
        if search_term in names:
            term=names.index(search_term)
            number=phone_numbers[term]
            print("Name:{}\nPhone Number:{}".format(search_term,Phone_Number))
            break
        else:
            print("Name Not Found")