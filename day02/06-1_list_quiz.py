quiz_1 = """
퀴즈1. 빈 리스트 colors를 만들고, "빨강", "초록", "파랑"을 순서대로 append()로 추가한 뒤 출력하세요.
"""
print(quiz_1)
colors = []
colors.append("빨강")
colors.append("초록")
colors.append("파랑")
print(f"append after colors: {colors}")

quiz_2 = """
퀴즈2. 리스트 numbers = [1, 2, 3, 4, 5]에서 모든 값을 더한 합계를 for문으로 구해서 출력하세요.
"""
print(quiz_2)
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print(f"sum numbers: {sum}")

quiz_3 = """
퀴즈3. 리스트 fruits = ["사과", "바나나", "포도", "딸기"]에서 "바나나"를 삭제하고 결과를 출력하세요.
"""
fruits = ["사과", "바나나", "포도", "딸기"]
fruits.remove("바나나")
print(f"remove 바나나 after fruits: {fruits}")

quiz_4 = """
퀴즈4. 리스트 scores = [70, 85, 90, 60, 95]를 내림차순으로 정렬해서 출력하세요.
"""
print(quiz_4)
scores = [70, 85, 90, 60, 95]
print(f"내림차순 scores: {sorted(scores, reverse=1)}")

quiz_5 = """
퀴즈5. 리스트 numbers = [1, 2, 3, 4, 5, 6]에서 짝수만 골라 새로운 리스트 even_numbers에 담아 출력하세요. (for문 + if문 활용)
"""
print(quiz_5)
numbers = list(range(1, 7))
print(f"numbers: {numbers}")
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(f"even_numbers: {even_numbers}")
