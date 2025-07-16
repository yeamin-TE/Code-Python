import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

#pd.set_option('display.max_columns',None) (Show each column but table/terminal breaks)
#print(df.head())
print(df.shape)
#print(df.info())
#print(df.isnull().sum())
missing_percentage = (df.isnull().sum() / len(df) * 100)
#print(missing_percentage)
df.drop(columns = 'Cabin', inplace=True)
#print(df.columns)
#df['Age'].fillna(df['Age'].median(), inplace=True)- erokom code likhle warning msg ashe
df['Age'] = df['Age'].fillna(df['Age'].median())
#df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)- erokom code likhle warning msg ashe
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
#print(df.isnull().sum())
categorical_cols = df.select_dtypes(include= 'object').columns
#print("Category/String cols:\n",categorical_cols)
numerical_cols = df.select_dtypes(include= ['int64', 'float64']).columns
#print("Numerical cols:\n", numerical_cols)
df['Title'] = df['Name'].str.extract(r'([A-Za-z]+)\.' , expand=False)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = 1
df.loc[df['FamilySize'] > 1, 'IsAlone'] = 0
#print(df.columns)
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Survived', labels=['No', 'Yes'])
#plt.show()

#sns.countplot(x= 'Pclass', hue = 'Survived', data=df)
plt.title('Survival Count by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.legend(title= 'Survived', labels=['No', 'Yes'])
#plt.show()

#plt.figure(figsize=(10,5))
sns.histplot(df['Age'], bins = 30 , kde = True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
#plt.show()

#sns.boxplot(x= 'Survived' , y= 'Fare', data=df)
plt.title('Fare Distribution by Survival')
plt.xlabel('Survived')
plt.ylabel('Fare')
#plt.show()

numeric_df = df.select_dtypes(include=['int64', 'float64'])
correlation_matrix = numeric_df.corr()
#print(correlation_matrix)

plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True , cmap= 'coolwarm', fmt= ".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()