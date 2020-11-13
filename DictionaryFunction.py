def  nameAgeDict (name, age):
    '''Creates a dictionary using name as key and age as
value.\n Must be entered as a string'''
    a = dict()
    a[name] = age
    return a

def nameAgeDictList (name=list(), age=list()):
    '''Creates a dictionary using a list of name as key and
a list of age as value.\n Must be entered as a string'''
    a = dict()
    if len(name) == len(age):
        for i in range(len(name)):
            a[name[i]] = age[i]
        return a
    else:
        print ("ValueError:The two list must have \
the same length")
