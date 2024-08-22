# Password Strength Tester Using Streamlit
This project is a simple password strength tester built using Python and Streamlit. The application evaluates the strength of a given password based on several criteria, such as length, inclusion of digits, uppercase and lowercase letters, and special characters. It then categorizes the password as "Weak," "Moderate," or "Strong."

## How It Was Done:
### Libraries Used:

- streamlit for creating the web interface.
- re (regular expressions) for pattern matching to check the presence of digits, uppercase letters, lowercase letters, and special characters.

### Password Strength Calculation:

The password strength is calculated by checking five criteria:
- Length of at least 8 characters.
- Presence of at least one digit.
- Presence of at least one uppercase letter.
- Presence of at least one lowercase letter.
- Presence of at least one special character from a specified set.
Each criterion met by the password adds one point to the strength score.

### Strength Categories:

- Strong: All five criteria are met.
- Moderate: At least three criteria are met.
- Weak: Fewer than three criteria are met.

### User Interface:

The application prompts the user to enter a password.
It then displays the strength of the password as either "Weak," "Moderate," or "Strong" based on the calculated score.

## How to Use:
- Install the required packages using pip install streamlit.
- Run the application by executing streamlit run <script_name>.py in the terminal.
- Enter a password in the provided text box, and the application will display the password's strength.
This project demonstrates basic password strength evaluation logic and showcases how to build a simple interactive web app using Streamlit.
