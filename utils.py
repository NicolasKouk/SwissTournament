import time

# finds if the element x exists in any of the pairs that the list mylist contains
def is_in_list_of_pairs(mylist, x):
    return (x in [i for (i,j) in mylist]) or (x in [j for (i,j) in mylist])

def is_valid_score(s):
    try:
        score = [int(i) for i in s.strip().split("-")]
        return len(score) == 2 and type(score[0]) == int and type(score[1]) == int
    except:
        return False

def result_to_scores(s):
    return [int(i) for i in s.strip().split("-")]

def slow_print(s, waiting):
    for c in s:
        print(c, end="", flush=True)
        time.sleep(waiting)