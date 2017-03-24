def number_needed(a, b):
    l1 = len(a)
    l2 = len(b)
    if l1==0 or l2==0:
        return 0
    s1 = sorted(a)
    s2 = sorted(b)
    i=j=counter=0
    while i<l1 and j<l2:
        if s1[i]<s2[j]:
            i+=1
            counter+=1
        elif s1[i]>s2[j]:
            j+=1
            counter+=1
        else:
            i+=1
            j+=1
    if i!=l1:
        counter+=(l1-i)
    if j!=l2:
        counter+=(l2-j)
    return counter

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
