import os
from twilio.rest import Client
class _node:
    def __init__(self, data):
        self.data = data
        self.next = None

#queue implementation 
class myqueue () :
    global head 
    global tail
   
    
    
    

    #initializes an empty queue 
    def __init__(self ) :
        self.head = None
        self.tail = None
        
        
    # adds person the queue    
    def enqueue(self, person) :
        if self.is_empty() :
            self.head = _node(person)
            self.tail = self.head
            
        else : 
            new_node = _node(person)
            self.tail.next = new_node
            self.tail = new_node
            
            
            
            
    # removes the top of the queue    
    def dequeue(self) :
        if self.is_empty() :
            print ('nothing to dequeue')
            
        
        else : 
            d_node = self.head
            self.head= d_node.next
            if self.head == None :
                self.tail = None
        return d_node.data
    #check if queue is empy
    def is_empty (self) :
        return self.head == None 
           


        

class person : 
    def __init__ (self ,id, name ,  phone) :
        self.id = id
        self.name = name
        self.phone = phone
        
class sms_system :
    #starts by initializing a dictionary of queues stored with the type as key 
    def __init__(self):
        self.queue = myqueue()
        
    
    def add_person(self,name, id, phone , request ) :
        patron_ = patron (id ,phone , request)
        self.queues[request].enqueue(patron_)
            
    def send_sms(self, patron_) :
        account_sid = "AC8fc71d27854fc7587d71c70b421610d5"
        auth_token = "44060ae9b4ae6e33964c0701b6f41dbd"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=patron_.phone,
            from_='+17692468375',
            body='Your item is ready for pickup at the library desk')
        print(message.sid)

    def update_queue (self) :
          try
                next_patron = self.queue.dequeue()
                self.send_sms(next_patron)
            except :
                print ('no patrons on the waitlist')
                
    
        
                


if __name__ == "__main__":
    
        
    
    



