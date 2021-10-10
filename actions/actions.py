from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import AllSlotsReset
from actions.database import MyMongoDB as md
import math

class ActionSearchPlaces(Action):
    def name(self) -> Text:
        return "search_places"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        x = tracker.get_slot("city_lookup")
        print(x)
        if x:
            res = md.find_random(md.PLACES,9)
            c = 0
            for i in res:
                c+=1
                dispatcher.utter_template("utter_place_info",tracker,image_url=str(i['image_link']),title=str(i['title']),description=str(i['Desc']),distance=str(i['distance']),link=str(i['link']))
        else:
            dispatcher.utter_message(text = str(f"Sorry... We are working for {x}"))
        return []

class ValidatHotelForm(FormValidationAction):
    hotel_values = {}
    def name(self) -> Text:
        return "validate_hotel_form"

    def validate_hotel_place(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `hotel_place` value."""
        
        print(f"City = {slot_value} length = {len(slot_value)}")
        self.hotel_values.update({"hotel_place": slot_value})
        return {"hotel_place": slot_value}
    
    def validate_hotel_start_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `hotel_start_date` value."""
        
        print(f"hotel_start_date = {slot_value} length = {len(slot_value)}")
        self.hotel_values.update({"hotel_start_date": slot_value})
        return {"hotel_start_date": slot_value}
    
    def validate_hotel_duration(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `hotel_duration` value."""
        
        print(f"hotel_duration = {slot_value} length = {len(slot_value)}")
        self.hotel_values.update({"hotel_duration": slot_value})
        return {"hotel_duration": slot_value}
    
    def validate_hotel_people(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `hotel_people` value."""
        
        print(f"hotel_people = {slot_value} length = {len(slot_value)}")
        self.hotel_values.update({"hotel_people": slot_value})
        return {"hotel_people": slot_value}
    
    def validate_hotel_budget(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `hotel_budget` value."""
        
        print(f"hotel_budget = {slot_value} length = {len(slot_value)}")
        self.hotel_values.update({"hotel_budget": slot_value})
        return {"hotel_budget": slot_value}
    

class ValidateBusForm(FormValidationAction):
    bus_values = {}
    def name(self) -> Text:
        return "validate_bus_form"

    def validate_bus_source(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `bus_source` value."""
        
        print(f"City = {slot_value} length = {len(slot_value)}")
        self.bus_values.update({"bus_source": slot_value})
        return {"bus_source": slot_value}
    
    def validate_bus_destination(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `bus_destination` value."""
        
        print(f"bus_destination = {slot_value} length = {len(slot_value)}")
        self.bus_values.update({"bus_destination": slot_value})
        return {"bus_destination": slot_value}
    
    def validate_bus_start_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `bus_start_date` value."""
        
        print(f"bus_start_date = {slot_value} length = {len(slot_value)}")
        self.bus_values.update({"bus_start_date": slot_value})
        return {"bus_start_date": slot_value}
    
    
    
class ActionSubmitHotel(Action):
    userData ={}
    def name(self) -> Text:
        return "action_submit_hotel"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        vh = ValidatHotelForm();
        print(vh.hotel_values)
        x = vh.hotel_values['hotel_place']
        print(x)
        res = md.find_document(md.HOTEL,{'search':x.lower()})
        if(res.count() == 0 ):
            placeList = ["panchgani","lonavala","mahabaleshwar","alibag","pune"]
            dispatcher.utter_message(text = str(f"I'm unable to find hotels in {x}."))
            dispatcher.utter_message(text = str(f"search hotels in following city {placeList}."))
        else:
            for i in res:
                dispatcher.utter_template("utter_hotel_info",tracker,image=str(i['image']),title=str(i['title']),rating=str(i['rating']),
                                          type=str(i['type']),room=str(i['room']),
                                          price=str(i['price']),canc=str(i['canc']),
                                          off=str(i['off']),location=str(i['location']))
        return [AllSlotsReset()]
    
    
class ActionSubmitHotel(Action):
    userData ={}
    def name(self) -> Text:
        return "action_submit_bus"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        vh = ValidateBusForm();
        print(vh.bus_values)
        x = vh.bus_values['bus_source'].lower()
        y = vh.bus_values['bus_destination'].lower()
        z = vh.bus_values['bus_start_date'].lower()
        
        print(x,y,z)
        data = md.findbus(x,y,z)
        if data == None:
            dispatcher.utter_message(text = str(f"I'm unable to find buses from {x} to {y}."))
        else:
            try:
                c = int(0)
                for i in range(5):
                    m = data['inv'][int(c)]
                    hour = math.floor((m['dur']/60)*100)/100
                    dispatcher.utter_template("utter_bus_info",tracker,bus=str(m['Tvs']),
                                                bus_type=str(m['bt']),
                                                bus_station=str(m['sn']),
                                                bus_fair=str(m['minfr']),
                                                bus_dur=str(f"{str(hour)},hrs"))
                    c+=1
            except:
                dispatcher.utter_message(text = str(f"I'm unable to find buses from {x} to {y}."))
        return [AllSlotsReset()]



