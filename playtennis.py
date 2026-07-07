import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB

# Play Tennis Dataset
data = {
    "Outlook": [
        "Sunny", "Sunny", "Overcast", "Rain", "Rain",
        "Rain", "Overcast", "Sunny", "Sunny", "Rain",
        "Sunny", "Overcast", "Overcast", "Rain"
    ],

    "Temperature": [
        "Hot", "Hot", "Hot", "Mild", "Cool",
        "Cool", "Cool", "Mild", "Cool", "Mild",
        "Mild", "Mild", "Hot", "Mild"
    ],

    "Humidity": [
        "High", "High", "High", "High", "Normal",
        "Normal", "Normal", "High", "Normal", "Normal",
        "Normal", "High", "Normal", "High"
    ],

    "Wind": [
        "Weak", "Strong", "Weak", "Weak", "Weak",
        "Strong", "Strong", "Weak", "Weak", "Weak",
        "Strong", "Strong", "Weak", "Strong"
    ],

    "Play": [
        "No", "No", "Yes", "Yes", "Yes",
        "No", "Yes", "No", "Yes", "Yes",
        "Yes", "Yes", "Yes", "No"
    ]
}

df = pd.DataFrame(data)

# Label Encoding
le = LabelEncoder()

for column in df.columns:
    df[column] = le.fit_transform(df[column])

# Features and Target
X = df.drop("Play", axis=1)
y = df["Play"]

# Create Model
model = MultinomialNB()

# Train Model
model.fit(X, y)

# Prediction
# Sunny, Cool, High, Strong
sample = [[2, 0, 0, 0]]

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Play Tennis: Yes")
else:
    print("Play Tennis: No")