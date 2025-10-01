import streamlit  as st
import joblib


model = joblib.load("mymarksmodel")

st.title("Welcome to Simple Marks Predictor Model!")

st.write("This model calculates your marks based on your hours of study.")

hrs = st.slider("Enter your hours : " , 0, 10, 4)

if int(hrs) <= 10:
        finalmarks= model.predict( [[ int(hrs) ]] )
        st.write("Your Final Marks Will be : " , finalmarks)
else:
        st.write("not supported")
