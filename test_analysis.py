import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('911.csv')
# print(df.columns)
# print(df.timeStamp)
df['department'] = df['title'].apply(lambda title: title.split(':')[0])
df['cause'] = df['title'].apply(lambda title: title.split(':')[1])
df['timeStamp'] = pd.to_datetime(df.timeStamp)
df['Year'] = pd.DatetimeIndex(df.timeStamp).year
df['month'] = pd.DatetimeIndex(df.timeStamp).month
df['week'] = pd.DatetimeIndex(df.timeStamp).dayofweek
df['day'] = pd.DatetimeIndex(df.timeStamp).day
df['hour'] = pd.DatetimeIndex(df.timeStamp).hour
df['minute'] = pd.DatetimeIndex(df.timeStamp).minute
df['second'] = pd.DatetimeIndex(df.timeStamp).second
print(df.columns)
df_20 = df.query("Year==2020")
# print(df.minute.value_counts())
final_df_20 = df_20[['lat', 'lng', 'desc', 'zip', 'title', 'timeStamp', 'twp', 'addr',
                     'month', 'day', 'hour', 'minute', 'second', 'department', 'cause']]

# print(final_df_20.desc.value_counts())
# print(final_df_20.department.unique())
# print(final_df_20.cause)
# print(df.year.unique())
# print(df.month.value_counts().sort_values(ascending=True))
cam_df = df.query("Year==[2020, 2019, 2018]")
# fig, axes = plt.subplot(2, 2, figsize=(12, 9))
sns.set_style('darkgrid')
# plt.figure(figsize=(13, 5))

# max calls in EMS dept.

# df.query("department=='EMS'").groupby('cause').count()['lat'].sort_values(ascending=True).tail(10).plot(kind='barh')
# plt.xlabel('Count')
# plt.title('Top 10 EMS calls')
# cause of max calls in Fire dept.

# df.query("department=='Fire'").groupby('cause').count()['lat'].sort_values(ascending=True).tail(10).plot(kind='barh',
#                  figsize=(
#                     10, 5),
#                 color='red')

# s = sns.countplot(data=cam_df, y='department')
# sn = sns.countplot(data=df.query("Year==[2020, 2019, 2018]"), y='title', order=df['title'].value_counts().index,
# palette='PuBuGn_r',
# hue='Year')  # order arranges bars in ascending order
# sn.set_ylim([9, 0])  # sets y limit
# sn.set_title('Overall Top 10 Causes of Call 2020 Vs 2019 Vs 2018', fontsize=15)
# sn.set_xlabel('Count')
# sn.set_ylabel('')
# s.set_title('Phone call camparison', fontsize=15)
# s.set_xlabel('Department')
# s.set_ylabel('Cases')
# s = sns.countplot(data=df, y='title', order=df['title'].value_counts().index)
# s.set_ylim([9, 0])

# Max calls in a specific time

# s = sns.countplot(data=df, y='hour', order=df['hour'].value_counts().index, palette='PuBuGn_r'
#                 )
##s.set_ylabel('Hour')
# s.set_xlabel('Count')
# s.set_title('Calls in each hour')
#fig, axes = plt.subplots(1, 2, figsize=(15, 5))

#sns.countplot(x='week', data=df, palette='viridis', ax=axes[0])
#axes[0].set_title('Weekly Calls', size=15)

#sns.countplot(x='month', data=df, hue='department', palette='viridis', ax=axes[1])
#axes[1].set_title('Monthly Calls', size=15)
#plt.legend(bbox_to_anchor=(1, 1), )

# sns.despine(bottom=False, left=True)
sns.kdeplot(data=df, x='month', hue='department')
plt.show()
