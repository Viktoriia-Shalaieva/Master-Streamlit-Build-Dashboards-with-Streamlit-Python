import streamlit as st


st.header('Lesson on Pills')

cities = ['Austin', 'Houston', 'London', 'Abuja', 'Ibadan', 'Lagos']

city_selected = st.pills(
                        label='Pick a city',
                        options=cities,
                        selection_mode='single',
                        default=cities[0],
                        key='pill1',
                        help='Pick your favorite city',
                        disabled=False,
                        label_visibility='visible',
                    )
st.markdown('The city you clicked on is {}'.format(city_selected))

# add a multiselect pill
city_multi = st.pills(
    label='Select top cities',
    key='pill2',
    options=cities,
    selection_mode='multi',
    help='Select multiple cities',
)

st.markdown('The cities you clicked on are {}'.format(city_multi))
