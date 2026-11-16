import pandas as pd
df = pd.read_csv("Customer_Churn_Analysis(Project).csv")
print(df)

print("Print the first 5 rows--")
print(df.head())
print("Shape of the Dataset--")
print(df.shape)
print("Dataset Information--")
print(df.info())
print("Column Name--")
print(df.columns)
print("Missing values--")
print(df.isnull().sum())
print("Duplicated Values--")
print("Duplicated Records:",df.duplicated().sum())
print("Check the Data type of the Dataset--")
df["TotalCharges"] = pd.to_numeric(df['TotalCharges'],errors="coerce")  
# convert the text value into the numeric value and the errors='coerce' is it convert invalid and blank value into the 'NAN'
print(df.dtypes)
print(df["TotalCharges"].unique()[:20])
print(df['TotalCharges'].isnull().sum())
print("Data Type:", df["TotalCharges"].dtype)

print("Missing Values:",
      df["TotalCharges"].isnull().sum())
# print(df["TotalCharges"].isnull().sum())
# print(df["TotalCharges"].dtype)

missing_data = df[df["TotalCharges"].isnull()]
print(missing_data[["customerID","tenure","MonthlyCharges","TotalCharges"]])

# How should we handle missing values to make it 0
df["TotalCharges"] = df['TotalCharges'].fillna(0)
print("Missing Values:",df["TotalCharges"].isnull().sum())

print(df.loc[
    df["tenure"] == 0,
    ["tenure", "MonthlyCharges", "TotalCharges"]
])
# How many customer churn
print(df["Churn"].value_counts())

# Calculate the Churn Rate
total_customers = len(df)
churn_customers = (df['Churn'] == "Yes").sum()
Churn_rate = (churn_customers/total_customers)*100
print("Total Customers:",total_customers)
print("Churn Customers:",churn_customers)
print("Churn Rate:",round(Churn_rate,2),"%")

# classify which gender churn more
print(df.groupby("gender")["Churn"].value_counts(normalize=True)*100)

# Contract Type vs Churn
print(df.groupby("Contract")["Churn"].value_counts(normalize=True)*100)
# Longer contracts are associated with significantly lower customer churn.

# Ab investigate karenge ki kis internet service ke customers company zyada chhod rahe hain.
print("Churn According to the Churn--")
print(df.groupby("InternetService")["Churn"].value_counts(normalize=True)*100)

# Fiber optic customers are significantly more likely to leave the company compared to DSL customers.


# Question: Kya high monthly charges pay karne wale customers company zyada chhod rahe hain?
print(df.groupby('Churn')["MonthlyCharges"].mean())
# Answer :  Yes

# Tenure vs Churn Analysis
# Tenure means customer kitne months se company ki service use kar rha hai
print(df.groupby('Churn')['tenure'].mean())

# Ab hum investigate karenge ki customers kis payment method se payment karte hain aur kis payment method mein churn sabse zyada hai.

print(df.groupby("Churn")["PaymentMethod"].value_counts(normalize=True)*100)
print(df.groupby("Churn")["PaymentMethod"].value_counts(normalize=True).unstack().T*100)

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
sns.countplot(data=df,x="Churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.show() 
# Most customers are staying with the company ,but 26.54% of customers have left. the company should focus on improving customer retention and reducing churn.


# contract type vs churn Visualization
plt.figure(figsize=(8,5))
sns.countplot(data=df,x="Contract",hue="Churn")
plt.title("Contract type vs Customer Churn")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.grid(True)
plt.show()

print(df.columns.tolist())
# Senior citizen vs Churn Visualization
plt.figure(figsize=(7,5))
sns.countplot(data=df,x="SeniorCitizen",hue="Churn")
plt.title("Senior Citizen vs Customer Churn")
plt.xlabel("Senior Cititzen(0=NO,1=Yes)")
plt.ylabel("Number of Customer")
plt.show()  

# advanced_churn = df.groupby(["Contract","InternetService"])["Churn"].value_counts(normalize=True ).unstack()*100
# print(advanced_churn)


# Exporting the clean csv file into the Power BI
print(df.to_csv("Customer_Churn_Cleaned_CSV",index=False))
print("Successfully Export")