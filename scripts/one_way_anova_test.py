import pandas as pd
from one_way_anova import one_way_anova
from os import path
import sys


wd = path.dirname(path.abspath(sys.argv[1:]))
df = pd.read_csv(wd + '/data/scores.csv')
print(df.head())

df['total_score'] = df['Average Score (SAT Reading)'] + df['Average Score (SAT Math)'] + df['Average Score (SAT Writing)']
df = df[['Borough', 'total_score']].dropna()
blocks = ['Brooklyn', 'Bronx', 'Manhattan', 'Queens', 'Staten Island']
district_dict = {}

print(one_way_anova(df, 'Borough', 'total_score'))
