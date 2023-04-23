#x = [-7,-5,-3,-1,1,3,5,7,9,11]
#y = [2,1,4,2,-4,4,6,8,4,2]
#n = 'какая-то формула'
#file_name = 'название файла'
def deimpl(x, y, n, file_name): #data entry in matplotlib
    if (not isinstance(x, list)) and (not isinstance(y, list)):
        return('Error: y and x are not lists')
    elif not isinstance(x, list):
        return('Error: x is not a list')
    elif not isinstance(y, list):
        return('Error: y is not a list')
    elif (len(x) <= 1) and (len(y) <= 1):
        return('Error: the lengths of x and y lists are 0 or 1')
    elif len(x) <= 1:
        return('Error: list length x is 0 or 1')
    elif len(y) <= 1:
        return('Error: list length y is 0 or 1')
    elif len(x) != len(y):
        return('Error: lists x and y are not the same length')
    elif not isinstance(n, str):
        return('Error: n is not a string')
    elif (n == '') or (n == ' '):
        return('Error: n is an empty string')
    elif not isinstance(file_name, str):
        return('Error: file_name is not a string')
    elif (file_name == '') or (file_name == ' '):
        return('Error: file_name is an empty string')
    else:
        #print(x)
        #print(y)
        #print(n)
        import matplotlib.pyplot as plt
        plt.title('y = ' + n)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(x,y, marker='o')
        plt.show()
        
#deimpl(x, y, n, file_name)
