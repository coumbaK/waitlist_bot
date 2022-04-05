import os
from twilio.rest import Client
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))

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
    def __init__ (self ,id, name ,  phone , sms_content) :
        self.id = id
        self.name = name
        self.phone = phone
        self.sms = sms_content
        
class sms_system :
    #starts by initializing a dictionary of queues stored with the type as key 
    def __init__(self):
        self.queue = myqueue()
        
    
    def add_person(self, id , name , phone , sms)   :
        they = person(id, name, phone , sms )
        self.queue.enqueue( they)
            
    def send_sms(self, person ) :
        account_sid = "AC8fc71d27854fc7587d71c70b421610d5"
        auth_token = "c743187bbc93a749cec98ab3c1d506f6"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=person.phone,
            from_='+18787897833',
            body= person.sms)
        print(message.sid)

    def update_queue (self) :
          try :
                next_person = self.queue.dequeue()
                self.send_sms(next_person)

          except : 
                print ('queue is empty')
    def queue_to_list (self) :
        list_of_people = []
        current_node = self.queue.head
        while current_node != None :
            list_of_people.append(current_node.data)
            current_node = current_node.next
        return list_of_people
         
                
@app.route("/" , methods=["GET", "POST"])

def view_index() :
    if request.method == "POST" :
       sms.add_person(request.form["id"], request.form["name"], request.form["phone"] , request.form["sms_content"])
    elif request.method == "GET" :
        sms.update_queue()
    return render_template("index.html", queue=sms.queue_to_list())
        
                


if __name__ == "__main__":
    
    sms = sms_system()
    app.run(debug=True)
    
        
    
    



