
import streamlit as st
import random
import string

def generate_random_password(characters,password_length=6):
    #shuffle characters
    random.shuffle(characters)
    password = []
    for i in range(password_length):
      password.append(random.choice(characters))

      return ("".join(password))


    #cost
ALL_CHARACTERS_PATTERN = list('str.ascii_letters' + 'str.digits' + "!@#$%^&*()_+=-")
ALPHANUMERIC_PATTERN = list('str.ascii_letters' + 'str' + 'str.digits')
ALPHABETS_PATTERN = list('str.ascii_letters') 
NATOPHONETICS_DICTIONARY = {"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta", "E": "Echo","F":"Foxtrot"}
    
def get_natophonetics(term):
        result = ''.jon([NATOPHONETICS_DICTIONARY.get(i.i) for i in list (term.upper())])
        return result
    

def main():
    st.title("Ultimate password generator app")
    st.subheader("Streamlit project")


    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        password_pattern_list = ['alphabets', 'alphanumeric', 'all']
        password_length = st.number_input ("Password Lenght", min_value=5,max_value=50,value=6)
        password_pattern_choice = st.selectbox("pattern",password_pattern_list)
        if st.button("Generate"):
            st.info("Generated results")

            if password_pattern_choice == 'alphabets':
                 password_result = generate_random_password(ALPHABETS_PATTERN,password_length)
            elif password_pattern_choice == 'alphanumeric':
                 password_result = generate_random_password(ALPHANUMERIC_PATTERN,password_length)
            else:
                 password_result = generate_random_password(ALL_CHARACTERS_PATTERN,password_length)

                 st.write(password_result)
                 st.code(password_result)
                 st.info("Nato phonetics")
                 st.write(get_natophonetics(password_result))
            
            
            
        else:
          st.subheader("about")


if __name__ == '__main__':
    main()
        
         
                        



            