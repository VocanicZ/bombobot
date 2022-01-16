def extract(lst):
        tmp = lst[0]
        del lst[0]
        return tmp

def min(lst):
        lst.sort()
        cost = 0
        for _ in range(len(lst)-1):
                total = extract(lst) + extract(lst)
                cost += total
                lst.append(total)
                lst.sort()
        return cost

data = [int(i) for i in input().split()]
print(min(data))