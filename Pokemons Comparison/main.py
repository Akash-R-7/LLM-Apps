import streamlit as st
from layout import build_sidebar, comaparsion_columns, build_dataframe, build_plots
from poke_dataloader import get_pokemon_data, colours


def main():
    
    st.title('Pokemon Stats Comparison Tool')
    st.divider()

    poke_name = ""
    poke_name_2 = ""
    pokemon_data = {}
    pokemon_data_2 = {}
    poke_type_colors = []

    poke_name, poke_name_2 = build_sidebar()
    pokemon_data = get_pokemon_data(poke_name)
    pokemon_data_2 = get_pokemon_data(poke_name_2)

    with st.spinner('Loading stats...'):

        if poke_name != poke_name_2:
            if pokemon_data and pokemon_data_2:

                poke_type_colors = comaparsion_columns(pokemon_data, pokemon_data_2, colours)
                df = build_dataframe(pokemon_data, pokemon_data_2, poke_name, poke_name_2)
                build_plots(df, poke_type_colors)
            
        else:
            st.write('Please select different pokemons for comparison')


if __name__ == "__main__":
    main()