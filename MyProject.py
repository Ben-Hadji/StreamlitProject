import streamlit as st
import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
import time

import streamlit as st



st.title('study of the transfer market for the 2017-2018 year')


@st.cache
def load_data(data):
    df = pd.read_csv(data, sep =";")
    return df

    
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
df = load_data('transfermarkt_fbref_201718.csv')
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! ")
##
##for percent_complete in range(15):
##    time.sleep(0.1)
##    my_bar.progress(percent_complete + 1)
    
df = pd.read_csv('transfermarkt_fbref_201718.csv', sep =";")

st.subheader('the raw data we worked on')
st.write(df)
st.write("we reduce the dataFrame just for keeping the columns which we have interest")

if st.checkbox('Show reduce dataframe'):
    df = df[["player",
            "nationality"
            ,"position"
            ,"squad"
            ,"age"
            ,"height" 
            ,"league"
            ,"minutes"
            ,"goals"
            ,"assists"
            ,"games"
            ,"value"
            ,"goals_per90"
            ,"assists_per90"
            ,"goals_assists_per90"
            ,"dribbles"
            ,"interceptions"
             ,"goals_assists_per90m"
            ,"minutes_90s",
                "WinCL"]]
    df
#nuage de point
if st.checkbox('valeur marchande par rapport aux temps de jeu (nuage de point)'):
    st.write("valeur marchande par rapport aux temps de jeu")
    #sb.scatterplot(data=df, x="value", y="minutes", hue = "position");
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(
       df["value"],
       df["minutes"],
    )

    ax.set_xlabel("value")
    ax.set_ylabel("minutes")
    st.write(fig)
if st.checkbox('valeur marchande par rapport aux buts marqués (nuage de point)'):
    #sb.scatterplot(data=df, x="value", y="goals", hue = "position");
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(
       df["value"],
       df["goals"],
    )

    ax.set_xlabel("value")
    ax.set_ylabel("goals")
    st.write(fig)

if st.checkbox('valeur marchande par rapport aux buts marqués (barre)'):
    fig = sb.catplot(data=df, y="value", x="goals", kind="bar",  height=7, aspect=1.5)
    st.pyplot(fig)

if st.checkbox('valeur marchande par rapport aux buts marqués (lineplot)'):
    fig, ax = plt.subplots() #solved by add this line 
    ax = sb.lineplot(data=df, x="goals", y="value",size = 20.6)
    st.pyplot(fig)

if st.checkbox('valeur marchande par rapport aux passes D (lineplot)'):
    fig, ax = plt.subplots() #solved by add this line 
    ax = sb.lineplot(data=df, x="assists", y="value",size = 20.6)
    st.pyplot(fig)
    
st.write('on rajoute deux nouvelle colonnes : GoalAssist et GoalAssist_game')
df=df.assign(GoalAssist = df['goals']+df['assists'])
df=df.assign(GoalAssist_game = df['GoalAssist']/df['games'])

if st.checkbox('afficher le nouveau dataset'):
    df

if st.checkbox('valeur marchande par rapport aux goals/assists (lineplot)'):
    fig, ax = plt.subplots() #solved by add this line 
    ax = sb.lineplot(data=df, x="GoalAssist", y="value",size = 20.6)
    st.pyplot(fig)

if st.checkbox('valeur marchande par rapport au poste du joueur(barre)'):
    fig = sb.catplot(data=df, y="value", x="position", kind="bar", height=5, aspect=2.3)
    st.pyplot(fig)

if st.checkbox('valeur marchande par rapport à la ligue (barre)'):
    fig = sb.catplot(data=df, y="value", x="league", kind="bar", height=5, aspect=2.3)
    st.pyplot(fig)

if st.checkbox('valeur marchande par rapport au poste du joueur et la ligue(barre)'):
    fig = sb.catplot(data=df, y="value", x="position", kind="bar", hue = 'league',height=5, aspect=2.5)
    st.pyplot(fig)

if st.checkbox('valeur marchande par rapport à la ligue (boxplot)'):
    fig, ax = plt.subplots(figsize=(17, 8))#solved by add this line
    ax = sb.boxplot(data=df, y="value", x="league", hue='position')
    st.pyplot(fig)

st.write("on va reduire l'echantillon pour ne garder que les joueurs d'une val < 6000000")

if st.checkbox('valeur marchande en dessous de 6000000£ par rapport à la ligue (boxplot)'):
    fig, ax = plt.subplots(figsize=(17, 12))#solved by add this line
    df1 = df[(df['value'] <6000000) ]
    ax = sb.boxplot(data=df1, y="value", x="position", hue = 'league')
    st.pyplot(fig)
    
st.write("pour une meilleure etude on a remplacé renommées les ligues par des chiffres")
df["league"] = df["league"].replace(['La Liga', 'Premier League', 'Ligue 1', 'Bundesliga', 'Serie A' ], [int(1), int(2), int(3), int(4), int(5)])
df['league'].unique()
if st.checkbox('afficher les nouvelles valeurs'):
    st.write(df['league'].unique())

#calcul de la correlation
corr = df.corr();

if st.checkbox('afficher la hitmap sur la correlation '):
    fig, ax = plt.subplots(figsize=(20,10))
    ax = sb.heatmap(corr, annot=True, ax =ax)
    st.pyplot(fig)
    
if st.checkbox('afficher le calcul de correlation'):
    st.write(corr)

