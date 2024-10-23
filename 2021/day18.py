import aocd
class Heap:
    def __init__(self,v):
        self.v=v
        self.l=None
        self.r=None
        self.p=None


def build_heap(d):
    if type(d)==int:
        return Heap(d)
    current = Heap(None)
    l,r = d
    l,r = build_heap(l),build_heap(r)
    l.p=current
    r.p=current
    current.l=l
    current.r=r
    return current



def depth(heap,c):
    if type(heap.v)==int:
        return c
    else:
        return max(depth(heap.l,c+1),depth(heap.r,c+1))



def add_to_dir(heap,child,f,direction="left"):
    if child == None:
        return add_to_dir(heap.p,heap,f,direction)
    if direction=="left":
        q = heap.l
    else:
        q = heap.r
    if q!=None and q!=child:
        if direction=="left":
            while q.v==None:
                q=q.r
            
        else:
            while q.v==None:
                q=q.l
        assert q.v!=None, f"{print_heap(heap)} {direction}"
        q.v+=f
        return
    if heap.p==None:
        return
    add_to_dir(heap.p,heap,f,direction)


def explode(heap,c):
    if type(heap.v)==int:
        return False
    
    if c<4:
        if explode(heap.l,c+1):
            return True
        if explode(heap.r,c+1):
            return True
        return False
    add_to_dir(heap,None,heap.l.v,"left")
    add_to_dir(heap,None,heap.r.v,"right")
    heap.l.p=None
    heap.r.p=None
    heap.l=None
    heap.r=None
    heap.v = 0
    return True



def print_heap(heap):
    if type(heap.v)==int:
        return heap.v
    return [print_heap(heap.l),print_heap(heap.r)]




def split(heap):
    if type(heap.v)==int:
        if heap.v>9:
            lv,rv = heap.v//2, heap.v//2 + heap.v%2
            heap.v = None
            heap.l=Heap(lv)        
            heap.r=Heap(rv)
            heap.r.p=heap
            heap.l.p=heap
            return True
    else:
        if heap.l!=None:
            if split(heap.l):
                return True
        if heap.r!=None:
            if split(heap.r):
                return True
    return False



def add(a,b):
    head = Heap(None)
    head.l=a
    head.r=b
    head.r.p=head
    head.l.p=head
    while True:
        change = False
        assert depth(head,0)<6, f"{print_heap(head)}\n{print_heap(a)} + {print_heap(b)} "
        while explode(head,0):
            change = True
        split_change = False
        while split(head):
            split_change=True
            break
        if split_change:
            continue
        if not(change):
            break
    return head



print_heap(add(build_heap([[[[4,3],4],4],[7,[[8,4],9]]]),build_heap([1,1])))==[[[[0,7],4],[[7,8],[6,0]]],[8,1]]


s = aocd.get_data(day=18,year=2021).splitlines()
s=[build_heap(eval(b)) for b in s]



while len(s)>1:
    k = s.pop(1)
    s[0] = add(s[0],k)
print_heap(s[0])



def mag(heap):
    if type(heap.v)==int:
        return heap.v
    return 3*mag(heap.l)+2*mag(heap.r)




print(mag(s[0]))


s = [eval(b) for b in aocd.get_data(day=18,year=2021).splitlines()]
v = 0
for b in s:
    for c in s:
         v=max(v,mag(add(build_heap(b),build_heap(c))))
print(v)

