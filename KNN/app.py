import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from sklearn.neighbors import NearestNeighbors
import pickle
from geopy.geocoders import Nominatim

@st.cache_resource
def load_original_data():
    data = pd.read_csv('us_hotels_data.csv')
    
    # Split cityName into City and State
    data[['City', 'State']] = data['cityName'].str.split(',', expand=True)
    data['City'] = data['City'].str.strip()  # Clean leading/trailing spaces
    data['State'] = data['State'].str.strip()  # Clean leading/trailing spaces
    
    # Extract Latitude and Longitude from the Map column 
    data[['Latitude', 'Longitude']] = data['Map'].str.split('|', expand=True)
    data['Latitude'] = pd.to_numeric(data['Latitude'], errors='coerce')
    data['Longitude'] = pd.to_numeric(data['Longitude'], errors='coerce')
    
    return data

@st.cache_resource
def load_model_and_ytrain():
    with open('final_pipeline.pkl', 'rb') as f:
        model, y_train = pickle.load(f)
    return model, y_train

def get_lat_lon(city, state):
    geolocator = Nominatim(user_agent="streamlit-app")
    location = geolocator.geocode(f"{city}, {state}")
    if location:
        return location.latitude, location.longitude
    else:
        st.error(f"Could not find coordinates for {city}, {state}.")
        return None, None

# Function to generate map with folium
def generate_map(query_lat, query_lon, nearest_hotels):
    m = folium.Map(location=[query_lat, query_lon], zoom_start=12)
    folium.Marker([query_lat, query_lon], popup="Your Location", icon=folium.Icon(color='green')).add_to(m)

    for _, hotel in nearest_hotels.iterrows():
        if pd.notnull(hotel['Latitude']) and pd.notnull(hotel['Longitude']):  # Ensure coordinates exist
            folium.Marker(
                [hotel['Latitude'], hotel['Longitude']],
                popup=f"{hotel['HotelName']}\nAddress: {hotel['Address']}\nPhone: {hotel['PhoneNumber']}",
                icon=folium.Icon(color='red')
            ).add_to(m)

    return m

original_data = load_original_data()  
model, y_train = load_model_and_ytrain()  

st.title("Hotel Recommendation System 🏨")
st.subheader("Find the best hotels near you with the amenities you want.")

if 'query_point' not in st.session_state:
    st.session_state['query_point'] = None
if 'nearest_hotels' not in st.session_state:
    st.session_state['nearest_hotels'] = None

states = original_data['State'].dropna().unique()
state = st.selectbox("Select a State", sorted(states))


city = st.selectbox("Select a City", sorted(original_data[original_data['State'] == state]['City'].unique()))

rating = st.selectbox("Select Hotel Rating (Stars)", [1, 2, 3, 4, 5], index=2)

st.subheader("Filter by Amenities")

col1, col2, col3 = st.columns(3)

amenities = ['Air Conditioning', 'Airport shuttle', 'Bar', 'Breakfast', 'Business Centre', 'Lift',
    'Non-smoking rooms', 'Pets Allowed', 'Restaurant', 'Room service', 'Swimming pool', 'WiFi']

selected_amenities = []

with col1:
    for amenity in amenities[:len(amenities)//3]:  
        if st.checkbox(amenity):
            selected_amenities.append(amenity)

with col2:
    for amenity in amenities[len(amenities)//3: 2 * len(amenities) // 3]:  
        if st.checkbox(amenity):
            selected_amenities.append(amenity)

with col3:
    for amenity in amenities[2 * len(amenities) // 3:]:  
        if st.checkbox(amenity):
            selected_amenities.append(amenity)

if st.button("Submit"):
    query_lat, query_lon = get_lat_lon(city, state)

    if query_lat and query_lon:
        query_dict = {
            'Latitude': query_lat,
            'Longitude': query_lon,
            'Rating': rating,
            **{amenity: 1 if amenity in selected_amenities else 0 for amenity in amenities}
        }

        features = ['Latitude', 'Longitude', 'Rating', 'Air Conditioning',
                    'Airport shuttle', 'Bar', 'Breakfast', 'Business Centre', 'Lift',
                    'Non-smoking rooms', 'Pets Allowed', 'Restaurant', 'Room service',
                    'Swimming pool', 'WiFi']
        
        st.session_state['query_point'] = pd.DataFrame([query_dict])[features]  # Ensure correct feature order

        distances, indices = model['knn'].kneighbors(st.session_state['query_point'])

        nearest_hotel_codes = y_train.iloc[indices[0]].tolist()

        st.session_state['nearest_hotels'] = original_data[original_data['HotelCode'].isin(nearest_hotel_codes)]

if 'nearest_hotels' in st.session_state and st.session_state['nearest_hotels'] is not None:
    st.subheader("Recommended Hotels")
    
    nearest_hotels = st.session_state['nearest_hotels']

    st.table(nearest_hotels[['HotelName', 'Address', 'PhoneNumber', 'HotelWebsiteUrl']].head(3).reset_index(drop=True))

    map = generate_map(st.session_state['query_point']['Latitude'][0], st.session_state['query_point']['Longitude'][0], st.session_state['nearest_hotels'])
    st_folium(map, width=700, height=500)
else:
    st.write("Submit a query to get hotel recommendations.")
