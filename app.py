import streamlit as st
import pandas as pd
import pickle


filename = r'C:\ds projects\best_model.pkl'
with open(filename, 'rb') as file:
    model = pickle.load(file)


encoding_dict = {

"Gender": {
    "Male": 0,
    "Female": 1
},

"Marital Status": {
    "Single": 0,
    "Married": 1,
    "Divorced": 2
},

"Education Level": {
    "High School": 0,
    "Bachelor's": 1,
    "Master's": 2,
    "PhD": 3
},

"Occupation": {
    "Unemployed": 0,
    "Employed": 1,
    "Self-Employed": 2
},

"Location": {
    "Rural": 0,
    "Urban": 1,
    "Suburban": 2
},

"Policy Type": {
    "Basic": 0,
    "Premium": 1,
    "Comprehensive": 2
},

"Smoking Status": {
    "No": 0,
    "Yes": 1
},

"Exercise Frequency": {
    "Rarely": 0,
    "Monthly": 1,
    "Weekly": 2,
    "Daily": 3
},

"Property Type": {
    "Apartment": 0,
    "House": 1,
    "Condo": 2
}

}

def encode_features(df, encoding_dict):
    df = df.replace(encoding_dict)
    return df

st.markdown("""
<style>

/* App background */
.stApp {
    background-color: #f8f6f2;
}

/* Main title */
.main-title {
    color: #8b1c2e;
    font-size: 50px;
    font-weight: 700;
    text-align: center;
    letter-spacing: 2px;
}

/* Subtitle */
.sub-title {
    color: #8b1c2e;
    font-size: 60px;
    font-weight: 900;
    text-align: center;
    letter-spacing: 4px;
    margin-top: 20px;
}

/* Sidebar background */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
}

/* Predict button */
.stButton>button {
    background-color: #8b1c2e;
    color: white;
    font-size: 18px;
    border-radius: 8px;
    padding: 10px 25px;
}

.stButton>button:hover {
    background-color: #6f1423;
}

/* Result card */
.result-card {
    background-color: white;
    padding: 30px;
    border-radius: 10px;
    border-left: 8px solid #8b1c2e;
    text-align: center;
    font-size: 70px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="sub-title">--- SMART PREMIUM ---</div>', unsafe_allow_html=True)
st.markdown(""" <h1 style='text-align: center;color:#2E86C1;'>You Can\'t Predict the FUTURE but You Can PROTECT It</h3> """, unsafe_allow_html=True)


columns = [
'Age','Gender','Annual Income','Marital Status',
'Number of Dependents','Education Level','Occupation','Health Score',
'Location','Policy Type','Previous Claims','Vehicle Age',
'Credit Score','Insurance Duration','Smoking Status',
'Exercise Frequency','Property Type','Policy_Year','Policy_Month','Policy_Day'
]

# ---------- SESSION STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 0

if "data" not in st.session_state:
    st.session_state.data = {}

# ---------- START SCREEN ----------
if st.session_state.step == 0:
    image= r'C:\Users\Hp\Downloads\Best-Health-Insurance-Plan-Family.png'
    st.image(image, use_container_width=True)
    col1,col2,col3 = st.columns([2,1,2])

    with col2:
        if st.button("You Click ⏻ We Cover"):
            st.session_state.step = 1
            st.rerun()

# ---------- QUESTIONS ----------
elif 1 <= st.session_state.step <= len(columns):

    field = columns[st.session_state.step-1]

    st.subheader(f"Enter {field}")

    # Input types
    if field == "Age":
        value = st.number_input("Age",18,80,30)

    elif field == "Gender":
        value = st.selectbox("Gender",["Male","Female"])

    elif field == "Annual Income":
        value = st.number_input("Annual Income",10000,10000000,500000)

    elif field == "Marital Status":
        value = st.selectbox("Marital Status",["Single","Married","Divorced"])

    elif field == "Number of Dependents":
        value = st.selectbox("Dependents",[0,1,2,3,4])

    elif field == "Education Level":
        value = st.selectbox("Education Level",
                             ["High School","Bachelor's","Master's","PhD"])

    elif field == "Occupation":
        value = st.selectbox("Occupation",
                             ["Employed","Self-Employed","Unemployed"])

    elif field == "Health Score":
        value = st.slider("Health Score",0,100,70)

    elif field == "Location":
        value = st.selectbox("Location",
                             ["Urban","Suburban","Rural"])

    elif field == "Policy Type":
        value = st.selectbox("Policy Type",
                             ["Basic","Comprehensive","Premium"])

    elif field == "Previous Claims":
        value = st.selectbox("Previous Claims",list(range(10)))

    elif field == "Vehicle Age":
        value = st.slider("Vehicle Age",0,20,5)

    elif field == "Credit Score":
        value = st.slider("Credit Score",300,1000,650)

    elif field == "Insurance Duration":
        value = st.slider("Insurance Duration",1,20,5)

    elif field == "Smoking Status":
        value = st.selectbox("Smoking Status",["Yes","No"])

    elif field == "Exercise Frequency":
        value = st.selectbox("Exercise Frequency",
                             ["Daily","Weekly","Monthly","Rarely"])

    elif field == "Property Type":
        value = st.selectbox("Property Type",
                             ["House","Apartment","Condo"])

    elif field == "Policy_Year":
        value = st.number_input("Policy Year",2020,2035,2026)

    elif field == "Policy_Month":
        value = st.number_input("Policy Month",1,12,3)

    elif field == "Policy_Day":
        value = st.number_input("Policy Day",1,31,7)

    # NEXT BUTTON
    if st.button("➜"):
        st.session_state.data[field] = value
        st.session_state.step += 1
        st.rerun()

# ---------- FINAL ----------
else:
    if st.button("Predict Premium"):

        df = pd.DataFrame([st.session_state.data])

        df=encode_features(df,encoding_dict)
        prediction = model.predict(df)

        premium = round(float(prediction[0]), 2)

        st.markdown( f""" <div class="result-card">Estimated Premium Amount<br><br>₹ {premium}</div>""",unsafe_allow_html=True )

        st.markdown( f""" <div class="sub-title">“Feel safe anywhere on Earth.”</div>""",unsafe_allow_html=True )