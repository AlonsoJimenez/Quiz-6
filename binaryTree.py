import unittest
loader = unittest.TestLoader()
tests = loader.discover(".")
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)

class binaryTree:

    def __init__(self, firstElement):
        self.root = node(firstElement)

    def findMax(self):
        return self.findMaxAux(self.root)
    
    def findMaxAux(self, temp ):
        if(temp.left == None and temp.right == None):
            return temp.data
        else:
            return self.findMaxAux(temp.right)

    def findMin(self):
        return self.findMinAux(self.root)

    def findMinAux(self, temp):
        if(temp.left== None ):
            return temp.data
        else:
            return self.findMinAux(temp.left)

    def deleteAux(self, frontValue, backValue):
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
            frontValue.data = self.findMinAux(frontValue.right)
            self.deleteAux2(self.findMinAux(frontValue.right),frontValue.right, frontValue )
    
    
    def deleteAux2(self, searchElement , tempFront , tempBack ):
        if(tempFront.data == searchElement):
            self.deleteAux(tempFront, tempBack)
        elif(searchElement >= tempFront.data):
            self.deleteAux2(searchElement, tempFront.right, tempFront)
        elif(tempFront.right == None and tempFront.left == None):
            print("not found")
        else:
            self.deleteAux2(searchElement, tempFront.left, tempFront)

    def delete(self, searchElement):
        self.deleteAux2(searchElement, self.root, self.root)
        
        
    def insert(self, element):
        self.insertAux(element, self.root)

    def insertAux(self, element, temp):
        if(element >= temp.data ):
            if(temp.right == None):
                temp.right = node(element)
            else:
                self.insertAux(element, temp.right)
        elif(element < temp.data):
            if(temp.left == None):
                temp.left = node(element)
            else:
                self.insertAux(element, temp.left)
     
    def printPreOrder(self):
        self.printPreOrderAux(self.root)

    def printPreOrderAux(self, tempRoot):
        if(tempRoot != None):
            print(tempRoot.data)
            self.printPreOrderAux(tempRoot.left)
            self.printPreOrderAux(tempRoot.right)
        else:
            return
    
    def printPostOrder(self):
        self.printPostOrderAux(self.root)

    def printPostOrderAux(self, tempRoot ):
        if(tempRoot != None):
            self.printPostOrderAux(tempRoot.left)
            self.printPostOrderAux(tempRoot.right)
            print(tempRoot.data)
        else:
            return

    def printOrder(self):
        self.printOrderAux(self.root)

    def printOrderAux(self, tempRoot):
        if(tempRoot != None):
            self.printOrderAux(tempRoot.left)
            print(tempRoot.data)
            self.printOrderAux(tempRoot.right)
        else:
            return

    

        





class node:
    def __init__(self, data = None, right = None, left = None):
        self.left = left
        self.right = right
        self.data = data    
        



class TestRoot(unittest.TestCase):
    def test_sum(self):
        tree = binaryTree(5)
        tree.insert(2)
        tree.insert(10)
        tree.insert(1)
        tree.insert(3)
        tree.insert(7)
        tree.insert(11)
        tree.printOrder()
        tree.printPreOrder()
        tree.printPostOrder()
        self.assertEqual(tree.findMin(), 1)
        self.assertEqual(tree.findMax(), 11)
        self.assertEqual(tree.root.right.data, 10)
        tree.delete(10)
        self.assertEqual(tree.root.right.data, 11)
        tree.delete(1)
        self.assertEqual(tree.findMin(), 2)
        tree.delete(11)
        self.assertEqual(tree.root.right.data, 7)
        self.assertEqual(tree.findMax(), 7)
        tree.delete(3)
        self.assertEqual(tree.root.left.right, None)
        tree.delete(6)
        self.assertEqual(tree.root.right.left, None)
        tree.insert(11)
        tree.insert(1)
        self.assertEqual(tree.findMax(), 11)
        self.assertEqual(tree.findMin(), 1)
        
        

        
        

if __name__ == '__main__':
    unittest.main()


