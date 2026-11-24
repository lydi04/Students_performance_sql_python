import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# 1. Connect to MySQL
password = quote_plus("YOUR PASSWORD")
engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/students_db")

# Connection test (1000 varanum)
print(pd.read_sql("SELECT COUNT(*) AS total_students FROM students_performance", engine))

# 2. Gender wise average scores
q1 = """
SELECT gender,
       ROUND(AVG(math_score),1) AS avg_math,
       ROUND(AVG(reading_score),1) AS avg_reading,
       ROUND(AVG(writing_score),1) AS avg_writing
FROM students_performance
GROUP BY gender
"""
df1 = pd.read_sql(q1, engine)
print(df1)
df1.set_index("gender").plot(kind="bar", figsize=(7, 5), rot=0)
plt.title("Average Scores by Gender")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("scores_by_gender.png")
plt.show()

# 3. Test prep course
q2 = """
SELECT test_prep,
       ROUND(AVG(math_score),1) AS avg_math,
       ROUND(AVG(reading_score),1) AS avg_reading,
       ROUND(AVG(writing_score),1) AS avg_writing
FROM students_performance
GROUP BY test_prep
"""
df2 = pd.read_sql(q2, engine)
print(df2)
df2.set_index("test_prep").plot(kind="bar", figsize=(7, 5), rot=0)
plt.title("Average Scores: Test Prep Course")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("scores_by_test_prep.png")
plt.show()

# 4. Parents education wise average score
q3 = """
SELECT parental_education,
       ROUND(AVG((math_score + reading_score + writing_score)/3),1) AS avg_score
FROM students_performance
GROUP BY parental_education
ORDER BY avg_score
"""
df3 = pd.read_sql(q3, engine)
print(df3)
df3.plot(kind="barh", x="parental_education", y="avg_score", legend=False, figsize=(8, 5))
plt.title("Average Score by Parental Education")
plt.xlabel("Average Score")
plt.tight_layout()
plt.savefig("scores_by_parent_education.png")
plt.show()

# 5. Math pass / fail
q4 = """
SELECT CASE WHEN math_score >= 40 THEN 'Pass' ELSE 'Fail' END AS result,
       COUNT(*) AS students
FROM students_performance
GROUP BY result
"""
df4 = pd.read_sql(q4, engine)
print(df4)
df4.plot(kind="bar", x="result", y="students", legend=False, figsize=(5, 5), rot=0)
plt.title("Math Pass vs Fail")
plt.ylabel("Students")
plt.tight_layout()
plt.savefig("math_pass_fail.png")
plt.show()
