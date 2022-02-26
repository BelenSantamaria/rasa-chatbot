from typing import Text, List, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, SlotSet
import json

with open(r"data\external\info_grados.json") as f:
    INFO_GRADO = json.load(f)


class InformacionGradoAction(Action):
    def name(self) -> Text:
        return "action_informacion_grado"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        if tracker.get_slot("grado") in INFO_GRADO:
            web_grado = INFO_GRADO[tracker.get_slot("grado").lower()]
            dispatcher.utter_message(
                f"Toda la información la podrás encontrar en la siguiente página web de la UV: {web_grado}"
            )
        else:
            web_grado = INFO_GRADO["informacion_general"]
            dispatcher.utter_message(
                f"Puedes consultar los grados que ofrece la Universitat de València en el siguiente enlace: {web_grado}"
            )
        return [SlotSet("grado", None)]
