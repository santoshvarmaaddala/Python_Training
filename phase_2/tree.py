class node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self) -> None:
        self.root = node(-105)
        self.obj1 = node(10)
        self.obj2 = node(20)
        self.obj3 = node(30)
        self.obj4 = node(40)
        self.obj5 = node(50)

    def getRoot(self):
        return self.root

    def initialize(self):
        self.root.left = self.obj1
        self.root.right = self.obj2
        self.obj1.left = self.obj3
        self.obj1.right = self.obj4
        self.obj2.left = self.obj5

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)

    def preorder(self,root):  
        if root == None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self,root):
        if root == None:
            return
        self.preorder(root.left)
        self.preorder(root.right)
        print(root.data,end=" ")


    def layerordertraversal(self,root):
        if not root:
            return 
        q = [root]
        res = []
        while len(q) != 0:
            sub = []
            n = len(q)
            for i in range(n):
                curr = q.pop(0)
                sub.append(curr.data)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(sub)
        print(res)




t = tree()
t.initialize()
t.inorder(t.getRoot())
print()
t.preorder(t.getRoot())
print()
t.postorder(t.getRoot())
print()
t.layerordertraversal(t.getRoot())