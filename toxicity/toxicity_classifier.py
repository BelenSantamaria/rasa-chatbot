from __future__ import annotations
from typing import Any, Text, Dict, List

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.nlu.classifiers.classifier import IntentClassifier
from rasa.shared.nlu.constants import INTENT, TEXT
from rasa.shared.nlu.training_data.message import Message
import joblib


model = joblib.load(r"data\models\toxicity_model.pkl")


@DefaultV1Recipe.register(
    DefaultV1Recipe.ComponentType.INTENT_CLASSIFIER, is_trainable=False
)
class ToxicityFallbackClassifier(GraphComponent, IntentClassifier):
    def __init__(self, component_config: Dict[Text, Any]) -> None:
        self.component_config = component_config

    @classmethod
    def create(
            cls,
            config: Dict[Text, Any],
            model_storage: ModelStorage,
            resource: Resource,
            execution_context: ExecutionContext,
    ) -> ToxicityFallbackClassifier:
        return cls(config)

    @staticmethod
    def is_toxic(
        message: Message
    ) -> bool:
        text = message.get(TEXT)
        if model.predict([text]) == ['toxico']:
            return True

    def process(self, messages: List[Message]) -> List[Message]:
        for message in messages:
            toxicity = self.is_toxic(message)
            if toxicity:
                message.data[INTENT] = {
                    "name": 'toxico',
                    "confidence": 1,
                }
        return messages
