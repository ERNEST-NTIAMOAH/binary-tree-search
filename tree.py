import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


def inorderprint(r):
    if r is None:
        return
    else:
        inorderprint(r.left)
        print(r.data,end=' ')
        inorderprint(r.right)
        
def preorderpdrint(r):
    if r is None :
        return 
    else:
        
        print(r.data,end='')
        preorderpdrint(r.left)
        preorderpdrint (r.right)

def postorderprint(r):
    if r is None:
      return 
    else:
         postorderprint(r.left)
     
         postorderprint(r.right)
         print(r.data,end='')
         
         import matplotlib.pyplot as plt

def draw_tree():
    nodes = {
        'g': (0, 0),
        'c': (-2, -1),
        'i': (2, -1),
        'b': (-3, -2),
        'e': (-1, -3),
        'h': (1, -2),
        'j': (3, -2),
        'a': (-3.5, -3),
        'd': (-1.5, -3),
        'f': (-0.5, -3),
        'k': (3.5, -3)
    }

    edges = [
        ('g','c'), ('g','i'),
        ('c','b'), ('c','e'),
        ('i','h'), ('i','j'),
        ('b','a'),
        ('e','d'), ('e','f'),
        ('j','k')
    ]

    for a, b in edges:
        x1, y1 = nodes[a]
        x2, y2 = nodes[b]
        plt.plot([x1, x2], [y1, y2])

    for label, (x, y) in nodes.items():
        plt.text(x, y, label, fontsize=12)

    plt.axis('off')
    plt.show()
     
      
if __name__ == "__main__":
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')
    
    postorderprint(root)
    draw_tree()
