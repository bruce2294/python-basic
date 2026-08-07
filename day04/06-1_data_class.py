from dataclasses import dataclass, replace

@dataclass
class Student:
    name: str
    age: int
    score: float

s1 = Student("철수", 20, 85.5)
s2 = replace(s1, age=21)

print(s1, s2, sep="; ")
