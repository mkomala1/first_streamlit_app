import streamlit;
streamlit.title('My parents new Healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega3 & Blueberrry Oatmeal')
streamlit.text('🥬 Kale,Spinach & Rocket smoothie')
streamlit.text('🥚 Hardboiled Free Range EGGS')
streamlit.text('🥑🍞 Avacado toast')

streamlit.header('🍌🍓🥭 Build your own fruit smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
