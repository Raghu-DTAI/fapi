def cal1(operation,x,y):
    if(operation=='addition'):
        return x+y
    elif (operation=='subtraction'):
        if x>y:
            return x-y
        elif y>x:
            return y-x
        
    elif (operation=='multiplication'):
        return x*y
    elif(operation=='division'):
        return x//y
    
