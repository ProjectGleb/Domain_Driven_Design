from dataclasses import dataclass
@dataclass
class Car:
    wheels: int
    color: str
    brand:str
    on_sale:bool


ferrari = Car(wheels=4, color="red", brand="Ferrari", on_sale=False)
print(ferrari)
