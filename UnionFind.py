class UnionFind:

    def __init__(self, size):
        self.id = [i for i in range(size)]
        self.sz = [1]*size
        self.numComponents = size
    
    def find(self, p):
        # find + path compression
        while p != self.id[p]:
            # set next to grandparent, note how if its already root nothing changes
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p
        
        # below is verbose method of find + path compression
        
        # find the root
        # root = p
        # while root != self.id[root]:
        #     root = self.id[root]
        
        # # path compression
        # while p != root:
        #     next = self.id[p]
        #     self.id[p] = root
        #     p = next
        # return root
    
    def union(self, p, q):
        # find p and q and union their sets
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            if self.sz[root_p] >= self.sz[root_q]:
                self.sz[root_p] += self.sz[root_q]
                self.id[root_q] = root_p
            else:
                self.sz[root_q] += self.sz[root_p]
                self.id[root_p] = root_q
            self.numComponents-=1
    
    def isConnected(self, p, q):
        return self.find(p) == self.find(q)
    


def main():
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(6, 7)
    uf.union(5, 6)
    print(uf.find(3)) # should print 1
    print(uf.isConnected(3,6)) # should print false
    print(uf.isConnected(1,3)) # should print true

if __name__ == "__main__":
    main()




        
        

        
