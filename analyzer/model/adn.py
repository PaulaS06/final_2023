from abc import ABC, abstractmethod
from dataclasses import dataclass


class Condition (ABC):
    @abstractmethod
    def evaluate(self, sequence: str) -> bool:
        pass


class ADNAnalyzer:
    def __init__(self, sequence: str, conditions: list, data_file):
        self.conditions: list = conditions
        self.data_file = data_file
        self.sequence:str = sequence
        self.valid_bases: list = []

        pass

    def add_condition(self, condition: Condition):
        self.conditions.append(condition)

    @staticmethod
    def _validate_sequence(self, sequence: str) -> bool:
        valid_bases = ["A", "T", "C", "G"]
        for bases in sequence:
            if bases not in valid_bases:
                return True
            else:
                return False

    def _evaluate_conditions(self, sequence: str) -> str:
        if self.LengthCondition(sequence):
            pass
        raise ValueError('El archivo contiene secuencias inválidas')

    def analyze(self) -> dict:
        pass


class LengthCondition (Condition):
    def __init__(self, min_length: int = 50):
        self.min_length = min_length
        super().__init__()

    def evaluate(self, sequence: str) -> bool:
        len(sequence) > self.min_length
        return True


class GCContentCondition (Condition):
    def __init__(self, min_gc_content:  float = 60):
        self.min_gc_content = min_gc_content
        super().__init__()

    def evaluate(self, sequence: str) -> bool:
        pass


class ATGPresenceCondition (Condition):
    def __init__(self):
        super().__init__()

    def evaluate(self, sequence: str) -> bool:
        if "ATG" in sequence:
            return True


class CTAPresenceCondition (Condition):

    def __init__(self):
        super().__init__()

    def evaluate(self, sequence: str) -> bool:
        if sequence.count("CTA") >= 3:
            return True