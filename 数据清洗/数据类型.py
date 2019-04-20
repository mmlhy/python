import pandas as pd
student_data = pd.read_csv('1.1-data.csv')
#标准型
print(student_data['省份'])
#序数型
print(student_data['年级'])

cate_array = pd.Categorical(['bad','bad','good','excellent','good','perfect','good','perfect'],categories = ['bad','good','excellent','perfect'])
#统计信息
print(cate_array.value_counts())
#格式化信息
print(cate_array.describe())

#布尔型
print(student_data.loc[:,['性别','住校']])

#数值型
print(student_data['成绩'])