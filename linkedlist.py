class node:
    def __init__(self,data=0,next_node=None):
        self.data=data
        self.next_node=next_node

class root:
    
    last_node=None
    def __init__(self):
        self.no_nodes=0
        self.last_node=self
        self.next_node=None

    def insert(self,data):
        self.last_node.next_node=node(data)

    def delete_node(self):
        if self.next_node==None:
            print("List empty")
        p=self

        while p.next_node!=None:
            q=p
            p=p.next_node
        else:
            print(f"{p.data}Is deleted")
            q.next_node=None

    def display_list(self):
         p=self.next_node
         while p.next_node!=None:
             print(p.data)
             p=p.next_node
         else:
            print("List terminated")


s=root()
s.insert(1)
s.insert(2)
input("|")

s.display_list()
input("|")
s.delete_node()
input("|")
s.display_list()
input("|")
s.delete_node()
input("|")
s.display_list()




        



    




