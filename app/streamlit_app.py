import pickle
import streamlit as st

model = pickle.load(open('Flight_fare_prediction.pkl','rb'))

input_dict = {
    "Total Stops" : 0,
    "Duration minutes" : 0,
    "Day" : 0,
    "Month" : 0,
    "Dep hour" : 0,
    "Dep minute" : 0,
    "Arrival hour" : 0,
    "Arrival minute" : 0,
    "Air Asia"  : 0,
    "Air India" : 0,
    "IndiGo" : 0,
    "Jet Airways" : 0,
    "Jet Airways Business" : 0,
    "Multiple carriers" : 0,
    "Multiple carriers Premium economy" : 0,
    "SpiceJet" : 0,
    "Trujet" : 0,
    "Vistara" : 0,
    "Vistara Premium economy" : 0,
    "Destination Cochin" : 0,
    "Destination Delhi" : 0,
    "Destination Hyderabad" : 0,
    "Destination Kolkata" : 0,
    "Destination New Delhi" : 0,
    "Source Chennai" : 0,
    "Source New_Delhi" : 0,
    "Source Kolkata" : 0,
    "Source Mumbai" : 0,
}

def prediction(input_data):
    fare = model.predict([input_data])
    return fare

def main():

    st.title("Flight Fare Prediction")

    #getting input data from user
    col1,col2 = st.columns(2)

    destination = col1.selectbox("Destination", 
    ("Cochin", "Delhi", "Hyderabad", "Kolkata", "New Delhi"))

    destination = "Destination " + destination
    input_dict[destination] = 1
    
    source = col2.selectbox("Destination", 
    ("Chennai", "New Delhi", "Kolkata", "Mumbai"))
    
    source = "Source " + source
    input_dict[source] = 1


    col3, col4 = st.columns(2)
    input_dict["Total Stops"] = col3.text_input("Total Stops")
    input_dict["Duration minutes"] = col4.text_input("Duration minutes")

    col5, col6 = st.columns(2)
    input_dict["Day"] = col5.text_input("Day")
    input_dict["Month"] = col6.text_input("Month")

    deph, depm, ah, am = st.columns(4)
    input_dict["Dep hour"] = deph.text_input("Departure hour")
    input_dict["Dep minute"] = depm.text_input("Departure minute")
    input_dict["Arrival hour"] = ah.text_input("Arrival hour")
    input_dict["Arrival minute"] = am.text_input("Arrival minute")

    airline = st.selectbox("Airline",
     ("Air Asia", "Air India", "IndiGo", "Jet Airways", "Jet Airways Business",
     "Multiple carriers", "Multiple carriers Premium economy", "SpiceJet",
     "Trujet", "Vistara", "Vistara Premium economy"))
    input_dict[airline] = 1


    

    input_list = [y for x, y in input_dict.items()]

    

    if st.button("Predict Fare"):
        flight_fare = prediction(input_list)
        st.success(round(flight_fare[0],2))


if __name__ == '__main__':
    main()
