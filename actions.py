# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ActionIMC(Action):
   def name(self) -> Text:
      return "IMC_action"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      w = int(tracker.get_slot("weight"))
      h = int(tracker.get_slot("height"))
      h_m = h/100

      IMC = w/(h_m*h_m)
      dispatcher.utter_message( "You have an IMC of {0:.2f}. The ideal is between 18,5 to 24,99".format(IMC))

      if IMC < 18.5:
         dispatcher.utter_message(template="utter_slim")

      elif IMC > 18.5 and IMC <= 24.99:
         dispatcher.utter_message(template="utter_perfect")

      elif IMC >= 25 and IMC <= 30:
         dispatcher.utter_message(template="utter_littlebig")

      else:
         dispatcher.utter_message(template="utter_fat")
      
      return []


class IMCForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "IMC_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["weight", "height"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        w = int(tracker.get_slot("weight"))
        h = int(tracker.get_slot("height"))
        h_m = h/100

        IMC = w/(h_m*h_m)
        dispatcher.utter_message( "You have an IMC of {0:.2f}. The ideal is between 18,5 to 24,99".format(IMC))

        if IMC < 18.5:
           dispatcher.utter_message(template="utter_slim")

        elif IMC > 18.5 and IMC <= 24.99:
           dispatcher.utter_message(template="utter_perfect")

        elif IMC >= 25 and IMC <= 30:
           dispatcher.utter_message(template="utter_littlebig")

        else:
           dispatcher.utter_message(template="utter_fat")
      
        return []
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
            """A dictionary to map required slots to
                - an extracted entity
                - intent: value pairs
                - a whole message
                or a list of them, where a first match will be picked"""

            return { "weight": [self.from_entity(entity="weight", intent="inform"), self.from_intent(intent='deny', value=False)],
                    "height": [self.from_entity(entity="height", intent="inform"), self.from_intent(intent='deny', value=False)]
            }


    def is_int(self, string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_weight(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate weight value."""

        if not self.is_int(value) or int(value) < 0 or int(value) > 300:
            dispatcher.utter_message(template="utter_wrong_num_weight")
            return {"weight": None}
        else:
            return {"weight": value}


    def validate_height(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate height value."""

        if not self.is_int(value) or int(value) < 0 or int(value) > 300:
            dispatcher.utter_message(template="utter_wrong_num_height")
            return {"height": None}
        else:
            return {"height": value}
