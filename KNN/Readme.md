# KNN-Based Hotel Recommendation System

## Overview

This project involves creating a **K-Nearest Neighbors (KNN)**-based recommendation system to suggest hotels based on user preferences. The model leverages several features such as location, rating, and amenities to recommend hotels that are closest (both geographically and feature-wise) to a given query hotel.

The project also utilizes a **Large Language Model (LLM)** to clean and preprocess textual data, ensuring that the dataset is in an optimal format for the machine learning model.

Due to computational and time constraints, we focused on a subset of the dataset, using only **20,000 hotel records** from the **United States**. This allowed us to efficiently preprocess the data and train the KNN model.

---

## Table of Contents

- [Objective](#objective)
- [Dataset](#dataset)
- [Workflow Summary](#workflow-summary)
- [Data Preprocessing](#data-preprocessing)
  - [LLM-Based Data Cleaning](#llm-based-data-cleaning)
- [Feature Engineering](#feature-engineering)
- [Model Building](#model-building)
- [Evaluation](#evaluation)
- [Visualization](#visualization)
- [Streamlit App](#streamlit-app)
  - [Installation](#installation)
  - [Running the Streamlit App](#running-the-streamlit-app)
  - [Screenshot](#screenshot)
- [Conclusion](#conclusion)

---

## Objective

The primary goal of this project is to build a recommendation system that suggests hotels similar to a given query based on a set of features such as:
- **Geographic location** (latitude and longitude)
- **Hotel rating** (e.g., star rating)
- **Hotel amenities** (WiFi, swimming pool, pets allowed, etc.)

The system uses the **K-Nearest Neighbors (KNN)** algorithm to find the top 3 nearest hotels, and the results are visualized using an interactive map.

---

## Dataset

The dataset used for this project is available on Kaggle:  
[**TBO Hotels Dataset**](https://www.kaggle.com/datasets/raj713335/tbo-hotels-dataset)

This dataset includes information on thousands of hotels from around the world, including geographic coordinates, ratings, and various amenities.

### Subset Selection

Due to computational and time constraints with processing such a large dataset using an LLM, we focused on a subset of **20,000 hotels** located in the **United States**. This reduced the data size and allowed us to efficiently clean, preprocess, and model the data without sacrificing too much diversity in the features.

---

## Workflow Summary

The project follows these steps:

1. **Data Collection**: Raw hotel data is collected, which includes features like geographic coordinates (latitude and longitude), ratings, and amenities.
  
2. **Data Cleaning**: A Large Language Model (LLM) is used to help clean and preprocess textual data, specifically to extract and standardize information about hotel facilities and other features.

3. **Feature Engineering**: The cleaned data is transformed into numerical features to make it suitable for the KNN algorithm. Features include latitude, longitude, star rating, and binary flags for hotel amenities.

4. **Model Training**: The K-Nearest Neighbors algorithm is trained using the engineered features. The model calculates the distance between hotels based on both geographic and amenity-based features.

5. **Evaluation**: The model's performance is evaluated by examining the effectiveness of its recommendations. The **Elbow method** is used to select the optimal number of neighbors.

6. **Visualization**: The results are visualized on a map using **Folium**, where the query hotel and the nearest neighbors are plotted with markers.

---

## Data Preprocessing

The first step after loading the data was to ensure that it was clean and usable for the KNN algorithm. The dataset included various attributes such as hotel names, locations (latitude and longitude), ratings, and a list of available amenities.

### LLM-Based Data Cleaning

In this project, an LLM was utilized to assist in cleaning the dataset, specifically for handling textual data related to hotel facilities. Here’s a breakdown of how the LLM was used:

1. **Facility Extraction**:
   - The hotel dataset included a column with unstructured text describing hotel facilities. These descriptions were often inconsistent, containing typos or varying formats.
   - The LLM was employed to extract meaningful facilities from the text, standardizing the descriptions into a structured format, such as converting "free wifi" and "WiFi" into a single feature "WiFi".
   
2. **Standardizing Data**:
   - The LLM helped to ensure that facilities such as "Pets Allowed," "Swimming Pool," and "Restaurant" were consistently formatted across all records.
   - This was crucial for transforming the facilities into binary features (i.e., whether a hotel has a given facility or not), which could then be used for feature engineering.

Using the LLM for these tasks greatly improved the accuracy and consistency of the dataset, allowing for more effective feature engineering and modeling.

---

## Feature Engineering

Once the data was cleaned, the next step was to transform the available attributes into features that could be used by the KNN algorithm.

- **Location Features**:
  - Latitude and Longitude were extracted and normalized. These features were critical for calculating the geographic distance between hotels.
  
- **Rating Feature**:
  - Hotel star ratings were converted into numerical values (e.g., 1 for one-star, 5 for five-star). This allowed the model to take into account the quality of the hotels when making recommendations.

- **Amenity Features**:
  - The extracted amenities (e.g., WiFi, pets allowed, swimming pool) were converted into binary features. For example, if a hotel had WiFi, the "WiFi" feature would be set to 1, otherwise 0.
  - This made it easy for the KNN algorithm to factor in whether or not a hotel had specific amenities when calculating similarity.

---

## Model Building

With the cleaned and engineered dataset, the next step was to build the recommendation model using the **K-Nearest Neighbors (KNN)** algorithm.

- **KNN Algorithm**:
  - The KNN algorithm calculates the distance between the query hotel and every other hotel in the dataset. The distance is based on both geographic proximity (latitude and longitude) and similarity in features (rating and amenities).
  - The model returns the **top 3 nearest neighbors** to the query hotel, which are considered to be the most similar hotels based on the input preferences.

---

## Evaluation

The performance of the KNN model was evaluated using several techniques:

- **Elbow Method**:
  - The Elbow method was used to determine the optimal number of neighbors (K) for the KNN model. This method involves plotting the average distance to the K-th nearest neighbor for different values of K and choosing the point where the rate of decrease slows down (the "elbow").
  - This ensures that the model is neither too complex nor too simple.

- **Distance Calculation**:
  - The model calculates the **Euclidean distance** between hotels based on both geographical features (latitude/longitude) and feature similarities (amenities, rating).
  - A hotel with a small distance to the query hotel is considered to be a good match.

---

## Visualization

To make the results of the recommendation system easy to interpret, an interactive map was created using **Folium**. The map displays:

- **Query Hotel**: The hotel that the user input as the query is marked on the map with a **green marker**.
- **Recommended Hotels**: The top 3 nearest hotels (based on the KNN model) are marked with **red markers**.

Each marker includes a popup with the hotel's information, allowing users to easily explore the recommendations.

---

## Streamlit App

To provide an interactive interface for the hotel recommendation system, a **Streamlit** web application is built. This allows users to input query hotel details and receive recommendations dynamically, along with a visualization of the results on an interactive map.

### Installation

To run the Streamlit app locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <your-repo-link>
   cd <your-repo-directory>
   ```

2. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Streamlit**:
   If you haven't already installed Streamlit, use:
   ```bash
   pip install streamlit
   ```

### Running the Streamlit App

To start the Streamlit app, run the following command:

```bash
streamlit run app.py
```

This will open a local web server (usually at `http://localhost:5000`), where you can interact with the hotel recommendation system.

### Screenshot

Here is a screenshot of the Streamlit app interface:

![Streamlit App Screenshot](./images/streamlit_screenshot.png)

(*Note: Add a screenshot of your Streamlit app interface once it's ready.*)

---

## Conclusion

This project demonstrates the successful application of the **K-Nearest Neighbors (KNN)** algorithm to recommend hotels based on geographic proximity and similarity in features such as ratings and amenities. The use of an **LLM** for data cleaning helped ensure that the dataset was accurately processed, leading to more reliable recommendations.

By leveraging the power of machine learning and interactive visualizations, this project provides an effective way to help users find hotels that best match their preferences.

---

### Future Work

- **Additional Features**: Future iterations of the project could include more advanced features, such as user reviews, prices, and booking availability, to further