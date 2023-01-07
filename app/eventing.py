import datetime 
from app import custome_event_collection,logging

class CustomEvents:
    def __init__(self):
        self.registeredEvent={}
        self.logger = logging.getLogger(__name__)
    
    def on(self,eventName,callback):
        if not eventName in self.registeredEvent:
            self.registeredEvent[eventName]=[]
        self.registeredEvent[eventName].append(callback)
        if callback in self.registeredEvent[eventName]:
            self.logger.info(f"On_event --> {eventName} {callback} {datetime.datetime.now()}")
    
    def trigger(self,eventName):
        if eventName in self.registeredEvent:
            event_schema={
                "eventName":eventName,
                "triggerTime":datetime.datetime.now()
            }
            custome_event_collection.insert_one(event_schema)   
            self.logger.info(f"Trigger_event --> {eventName} {self.registeredEvent[eventName]} {event_schema['triggerTime']}")
    
    def off(self,eventName):
        if eventName in self.registeredEvent:
            del  self.registeredEvent[eventName]
            event_schema={
                "eventName":eventName,
                "offTime":datetime.datetime.now()
            }
            custome_event_collection.insert_one(event_schema)
            self.logger.info(f"Off_event --> {eventName} {event_schema['offTime']}")
