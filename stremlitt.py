import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


@st.cache_data
def load_data():
    data = pd.read_csv('all_players.csv')
    data['Name'] = data['Name'].astype(str)
    return data

data = load_data()

st.title('Interactive Correlation Matrix')

st.write("## Correlation Matrix")

num_features = st.slider("Select number of features", min_value=2, max_value=len(data.columns)-15, value=2)

selected_features = st.multiselect("Select features", data.columns[5:39].tolist(), default=data.columns[5:39].tolist()[:num_features])



corr_matrix = data[selected_features].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=.5)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
st.write("## Correlation values")
st.write(corr_matrix)


@st.cache_data
def load_data():
    data = pd.read_csv('all_players.csv')
    return data

data = load_data()

st.title('Top Player by Country')

selected_country = st.selectbox("Select a country", data['Nation'].unique())

top_player = data.loc[data[data['Nation'] == selected_country]['Overall'].idxmax(), ['Nation', 'Name', 'Overall']]

st.write(f"The top player in {selected_country} is {top_player['Name']} with a rating of {top_player['Overall']}.")


@st.cache_data
def load_data():
    data = pd.read_csv('all_players.csv')
    return data

data = load_data()


st.title('Search Players')


position = st.selectbox('Position', ['ST', 'CM', 'CAM', 'CDM', 'LW', "RW", 'CB', 'GK', 'CF', 'RB', 'LB', 'LM', 'RM', 'RWB', 'LWB'])
nation = st.text_input('Nation')
age = st.slider('Age', min_value=17, max_value=40, value=(20, 30))
pace = st.slider('Pace', min_value=0, max_value=100, value=(20, 100))
shooting = st.slider('Shooting', min_value=0, max_value=100, value=(20, 100))
defending = st.slider('Defending', min_value=0, max_value=100, value=(20, 100))
physicality = st.slider('Physicality', min_value=0, max_value=100, value=(20, 100))
passing = st.slider('Passing', min_value=0, max_value=100, value=(20, 100))
dribbling = st.slider('Dribbling', min_value=0, max_value=100, value=(20, 100))

filtered_data = data[
    (data['Position'] == position) &
    (data['Nation'].str.contains(nation, na=False, case=False)) &
    (data['Age'].between(age[0], age[1])) &
    (data['Pace'].between(pace[0], pace[1])) &
    (data['Dribbling'].between(dribbling[0], dribbling[1])) &
    (data['Passing'].between(passing[0], passing[1])) &
    (data['Physicality'].between(physicality[0], physicality[1])) &
    (data['Defending'].between(defending[0], defending[1])) &
    (data['Shooting'].between(shooting[0], shooting[1]))
]

st.write(filtered_data)
