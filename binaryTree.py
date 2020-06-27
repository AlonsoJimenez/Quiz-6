class binaryTree:

    def __init__(self, firstElement):
        self.root = node(firstElement)

    def findMax(temp = root):
        if(temp.left == None and temp.right == None):
            return temp
        else:
            return self.findMax(temp.right)

    def findMin(temp = root):
        if(temp.left == None and temp.right == None):
            return temp
        else:
            return self.findMin(temp.left)

    def deleteAux(frontValue, backValue):
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
            frontValue.data = self.findMin(frontValue.right)
            delete(self.findMin(frontValue.right), frontValue, frontValue)
    
    
    def delete(searchElement , tempFront = root, tempBack = root):
        if(tempFront.data == searchElement):
            deleteAux(tempFront, tempBack)
        elif(searchElement >= tempFront.data):
            self.delete(searchElement, tempFront.right, tempFront)
        elif:
            self.delete(searchElement, tempFront.left, tempFront)
        else(tempFront.right == None and tempFront.left == None):
            print("not found")
        


    def insert(element, temp = self.root):
                
        if(element >= temp.data ):
            if(temp.right == None)
                temp.right = node(element)
            else:
                self.insert(element, temp.right)
        elif(element < temp.data):
            if(temp.left == None)
                temp.left = node(element)
            else:
                self.insert(element, temp.left)
    
    def

    



class node:
    

    def __init__(self, data = None, right = None, left = None):
        self.left = left
        self.right = right
        self.data = data

   

