import streamlit as st

import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

loaded_model = pickle.load(open('trained_model.sav','rb'))

def check(input_data):

    array_input = np.array(input_data)

    reshaped_input = array_input.reshape(1,-1)

    prediction = loaded_model.predict(reshaped_input)

    return "{:.2f}".format(prediction[0]*100)

def main():
    st.title("Admission Prediction")

    Gre = st.number_input("Graduate Record Examination")

    Toefl = st.number_input("Test of English as a Foreign Language")

    UniRating = st.number_input("University Rating is based on various criteria")

    Sop = st.number_input("Statement of Purpose")

    Lor = st.number_input("Letter of Recommendation")

    cgpa = st.number_input("Cumulative Grade Point Average")

    Research = st.number_input("Research")

    pred = ""
    if st.button("Click Here for Admission Prediction"):
        pred = check([Gre,Toefl,UniRating,Sop,Lor,cgpa,Research])

    st.success(f"Your Admission Chances is {pred} %")

if __name__=='__main__':
    main()
    