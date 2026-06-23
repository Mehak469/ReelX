import ast
def convert(obj):
    """
    This function takes a string representation of a list of dictionaries, converts it to a list of dictionaries, and then extracts the "name" value from each dictionary to create a list of names. 
    """
    obj=ast.literal_eval(obj)
    L=[]
    for i in obj:
        L.append(i["name"])
    return L

def cast(obj):

    """
    This function takes a string representation of a list of dictionaries, converts it to a list of dictionaries, and then extracts the "name" value from the first three dictionaries(3 main/Popular Actors) to create a list of names.`
    """
    obj=ast.literal_eval(obj)
    counter=0
    L=[]
    for i in obj:
        if counter!=3:
            L.append(i["name"])
            counter+=1
        else:
            break
    return L

import ast
def fetch_director(obj):
    """
    This function takes a string representation of a list of dictionaries, converts it to a list of dictionaries, and then extracts the "name" value from the dictionary where the "job" key has the value "Director". It returns a list containing the director's name.

    """
    obj=ast.literal_eval(obj)
    L=[]
    for i in obj:
        if i["job"]=="Director":
            L.append(i["name"])
            break
    return L