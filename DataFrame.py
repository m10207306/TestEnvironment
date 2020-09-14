import pandas as pd
# print(pd.__version__)

# dic = \
# 	{
# 		"col 1": [1, 2, 3],
# 		"col 2": [10, 20, 30],
# 		"col 3": list("xyz"),
# 		"col 4": pd.Series(range(3)),
# 	}
#
# df = pd.DataFrame(dic)
# print(df)

#=== Rename Column
# rename_col = {"col 1": "x", "col 2": "10x"}
# df.rename(rename_col, axis = 1, inplace = True)
# print(df)

# df.columns = ["x(new)", "10x(new)"] + list(df.columns[2:])
# print(df)

#=== create random DataFrame
# print(pd.util.testing.makeDataFrame().shape)
# print(pd.util.testing.makeMixedDataFrame().shape)

#=== I/O of DataFrame
# df.to_csv("file.csv")
# df = pd.read_csv("file path or http address")

#=== MemoryUsage of DataFrame
# df.info(memory_usage = "deep")

#=== DataFrame Combination
# df = pd.concat([pd.read_csv(f) for f in file_list]) # combine a list of dataframes (default axis = 0)
#				[df1, df2, df3...]
# df.reset_index(drop = True, inplace = True)		# drop the orginal index column created from reset_index function
#
# dic1 = \
# 	{
# 		"PassengerID": [1, 2, 3],
# 		"Survived": [0, 1, 1],
# 		"Pclass": [8, 1, 8],
# 		"Name": ["Braund", "Cumings", "Heikkinen"],
# 	}
# df1 = pd.DataFrame(dic1)
#
# dic2 = \
# 	{
# 		"Sex": ["male", "female", "female"],
# 		"Age": [22, 88, 26],
# 	}
# df2 = pd.DataFrame(dic2)
#
# df = pd.concat([df1, df2], axis = 1)
# print(df)

#=== Display Option
# pd.set_option("display.max_columns", None)	# remove the limit number to show column
# pd.get_option("display.max_colwidth")		# get display length of column
# pd.set_option("display.max_colwidth", 10)	# set display length of column
# pd.set_option("display.precision", 1)
# pd.reset_option("all")
# pd.describe_option()						# display available options

# set_option is global setting. if we want to set the specific dataframe, use datafrome.style
df_sample = pd.DataFrame({
	"PassengerID": [5, 183, 377],
	"Survived": [0, 0, 1],
	"Pclass": [3, 3, 3],
	"Sex": ["male", "male", "female"],
	"Age": [35, 9, 22],
	"SibSp": [0, 4, 0],
	"Parch": [0, 2, 0],
	"Ticket": ["373450", "347077", "C 7077"],
	"Fare": [8.1, 31.4, 7.2],
	"Cabin": [None, None, None],
	"Embarked": ["S", "S", "S"]
	})
df_sample.style\
	.format('{:.1f}', subset='Fare')\
	.set_caption('★五顏六色の鐵達尼號數據集☆')\
	.hide_index()\
	.bar('Age', vmin=0)\
	.highlight_max('Survived')\
	.background_gradient('Greens', subset='Fare')\
	.highlight_null()

print(df_sample)

#=== Random Sampling
# df_sample = df.sample(n=10, random_state = 9527).drop("name", axis = 1)

#=== Transpose
# print(df.T)

#=== Operation
# df.fillna(0)
# df.fillna("unknown")

# 刪除 row/column
# columns = ["col 1", "col 2"]
# df.drop(columns, axis = 1)

# df.drop("Name", axis = 1, inplace = True)
# df.drop(0, axis = 0, inplace = True)
# print(df)

# 分割欄位內容
# df = pd.DataFrame({
# 	"name": ["A", "B"],
# 	"feat": ["aa, aaa", "bb, bbb"]
# 	})

# df[["double", "triple"]] = df.feat.str.split(",", expand = True)
# print(df)

