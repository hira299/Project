import streamlit as st
import re

def calculate_password_strength(password):
    # Initialize strength score
    score = 0
    
    # Criteria
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r"\d", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    special_char_criteria = re.search(r"[@$!%*?&,.:;''-_+=]", password) is not None
    
    # Scoring
    if length_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if special_char_criteria:
        score += 1
    
    # Determine strength
    if score == 5:
        st.success("Password Strength : Strong")
    elif score >= 3:
       st.warning("Password Strength : Moderate")

    else:
       st.info("Password Strength : Weak")
        
    

# Streamlit application
def main():
    st.title("Password Strength Tester")
    
    password = st.text_input("Enter your password", type="password")
    
    if password:
        calculate_password_strength(password)
        

if __name__ == "__main__":
    main()
