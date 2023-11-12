def printAll(*args, **kwargs):
    for element in args:
        # print("100")
        print("type:"+type(element).__name__+", value:"+str(element))
    
    for key,value in kwargs.items():
        # print("200")
        print("key:"+key+", type:"+type(value).__name__+", value:"+str(value))
    
if __name__=="__main__":
    dict={
        'name':'zhangsan',
        'age':'20',
        'skill':['eat','sleep', 'drink']
    }

    # printAll(1,2,3,['a','b','c'],dict)
    printAll(1,2,3,['a','b','c'],**dict)


# output

# type:int, value:1
# type:int, value:2
# type:int, value:3
# type:list, value:['a', 'b', 'c']
# key:name, type:str, value:zhangsan
# key:age, type:str, value:20
# key:skill, type:list, value:['eat', 'sleep', 'drink']