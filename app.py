
import streamlit as st
import random
import string

def generate_random_password(characters, password_length=6):
    # shuffle characters
    random.shuffle(characters)
    password = []
    for i in range(password_length):
        password.append(random.choice(characters))

    return "".join(password)

# Corrected character patterns
ALL_CHARACTERS_PATTERN = list(string.ascii_letters + string.digits + "!@#$%^&*()_+=-")
ALPHANUMERIC_PATTERN = list(string.ascii_letters + string.digits)
ALPHABETS_PATTERN = list(string.ascii_letters)
NATOPHONETICS_DICTIONARY = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot"}

# Updated get_natophonetics function
def get_natophonetics(term):
    result = ''
    for i in list(term.upper()):
        if i in NATOPHONETICS_DICTIONARY:
            result += NATOPHONETICS_DICTIONARY[i]
        else:
            print(f"Character '{i}' not found in NATOPHONETICS_DICTIONARY.")
            result += i
    return result

def main():
    st.title("Ultimate password generator app")
    st.subheader("Streamlit project")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        password_pattern_list = ['alphabets', 'alphanumeric', 'all']
        password_length = st.number_input("Password Length", min_value=5, max_value=50, value=6)
        password_pattern_choice = st.selectbox("Pattern", password_pattern_list)
        if st.button("Generate"):
            st.info("Generated results")

            if password_pattern_choice == 'alphabets':
                password_result = generate_random_password(ALPHABETS_PATTERN, password_length)
            elif password_pattern_choice == 'alphanumeric':
                password_result = generate_random_password(ALPHANUMERIC_PATTERN, password_length)
            else:
                password_result = generate_random_password(ALL_CHARACTERS_PATTERN, password_length)

            st.write(password_result)
            st.code(password_result)
            st.info("Nato phonetics")
            st.write(get_natophonetics(password_result))

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
