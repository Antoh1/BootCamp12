def find_missing(list1,list2):
    """This function finds the missing number in one of the given two lists and returns respective output"""
    
    absent = 0 #initialize variable absent to hold absent digit to zero
    if len(list1) < len(list2): #find and  display missing number if first list is smaller
        missing = (set(list2) - set(list1))
        absent = missing.pop()
        return absent
    elif len(list2) < len(list1): #find and  display missing number if second list is smaller
        missing = (set(list1) - set(list2))
        absent = missing.pop()
        return absent
    else: #default statement
        return 0