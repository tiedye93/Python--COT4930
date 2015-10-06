# COT 4930  Python Programming
# Name: Tyler Bourque
# ID  : tbourque2012
# Lab : 06


#-----------------------------------------
class Node :

    def __init__( self, data = None, next_node = None ) :
        self.data = data
        self.next_node = next_node

    def get_data( self ) :
        return self.data

    def get_next( self ) :
        return self.next_node

    def set_next( self, new_next ) :
        self.next_node = new_next


class List :

    def __init__( self, head = None ) :
        self.head = head
        self.tail = head

    def insert( self, data ) :
        print("Inserting ", data, " into the List...")
        
        new_node = Node( data )
        temp = self.head
        prev = self.head
        
        if self.head == None :
            self.head = new_node
            self.tail = new_node
        else :
            while temp is not None:
                if data < self.head.get_data( ):
                    new_node.set_next( self.head )
                    self.head = new_node
                    temp = temp.get_next( )
                    break
                elif data > self.tail.get_data():
                    self.tail.set_next( new_node )
                    self.tail = new_node
                    temp = temp.get_next( )
                    break
                else:
                    
                    if temp.get_data( ) > data:
                        new_node.set_next(temp)
                        prev.set_next(new_node)
                        break
                    else:
                        temp = temp.get_next( )
                        
                    if prev.get_next( ) != temp:
                        prev = prev.get_next()
                        print("temp: ", temp.get_data())
                        print("prev: ", prev.get_data())
                        
   
    def remove(self, data ):
        print("Removing ", data, "from the List...")
        
        temp = self.head
        prev = None
        
        while temp is not None:
            if temp.get_data( ) == data:
                if prev is not None:
                    prev.next_node = temp.next_node
                else:
                    self.head = temp.next_node
            prev = temp
            temp = temp.next_node
   
    def print( self ) :
        print("Printing List...")
        
        cur = self.head

        while cur is not None :
            print( id( cur ), "\t", cur.get_data( ),
                              "\t", id( cur.get_next( ) ) )
            cur = cur.get_next( )
        
        print("\n\n")    
def main( ):
   
    SLL = List( )
    ifile = open( "llist.txt", "r" )
    
    for line in ifile :
        line = line.strip( )
        line = line.split( )
        command = line[0]
        
        if 'i' in command:
            key = line[1]
            SLL.insert(key)
        elif 'r' in command:
            key = line[1]
            SLL.remove(key)
        elif 'p' in command:
            SLL.print()
        else:
            print("***Unknown Command***")
        
    ifile.close( )


main()