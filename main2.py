import requests
import streamlit as st

st.title('prayer timing :blue[App] :heart:')




def fetch_prayer_times (city, country):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country=United{country}&method=8"

    try:
        response = requests.get(url)
        info = response.json()
        if "data" in info:
            timings = info["data"]["timings"]
            return timings
        else:
            return "none"
    except Exception as e:
        return f"an error occurred {e}"
    

city = st.selectbox(
    'Enter a city',
    ('ismailia', 'cairo', 'tanta'))
st.write('your city is:', city)



country = st.selectbox(
    'Enter a country',
    ('Egypt', '1', '2'))

st.write('your city is:', country)



#city = input("inter a city: ")
#country = input("inter a country: ")




st.subheader('the time in your region is', divider='red')
if city and country:
    prayer_timings = fetch_prayer_times(city, country)
    for name, time in prayer_timings.items():
        data = f"{name} : {time}"
        st.subheader(data)
        
    #else:
            #print("unable to fetch prayer times")

