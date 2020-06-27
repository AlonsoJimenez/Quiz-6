import unittest
loader = unittest.TestLoader()
tests = loader.discover(".")
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)

class BinaryTree:

    def __init__(self, first_element):
        self.root = Node(first_element)

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

    def delete_aux(self, front_value, back_value):
        if(front_value.right == None and front_value.left == None):
            if(back_value.right.data == front_value.data):
                back_value.right = None
            else:
                back_value.left = None
        elif(front_value.right != None and front_value.left == None ):
            if(back_value.right.data == front_value.data):
                back_value.right = front_value.right
            else:
                back_value.left = front_value.right
        elif(front_value.right == None and front_value.left != None ):
            if(back_value.right.data == front_value.data):
                back_value.right = front_value.left
            else:
                back_value.left = front_value.left
        else:
            front_value.data = self.find_min_aux(front_value.right)
            self.format_delete(self.find_min_aux(front_value.right),front_value.right, front_value )
    
    
    def format_delete(self, search_element , temp_front , temp_back ):
        if(temp_front.data == search_element):
            self.delete_aux(temp_front, temp_back)
        elif(search_element >= temp_front.data):
            self.format_delete(search_element, temp_front.right, temp_front)
        elif(temp_front.right == None and temp_front.left == None):
            print("not found")
        else:
            self.format_delete(search_element, temp_front.left, temp_front)

    def delete(self, search_element):
        self.format_delete(search_element, self.root, self.root)
        
        
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

    def print_pre_order_aux(self, temp_root):
        if(temp_root != None):
            print(temp_root.data)
            self.print_pre_order_aux(temp_root.left)
            self.print_pre_order_aux(temp_root.right)
        else:
            return
    
    def print_post_order(self):
        self.print_post_order_aux(self.root)

    def print_post_order_aux(self, temp_root ):
        if(temp_root != None):
            self.print_post_order_aux(temp_root.left)
            self.print_post_order_aux(temp_root.right)
            print(temp_root.data)
        else:
            return

    def print_order(self):
        self.print_order_aux(self.root)

    def print_order_aux(self, temp_root):
        if(temp_root != None):
            self.print_order_aux(temp_root.left)
            print(temp_root.data)
            self.print_order_aux(temp_root.right)
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


