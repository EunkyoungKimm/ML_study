import pandas as pd
csv_input = pd.read_csv(filepath_or_buffer="train_transactions.csv", encoding="ms932", sep=",")
# 항목 수（행수 * 칼럼수）를 반환한다.
print(csv_input.size)
# 지정한 칼럼만을 추출하여 DataFrame객체를 반환한다.
print(csv_input[["특정 열 이름", "특정 열 이름"]])


