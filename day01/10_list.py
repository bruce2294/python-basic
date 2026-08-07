fruits = ["사과", "바나나", "체리", "포도", "딸기"]
item = input("과일 이름을 입력하세요: ")
def check_fruit(item):
    return "있습니다." if item in fruits else "없습니다."

result = f"{check_fruit(item)}"
print(f"결과: {item}은(는) 과일 목록에 {result}")