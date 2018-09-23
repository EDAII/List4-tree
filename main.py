from rb_tree import RedBlackTree, Node, BLACK, RED, NIL
NIL_LEAF = RedBlackTree.NIL_LEAF

DOT_DIAMETER = 20

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
    
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(val)
            for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            if node.val.find('None') == -1:
                t.goto(x, y)
                jumpto(x, y-12)
                t.dot(24, node.val.split(' ')[0])
                jumpto(x, y-20)
                t.color("white")
                t.write(node.val.split(' ')[1], align="center", font=('Arial', 16, 'normal'))
                t.color("black")
                draw(node.left, x-dx, y-60, dx/2)
                jumpto(x, y-20)
                draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(3); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()
    
def create_string(rb_tree, num_elementos_arr):
    # 2^altura-1
    string =  str(rb_tree.root)

    string = string + ',' + str(rb_tree.root.left) + ',' + str(rb_tree.root.right) 

    string = string + ',' + str(rb_tree.root.left.left) + ',' + str(rb_tree.root.left.right) + ',' + str(rb_tree.root.right.left) + ',' + str(rb_tree.root.right.right)

    string = string + ',' + str(rb_tree.root.left.left.left) + ',' + str(rb_tree.root.left.left.right) + ',' + str(rb_tree.root.left.right.left) + ',' + str(rb_tree.root.left.right.right) + ',' + str(rb_tree.root.right.left.left) + ',' + str(rb_tree.root.right.left.right) + ',' + str(rb_tree.root.right.right.left) + ',' + str(rb_tree.root.right.right.right)
    
    string = string + ',' + str(rb_tree.root.left.left.left.left) + ',' + str(rb_tree.root.left.left.left.right) + ',' + str(rb_tree.root.left.left.right.left) + ',' + str(rb_tree.root.left.left.right.right) + ',' + str(rb_tree.root.left.right.left.left) + ',' + str(rb_tree.root.left.right.left.right) + ',' + str(rb_tree.root.left.right.right.left) + ',' + str(rb_tree.root.left.right.right.right) + ',' + str(rb_tree.root.right.left.left.left) + ',' + str(rb_tree.root.right.left.left.right) + ',' + str(rb_tree.root.right.left.right.left) + ',' + str(rb_tree.root.right.left.right.right) + ',' + str(rb_tree.root.right.right.left.left) + ',' + str(rb_tree.root.right.right.left.right) + ',' + str(rb_tree.root.right.right.right.left) + ',' + str(rb_tree.root.right.right.right.right)

    return string

if __name__ == '__main__':

    #2,1,4,5,9,3,6,7,15
    #1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

    vals = input('Entre com os valores separados por vírgula: ')
    arr = vals.split(',')

    rb_tree = RedBlackTree()

    x = 0
    num_elementos_arr = len(arr)
    while(x < num_elementos_arr):
        rb_tree.add(arr[x])
        x+=1 

    drawtree(deserialize('[' + create_string(rb_tree, num_elementos_arr) + ']'))