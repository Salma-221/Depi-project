import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# ----------------------
# Load Dataset
# ----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("TrainRides_Cleaned_Enhanced2.csv")

    # Convert Journey Status to Cancelled
    df['Cancelled'] = (df['Journey Status'] == 'Cancelled').astype(int)

    # Month mapping
    month_map = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }

    return df, month_map


# ----------------------
# Regression Model Function
# ----------------------
def regression_predict(X, Y, X_future):
    X = np.array(X)
    Y = np.array(Y)

    model = LinearRegression()
    model.fit(X, Y)

    X_future = np.array(X_future)
    prediction = model.predict(X_future)

    return prediction


# ----------------------
# Streamlit App UI
# ----------------------
st.title("🚆 Train Forecasting Dashboard")
st.write("Predict cancellations, delay, and passenger volume using Linear Regression.")

df, month_map = load_data()

# ----------------------
# Prepare Monthly Datasets
# ----------------------

# Cancellations
monthly = df.groupby(["Journey year", "Journey Month"])["Cancelled"].sum().reset_index()
monthly["Journey Month"] = monthly["Journey Month"].map(month_map)

# Delay
monthly_delay = df.groupby(["Journey year", "Journey Month"])['Journey Delay (min)'].mean().reset_index()
monthly_delay["Journey Month"] = monthly_delay["Journey Month"].map(month_map)

# Passengers
monthly_passengers = df.groupby(["Journey year", "Journey Month"]).size().reset_index(name="Passengers Volume")
monthly_passengers["Journey Month"] = monthly_passengers["Journey Month"].map(month_map)

# ----------------------
# User Input
# ----------------------
st.subheader("🔢 Enter Prediction Date")

year = st.number_input("Year", min_value=2020, max_value=2030, value=2024)
month = st.selectbox(
    "Month",
    list(month_map.keys())
)
month_num = month_map[month]

X_future = [[year, month_num]]

# ----------------------
# Make Predictions
# ----------------------

# Cancellation
X1 = monthly[["Journey year", "Journey Month"]]
Y1 = monthly["Cancelled"]
pred_cancel = regression_predict(X1, Y1, X_future)[0]

# Delay
X2 = monthly_delay[["Journey year", "Journey Month"]]
Y2 = monthly_delay["Journey Delay (min)"]
pred_delay = regression_predict(X2, Y2, X_future)[0]

# Passengers
X3 = monthly_passengers[["Journey year", "Journey Month"]]
Y3 = monthly_passengers["Passengers Volume"]
pred_pass = regression_predict(X3, Y3, X_future)[0]

# ----------------------
# Display Results
# ----------------------
st.subheader("📊 Forecast Results")
st.write(f"🚫 **Expected Cancellations:** `{pred_cancel:.2f}`")
st.write(f"⏱️ **Expected Average Delay:** `{pred_delay:.2f} minutes`")
st.write(f"👥 **Expected Passenger Volume:** `{pred_pass:.0f}`")

st.success("Prediction completed successfully!")
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# ----------------------
# Load Dataset
# ----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("TrainRides_Cleaned_Enhanced2.csv")

    # Convert Journey Status to Cancelled
    df['Cancelled'] = (df['Journey Status'] == 'Cancelled').astype(int)

    # Month mapping
    month_map = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }

    return df, month_map


# ----------------------
# Regression Model Function
# ----------------------
def regression_predict(X, Y, X_future):
    X = np.array(X)
    Y = np.array(Y)

    model = LinearRegression()
    model.fit(X, Y)

    X_future = np.array(X_future)
    prediction = model.predict(X_future)

    return prediction


# ----------------------
# Streamlit App UI
# ----------------------
st.title("🚆 Train Forecasting Dashboard")
st.write("Predict cancellations, delay, and passenger volume using Linear Regression.")

df, month_map = load_data()

# ----------------------
# Prepare Monthly Datasets
# ----------------------

# Cancellations
monthly = df.groupby(["Journey year", "Journey Month"])["Cancelled"].sum().reset_index()
monthly["Journey Month"] = monthly["Journey Month"].map(month_map)

# Delay
monthly_delay = df.groupby(["Journey year", "Journey Month"])['Journey Delay (min)'].mean().reset_index()
monthly_delay["Journey Month"] = monthly_delay["Journey Month"].map(month_map)

# Passengers
monthly_passengers = df.groupby(["Journey year", "Journey Month"]).size().reset_index(name="Passengers Volume")
monthly_passengers["Journey Month"] = monthly_passengers["Journey Month"].map(month_map)

# ----------------------
# User Input
# ----------------------
st.subheader("🔢 Enter Prediction Date")

year = st.number_input("Year", min_value=2020, max_value=2030, value=2024)
month = st.selectbox(
    "Month",
    list(month_map.keys())
)
month_num = month_map[month]

X_future = [[year, month_num]]

# ----------------------
# Make Predictions
# ----------------------

# Cancellation
X1 = monthly[["Journey year", "Journey Month"]]
Y1 = monthly["Cancelled"]
pred_cancel = regression_predict(X1, Y1, X_future)[0]

# Delay
X2 = monthly_delay[["Journey year", "Journey Month"]]
Y2 = monthly_delay["Journey Delay (min)"]
pred_delay = regression_predict(X2, Y2, X_future)[0]

# Passengers
X3 = monthly_passengers[["Journey year", "Journey Month"]]
Y3 = monthly_passengers["Passengers Volume"]
pred_pass = regression_predict(X3, Y3, X_future)[0]

# ----------------------
# Display Results
# ----------------------
st.subheader("📊 Forecast Results")
st.write(f"🚫 **Expected Cancellations:** `{pred_cancel:.2f}`")
st.write(f"⏱️ **Expected Average Delay:** `{pred_delay:.2f} minutes`")
st.write(f"👥 **Expected Passenger Volume:** `{pred_pass:.0f}`")

st.success("Prediction completed successfully!")
