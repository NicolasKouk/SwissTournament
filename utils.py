# finds if the element x exists in any of the pairs that the list mylist contains
def is_in_list_of_pairs(mylist, x):
    return (x in [i for (i,j) in mylist]) or (x in [j for (i,j) in mylist])