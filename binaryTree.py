import unittest
loader = unittest.TestLoader()
tests = loader.discover(".")
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)

class BinaryTree:

    def __init__(self, firstElement):
        self.root = Node(firstElement)

    def find_max(self):
        return self.find_max_aux(self.root)
    
    def find_max_aux(self, temp ):
        if(temp.left == None and temp.right == None):
            return temp.data
        else:
            return self.find_max_aux(temp.right)

    def find_min(self):
        return self.find_min_aux(self.root)

    def find_min_aux(self, temp):
        if(temp.left== None ):
            return temp.data
        else:
            return self.find_min_aux(temp.left)

    def delete_aux(self, frontValue, backValue):
        if(frontValue.right == None and frontValue.left == None):
            if(backValue.right.data == frontValue.data):
                backValue.right = None
            else:
                backValue.left = None
        elif(frontValue.right != None and frontValue.left == None ):
            if(backValue.right.data == frontValue.data):
                backValue.right = frontValue.right
            else:
                backValue.left = frontValue.right
        elif(frontValue.right == None and frontValue.left != None ):
            if(backValue.right.data == frontValue.data):
                backValue.right = frontValue.left
            else:
                backValue.left = frontValue.left
        else:
            frontValue.data = self.find_min_aux(frontValue.right)
            self.format_delete(self.find_min_aux(frontValue.right),frontValue.right, frontValue )
    
    
    def format_delete(self, searchElement , tempFront , tempBack ):
        if(tempFront.data == searchElement):
            self.delete_aux(tempFront, tempBack)
        elif(searchElement >= tempFront.data):
            self.format_delete(searchElement, tempFront.right, tempFront)
        elif(tempFront.right == None and tempFront.left == None):
            print("not found")
        else:
            self.format_delete(searchElement, tempFront.left, tempFront)

    def delete(self, searchElement):
        self.format_delete(searchElement, self.root, self.root)
        
        
    def insert(self, element):
        self.insert_aux(element, self.root)

    def insert_aux(self, element, temp):
        if(element >= temp.data ):
            if(temp.right == None):
                temp.right = Node(element)
            else:
                self.insert_aux(element, temp.right)
        elif(element < temp.data):
            if(temp.left == None):
                temp.left = Node(element)
            else:
                self.insert_aux(element, temp.left)
     
    def print_pre_order(self):
        self.print_pre_order_aux(self.root)

    def print_pre_order_aux(self, tempRoot):
        if(tempRoot != None):
            print(tempRoot.data)
            self.print_pre_order_aux(tempRoot.left)
            self.print_pre_order_aux(tempRoot.right)
        else:
            return
    
    def print_post_order(self):
        self.print_post_order_aux(self.root)

    def print_post_order_aux(self, tempRoot ):
        if(tempRoot != None):
            self.print_post_order_aux(tempRoot.left)
            self.print_post_order_aux(tempRoot.right)
            print(tempRoot.data)
        else:
            return

    def print_order(self):
        self.print_order_aux(self.root)

    def print_order_aux(self, tempRoot):
        if(tempRoot != None):
            self.print_order_aux(tempRoot.left)
            print(tempRoot.data)
            self.print_order_aux(tempRoot.right)
        else:
            return

    

        





class Node:
    def __init__(self, data = None, right = None, left = None):
        self.left = left
        self.right = right
        self.data = data    
        



class TestRoot(unittest.TestCase):
    def test_sum(self):
        tree = BinaryTree(5)
        tree.insert(2)
        tree.insert(10)
        tree.insert(1)
        tree.insert(3)
        tree.insert(7)
        tree.insert(11)
        tree.print_order()
        tree.print_pre_order()
        tree.print_post_order()
        self.assertEqual(tree.find_min(), 1)
        self.assertEqual(tree.find_max(), 11)
        self.assertEqual(tree.root.right.data, 10)
        tree.delete(10)
        self.assertEqual(tree.root.right.data, 11)
        tree.delete(1)
        self.assertEqual(tree.find_min(), 2)
        tree.delete(11)
        self.assertEqual(tree.root.right.data, 7)
        self.assertEqual(tree.find_max(), 7)
        tree.delete(3)
        self.assertEqual(tree.root.left.right, None)
        tree.delete(6)
        self.assertEqual(tree.root.right.left, None)
        tree.insert(11)
        tree.insert(1)
        self.assertEqual(tree.find_max(), 11)
        self.assertEqual(tree.find_min(), 1)
        
        

        
        

if __name__ == '__main__':
    unittest.main()


