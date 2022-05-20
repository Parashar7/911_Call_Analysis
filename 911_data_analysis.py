import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import jinja2

df = pd.read_csv('911.csv')
df['department'] = df['title'].apply(lambda title: title.split(':')[0])
df['cause'] = df['title'].apply(lambda title: title.split(':')[1])
df['timeStamp'] = pd.to_datetime(df.timeStamp)
df['Year'] = pd.DatetimeIndex(df.timeStamp).year
df['month'] = pd.DatetimeIndex(df.timeStamp).month
df['date'] = pd.DatetimeIndex(df.timeStamp).date
df['week'] = pd.DatetimeIndex(df.timeStamp).dayofweek
df['day'] = pd.DatetimeIndex(df.timeStamp).day
df['hour'] = pd.DatetimeIndex(df.timeStamp).hour
df['minute'] = pd.DatetimeIndex(df.timeStamp).minute
df['second'] = pd.DatetimeIndex(df.timeStamp).second

# dictionary string names
dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
df['week'] = df['week'].map(dmap)

print(df.date.unique())
# print(df.nunique())
# print(df.describe())
# print(df.shape)
# print(df.lat.unique())
df_new = df.drop('e', axis=1)
# print(df_new.columns)
# print(df_new.zip.nunique())
# print('Null Values :\n', df_new.isnull().values.sum())
# print(df_new.isnull().sum())
# df_zip = pd.DataFrame(df_new['zip'].value_counts().head(5))
# df_zip.rename(columns={'zip': 'Top 5'}, inplace=True)
# print(df_zip)
# print(df_twp)
# print(df_new.title.unique())

# print(df.title.unique())
df['reason'] = df['title'].apply(lambda title: title.split(':')[0])
df['title_code'] = df['title'].apply(lambda title: title.split(':')[1])
# print('Title is\n\n', df.title.unique())
# print('Reason\n\n', df.reason.unique())
# print(df.reason.value_counts())
# print('Title_code\n\n', df.title_code)

# df['reason'].value_counts()
# print(df['reason'])
# print(df.columns)
# print(df_new.title.unique())

sns.set_style("darkgrid")

# sns.countplot(data=df, x='reason', hue='reason')
# sns.countplot(x='reason', data=df)

#Overall 911 Emregency Calls

# fig, axes = plt.subplots(figsize=(10, 5))
# sns.countplot(y='title', data=df, order=df['title'].value_counts().index, palette='prism')
# sns.despine(bottom=False, left=True)
# axes.set_ylim([9, 0])
# axes.set_title('Overall 911 Emregency Calls', size=15)
# axes.set(xlabel='Number of 911 Calls', ylabel='')
# plt.tight_layout()

#Fire 911 Calls

df.query("reason=='Fire'").groupby('date').count()['lat'].plot(
    figsize=(
        10, 5),
    color='red')
plt.title('Top 10 911 Fire emergency calls', fontsize=16)
plt.xlabel('Count', fontsize=10)
plt.ylabel('')

# Emergency Medical Services 911 calls

# df.query("reason=='EMS'").groupby('title_code').count()['lat'].sort_values(ascending=True).tail(15).plot(kind='barh',
#                                                                                                         color='maroon',
#                                                                                                        figsize=(
#                                                                                                            10, 5))
# plt.title('Emergency Medical Services 911 calls', fontsize=16)
# plt.xlabel('Count', fontsize=10)
# plt.ylabel('')
# df[df['reason'] == 'Traffic'].groupby('Date').count()['lat'].plot(figsize=(15, 5), color='darkblue')
# plt.title('Traffic', fontsize=15)
# sns.despine(bottom=False, left=True)
# plt.tight_layout()

# Heatmap
dayHour = df.groupby(by=['week', 'hour']).count()['department'].unstack()
plt.figure(figsize=(12, 6))
sns.heatmap(dayHour, cmap='viridis', linewidths=0.05)

# Clustermap
# plt.figure(figsize=(12, 6))
# sns.clustermap(dayHour, cmap='viridis', linewidths=0.05)

plt.show()
