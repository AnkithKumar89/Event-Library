# Event-Library
### Eventing Library with MongoDB and Flask framework

This is a Python-based library for event handling using Flask framework and mongoDB database. It provides the functionality to register event handlers, trigger events, and remove event handlers. 

In addition, all events triggered (including off) are logged in a MongoDB database with the schema storing the event and its trigger time. The `app.log` file contains all the event logging in the format of `event --> event timestamp`. 

This library can be used for various purposes such as tracking user interactions, monitoring application performance, and more.


// Problem statement 

// Step 1: Create an 'eventing' library out of the Events class.  The Events class should have methods 'on', 'trigger', and 'off'.

// Step 2: Log the trigger events in the Mongo DB. The schema will store all events triggered (including off), the document structure would look like:
{ event :"click",
  triggerTime: timestamp 
}

//Step 3:- Print all logging in app.log file, in below pattern e.g. event --> event timestamp

//Note: You can use https://mlab.com/ to use store events in sandbox free version of mongodb or you can setup you own mongodb. 

class Events {
  
  //Register an event handler
  
    on(eventName, callback) {}

  //Trigger all callbacks associated with a given eventName
  
    trigger(eventName) {}

  //Remove all event handlers associated with the given eventName
  
    off(eventName) {}

}
