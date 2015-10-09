# COT 4930  Python Programming
# Name: Tyler Bourque
# ID  : tbourque2012
# Lab : 07


#-----------------------------------------
class SLNode :              # single link node

    def __init__( self, data = None, next = None ) :
        self.data = data
        self.next = next

    def get_data( self ) :
        return self.data

    def get_next( self ) :
        return self.next

    def set_next( self, next ) :
        self.next = next

class DLNode( SLNode ) :    # double link node

    def __init__( self, data = None, next = None, prev = None ) :
        super( ).__init__( data, next )
        self.prev = prev

    def get_prev( self ) :
        return self.prev

    def set_prev( self, prev ) :
        self.prev = prev


class DLList :

    def __init__( self, head = None ) :
        self.head = head
        self.tail = head

    def insert( self, data ) :
        print("Inserting ", data, " into the List...")
        
        node = DLNode( data )
        temp = self.head
        p = self.head

        if self.head == None :
            self.head = node
            self.tail = node
        else :
            while temp is not None:
                if data < self.head.get_data( ):
                    node.set_next( self.head )
                    self.head.set_prev( node )
                    self.head = node
                    temp = temp.get_next( )
                    break
                elif data > self.tail.get_data():
                    node.set_prev( self.tail )
                    self.tail.set_next( node )
                    self.tail = node
                    temp = temp.get_next( )
                    break
                else:
                    
                    if temp.get_data( ) > data:
                        node.set_next(temp)
                        p.set_next(node)
                        node.set_prev(p)
                        temp.set_prev( node )
                        break
                    else:
                        p = temp
                        temp = temp.get_next( )
                        
                    

    def remove(self, data ):
        print("Removing ", data, "from the List...")
        
        temp = self.head
        prev = None
        
        while temp is not None:
            if temp.get_data( ) == data:
                if prev is not None:
                    prev.next = temp.next
                    prev.prev = temp.prev
                else:
                    self.head = temp.next
            prev = temp
            temp = temp.next

    def print_forw( self ) :
        print( "cur\t\t prev\t\t data\t next" );

        cur = self.head
        while cur :
            print( id( cur ), "\t", id( cur.get_prev( ) ),
                              "\t", cur.get_data( ),
                              "\t", id( cur.get_next( ) ) )
            cur = cur.get_next( )
            
        print("\n\n")

    def print_back( self ) :
        print( "cur\t\t prev\t\t data\t next" );

        cur = self.tail
        while cur :
            print( id( cur ), "\t", id( cur.get_prev( ) ),
                              "\t", cur.get_data( ),
                              "\t", id( cur.get_next( ) ) )
            cur = cur.get_prev( )
            
        print("\n\n")

def main( ):
   
    DLL = DLList( )
    ifile = open( "llist.txt", "r" )
    
    for line in ifile :
        line = line.strip( )
        line = line.split( )
        command = line[0]
        
        if 'i' in command:
            key = line[1]
            DLL.insert(key)
        elif 'r' in command:
            key = line[1]
            DLL.remove(key)
        elif 'p' in command:
            DLL.print_forw()
        else:
            print("***Unknown Command***")
        
    ifile.close( )


main()