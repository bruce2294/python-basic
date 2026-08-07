# pip install pandas matplotlib seaborn openpyxl

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ---------------------------------------------------------
# 1. 데이터 불러오기 및 전처리 (Data Cleaning)
# ---------------------------------------------------------
print("\n--- [데이터 불러오기 및 전처리] ---")
df = pd.read_csv("customers.csv")

print("--- [열별 결측치 개수] ---")
print(df.isnull().sum())
print("-" * 30)

# 1) 나이 결측치 -> 평균 나이로 채우기 (반올림 정수)
mean_age = round(df["나이"].mean())
df["나이"] = df["나이"].fillna(mean_age).astype(int)

# 2) 연락처 결측치 -> "정보없음"으로 채우기
df["연락처"] = df["연락처"].fillna("정보없음")

# 3) 성별 표기 통일 (M -> 남, F -> 여)
df["성별"] = df["성별"].replace({"M": "남", "F": "여"})

# 4) 가입일을 datetime 타입으로 변환
df["가입일"] = pd.to_datetime(df["가입일"])

# 5) 가입월(月) 추출
df["가입월"] = df["가입일"].dt.month

# 6) 연령대 컬럼 동적 생성 (10대, 20대, 30대 ... 70대 등 자동 계산)
df["연령대"] = (df["나이"] // 10 * 10).astype(str) + "대"


# ---------------------------------------------------------
# 2. 데이터 분석 및 통계 출력 (Data Analysis)
# ---------------------------------------------------------
print("\n--- [고객 데이터 분석 결과] ---")

# 1) 평균 나이
avg_age = df["나이"].mean()
print(f"1. 고객 평균 나이: {avg_age:.1f}세")

# 2) 성별 분포 및 비율
gender_count = df["성별"].value_counts()
gender_ratio = (df["성별"].value_counts(normalize=True) * 100).round(1)
print(f"\n2. 성별 분포 (명):\n{gender_count}")
print(f"\n3. 성별 비율 (%):\n{gender_ratio}")

# 3) 성별에 따른 평균 나이
age_by_gender = df.groupby("성별")["나이"].mean().round(1)
print(f"\n4. 성별 평균 나이:\n{age_by_gender}")

# 4) 월별 가입 고객 수 & 최다 가입 월
monthly_signup = df["가입월"].value_counts().sort_index()
most_month = monthly_signup.idxmax()
print(f"\n5. 월별 가입자 수:\n{monthly_signup}")
print(
    f"   -> 가장 가입자가 많았던 달: {most_month}월 ({monthly_signup.max()}명)"
)

# 5) 연령대별 고객 수 (10대 ~ 70대 전체 반영)
age_counts = df["연령대"].value_counts().sort_index()
print(f"\n6. 연령대별 고객 수:\n{age_counts}")


# ---------------------------------------------------------
# 3. 엑셀 파일 저장
# ---------------------------------------------------------
df.to_excel("고객분석.xlsx", index=False)
print("\n[성공] '고객분석.xlsx' 엑셀 파일 생성 완료!")


# ---------------------------------------------------------
# 4. 연령대별 가입자 수 시각화 (Visualization)
# ---------------------------------------------------------
# 한글 폰트(맑은 고딕) 설정 및 마이너스 깨짐 방지
plt.rc("font", family="Malgun Gothic")
plt.rc("axes", unicode_minus=False)

plt.figure(figsize=(10, 6))
ax = sns.barplot(
    x=age_counts.index,
    y=age_counts.values,
    hue=age_counts.index,
    palette="viridis",
    legend=False,
)

# 그래프 세부 디테일 설정
plt.title("연령대별 가입자 수 분포", fontsize=16, fontweight="bold", pad=15)
plt.xlabel("연령대", fontsize=12)
plt.ylabel("가입자 수 (명)", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# 막대 상단 수치 표시
for p in ax.patches:
    height = int(p.get_height())
    ax.annotate(
        f"{height:,}명",
        (p.get_x() + p.get_width() / 2.0, height),
        ha="center",
        va="bottom",
        fontsize=11,
        xytext=(0, 3),
        textcoords="offset points",
    )

plt.tight_layout()
plt.show()