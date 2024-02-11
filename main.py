import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
from annotated_text import annotated_text
import plotly_express as px


colours = {
	'normal': '#A8A77A',
	'fire': '#EE8130',
	'water': '#6390F0',
	'electric': '#F7D02C',
	'grass': '#7AC74C',
	'ice': '#96D9D6',
	'fighting': '#C22E28',
	'poison': '#A33EA1',
	'ground': '#E2BF65',
	'flying': '#A98FF3',
	'psychic': '#F95587',
	'bug': '#A6B91A',
	'rock': '#B6A136',
	'ghost': '#735797',
	'dragon': '#6F35FC',
	'dark': '#705746',
	'steel': '#B7B7CE',
	'fairy': '#D685AD',
}

st.title('Pokemon Stats Comparison Tool')
st.divider()


#Get a random pokedex number
random_number = str(np.random.randint(0, 720))
random_number_2 = str(np.random.randint(0, 720))

## For random pokemons
# print(all_pokemon)
#Fetch the name of that pokemon 
# def get_random_pokemon(number:int) -> str:
#     try: 
#         url = 'https://pokeapi.co/api/v2/pokemon/'+number
#         response = requests.get(url)
#         data = response.json()
#     except Exception as e:
#         st.write(f'Error: {e}')
#         data = None
#     return data.get('name')

# poke_name = get_random_pokemon(random_number)
# poke_name_2 = get_random_pokemon(random_number_2)
######################################################################################################



file = open('pokemon-list-en.txt', 'r')
all_pokemon = list(file.readlines())
all_pokemon = [pokemon.strip() for pokemon in all_pokemon]

def get_pokemon_data(pokemon_name) -> dict:
    try: 
        url = 'https://pokeapi.co/api/v2/pokemon/'+pokemon_name
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        st.write(f'Error: {e}')
        data = None
    return data

poke_name = ""
poke_name_2 = ""
pokemon_data = {}
pokemon_data_2 = {}
poke_type_colors = []

col1, col2 = st.columns(2, gap='medium')


with col1:
    poke_name = st.selectbox('Select Pokemon 1', all_pokemon, index=100)
    pokemon_data = get_pokemon_data(poke_name)

with col2:
    poke_name_2 = st.selectbox('Select Pokemon 2', all_pokemon, index=200)
    pokemon_data_2 = get_pokemon_data(poke_name_2)

with st.spinner('Wait for it...'):

    if poke_name != poke_name_2:
        if pokemon_data and pokemon_data_2:
            col1, col2 = st.columns(2, gap="medium")

            with col1:
                st.header(pokemon_data.get('name').capitalize())
                st.image(pokemon_data.get('sprites').get('front_default'))
                st.write('Pokemon Weight',pokemon_data.get('weight'))
                poke_type = pokemon_data.get('types')[0].get('type').get('name') 
                annotated_text(
                    (poke_type,"", colours[poke_type]),
                )
                poke_type_colors.append(colours[poke_type])

            # with col2:
            #     st.header('vs')

            with col2:
                st.header(pokemon_data_2.get('name').capitalize())
                st.image(pokemon_data_2.get('sprites').get('front_default'))
                st.write('Pokemon Weight',pokemon_data_2.get('weight'))
                poke_type = pokemon_data_2.get('types')[0].get('type').get('name') 
                annotated_text(
                    (poke_type,"", colours[poke_type]),
                )    
                poke_type_colors.append(colours[poke_type])
            

            stats_data = {stat.get('stat').get('name').capitalize(): stat.get('base_stat') for stat in pokemon_data.get('stats')}
            stats_data_2 = {stat.get('stat').get('name').capitalize(): stat.get('base_stat') for stat in pokemon_data_2.get('stats')}
            stats_df = pd.DataFrame([stats_data,stats_data_2])

            name_col = [poke_name.capitalize(), poke_name_2.capitalize()]

            # Renaming indexes
            stats_df = stats_df.rename(index={0: name_col[0], 1: name_col[1]})
            # stats_df

            transposed_df = stats_df.T
            # transposed_df

            # Making plotly bar chart
            fig = px.bar(transposed_df, x=transposed_df.index, y=transposed_df.columns,
                        color_discrete_sequence=poke_type_colors*len(transposed_df),
                        barmode='group')
            fig.update_layout(legend_title_text="Pokemon", xaxis_title="Stat", yaxis_title="Value")

            st.plotly_chart(fig)

        
    else:
        st.write('Please select different pokemons for comparison')
