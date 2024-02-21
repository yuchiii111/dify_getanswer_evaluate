from getanswer import GETANSWER
from evaluation import eva_mean
import pandas as pd


api_key = ''
url = ''
input_file_path = ''
output_file_path = ''

df = pd.read_csv(input_file_path)
querys = df['query']
csv_ans = []
for query in querys:
	d_GETANS = GETASNWER(query, api_key, url)
	csv_ans.append(d_GETANS.get_answer())

df['answer'] = csv_ans
df.to_csv(output_file_path, index=False)

f1,em = eva_mean(df)
print(f1,em)

	
	
