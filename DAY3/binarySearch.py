class BinarySearch(list):
    """this class creates instances of various lists. it receives 
    length(integer) of list to be generated and the steps(integer) 
    which is the difference between consecutive values in the list to be generated"""
    
    def __init__(self, a, b, *args): 
        """the constructor method for class instance variables"""
        
        list.__init__(self, *args) #initializes the list to be generated
        self.list_length = a  #length of the list to be generated
        self.step = b #steps within the consecutive values in the list to be generated
        end = self.list_length * self.step #the end point/value in the list to be generated
        for value in range(self.step, end + 1, self.step): #loop to generate a list
            self.append(value)
        self.length = len(self) #an instance variable 'length' to hold length of a list instance   
    def search(self, binary_item, first_item=0, last_item=None, count_iter=0):
        """method to search for a binary_item within a generated list instance and 
        return a dictioray containing the indexof the item searched and number of iterations executed"""
        if not last_item:
            last_item = self.length - 1
        if binary_item == self[first_item]:
            return {'index': first_item, 'count': count_iter}
        elif binary_item == self[last_item]:
            return {'index': last_item, 'count': count_iter}
        midpoint = (first_item + last_item) // 2
        if binary_item == self[midpoint]:
            return {'index': midpoint, 'count': count_iter}
        elif binary_item > self[midpoint]:
            first_item = midpoint + 1
        elif binary_item < self[midpoint]:
            last_item = midpoint - 1
        if first_item >= last_item:
            return {'index': -1, 'count': count_iter}
        count_iter += 1  
        return self.search(binary_item, first_item, last_item, count_iter)        