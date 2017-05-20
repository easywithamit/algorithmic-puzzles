#!/usr/bin/python
# -*- coding: utf-8 -*-
def count_chars(s):
    ch = s[0]
    c = 1
    s2 = ''
    for i in xrange(1,len(s)):
        if ch==s[i]:
            c+=1
        else:
            s2+=ch+str(c)
            ch=s[i]
            c=1
    s2 += ch + str(c)
    return s2
if __name__=='__main__':
    s = raw_input()
    print(count_chars(s))