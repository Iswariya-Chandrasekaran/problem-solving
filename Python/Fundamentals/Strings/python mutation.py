# def mutate_string(string, position, character):
#     lst=list(string)
#     lst[position]=character
#     changed="".join(lst)
#     return changed
def mutate_string(string, position, character):
    changed = string[:position]+character+string[position+1:]
    return changed


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)