class Node:
    def __init__(self):
        self.is_word = False
        self.count = 0
        self.child = dict()
class Contact():
    def __init__(self):
        self.root = Node()
    def add(self,word):
        if not word:
            return
        current = self.root
        for letter in word:
            current.count += 1
            if letter not in current.child:
                current.child[letter]=Node()
            current = current.child[letter]
        current.is_word = True
    def find(self,prefix):
        if not prefix:
            print 0
        current = self.root
        for letter in prefix:
            try:
                current = current.child[letter]
            except Exception as e:
                print 0
                return
        counter = current.count
        print counter
    
if __name__=='__main__':
    n = int(raw_input().strip())
    c = Contact()
    for a0 in xrange(n):
        op, contact = raw_input().strip().split()
        getattr(c, op)(contact)
