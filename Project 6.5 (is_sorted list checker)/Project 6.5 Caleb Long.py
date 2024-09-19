#Caleb Long Project 6.5

def is_sorted(mylist):
    #if list length is 1 or less, sorting doesnt matter
    if(len(mylist) >= 2):
        
        #indexing list
        for index in range(len(mylist) - 1):

            #check indexed values
            if(mylist[index] > mylist[index + 1]):
                return False 
        else:
            return True     
    else:
        return True

def main():
    #create list
    mylist = []

    #appending/editing list to test with is_sorted
    mylist.append(1)
    print(mylist)
    print(is_sorted(mylist))

    mylist.append(0)
    print(mylist)
    print(is_sorted(mylist))

    mylist[1] = 2
    mylist.append(3)
    print(mylist)
    print(is_sorted(mylist))

    mylist[1] = 0
    print(mylist)
    print(is_sorted(mylist))

main()