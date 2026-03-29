import pandas as p
import matplotlib.pyplot as m
data={"Students":["Adithya","Vikas","Arjun","Arun","Jhon","Naveen","Vishal","Nivas","Neha","Madhav"],
      "Percentage":[88,78,98,90,67,89,60,80,89,96],
      "Branch":["CSM","IT","AIM","CSM","IT","AIM","CSE","CSE","CSD","CSD"],
      "Year":["1st year","1st year","1st year","2nd year","2nd year","3rd year","3rd year","3rd year","4th year","4th year"]
}
df=p.DataFrame(data)

df.to_csv("BranchToppers.csv",index=False)

df=p.read_csv("BranchToppers.csv")
print("----- Full Student Data -----")
print(df)
print("\n----- Results -----")
print("\nAverage Percentage:",df["Percentage"].mean())
print("\nHigest Percentage in  College:", df["Percentage"].max())
print("\n The number Toppers from Each Year:")
print(df["Year"].value_counts())
print("\nAverage Percentage from Each Branch:")
print(df.groupby("Branch")["Percentage"].mean())
print("\nTop Students: ")
df=df.sort_values("Percentage",ascending=False)
print(df)
print("\nTop 5 students:")
print(df.head())
df.head().to_csv("Top5Students.csv", index=False)
print("\nLast 5 students:")
print(df.tail())
df.groupby("Branch")["Percentage"].mean().plot(kind="bar")
m.title("Toppers Percentage by  Branch")
m.xlabel("Branch")
m.ylabel("Percentage")
m.show()




