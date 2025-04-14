import pandas as pd

# Load data
df = pd.read_csv("students.csv")

# Show data
print("Student Marks Data:")
print(df)

# Calculate average marks for each student
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
print("\n Average Marks per Student:")
print(df[["Name", "Average"]])

# Find the top scoring student
top_student = df.loc[df["Average"].idxmax()]
print(f"\n🏆 Top Scorer: {top_student['Name']} with an average of {top_student['Average']:.2f}")

# Subject-wise average
subject_avg = df[["Math", "Science", "English"]].mean()
print("\n📚 Subject-wise Average Marks:")
print(subject_avg)

# Save results to a new CSV
df.to_csv("students_with_averages.csv", index=False)
print("\n✅ Results saved to 'students_with_averages.csv'")
