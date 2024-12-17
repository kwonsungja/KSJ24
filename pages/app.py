import streamlit as st
import pandas as pd
import random

# Load the CSV file
csv_url = "https://raw.githubusercontent.com/kwonsungja/KSJ24/main/regular_Nouns_real.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(csv_url)
    df.columns = df.columns.str.lower()
    df["singular"] = df["singular"].str.strip()
    return df

df = load_data()

# Pluralization logic
def pluralize(noun):
    if noun.endswith(('s', 'ss', 'sh', 'ch', 'x', 'z', 'o')):
        return noun + 'es'
    elif noun.endswith('y') and not noun[-2] in 'aeiou':
        return noun[:-1] + 'ies'
    return noun + 's'

# Initialize session state
if "app_state" not in st.session_state:
    st.session_state.app_state = {
        "current_noun": "",
        "score": 0,
        "trials": 0,
        "feedback": "",
    }

# App Layout
st.title("NounSmart: Practice Regular Plural Nouns")
st.markdown("""
## Instructions:
1. Select any singular noun from the dropdown list.
2. Type its plural form.
3. Check your answer to see feedback and score.
""")

# Step 1: Select a Noun
st.subheader("Step 1: Select a Singular Noun")
all_nouns = df["singular"].unique()
selected_noun = st.selectbox("Choose a noun to start:", all_nouns)

if selected_noun:
    st.session_state.app_state["current_noun"] = selected_noun
    st.write(f"### Singular Noun: **{selected_noun}**")

# Step 2: User Input
st.subheader("Step 2: Type the Plural Form")
user_input = st.text_input("Enter the plural form:")

# Step 3: Check Answer
if st.button("Check Answer"):
    state = st.session_state.app_state
    correct_plural = pluralize(state["current_noun"])
    state["trials"] += 1

    if user_input.strip().lower() == correct_plural.lower():
        state["score"] += 1
        state["feedback"] = f"✅ Correct! The plural form of '{state['current_noun']}' is '{correct_plural}'."
    else:
        state["feedback"] = f"❌ Incorrect. The correct plural form of '{state['current_noun']}' is '{correct_plural}'."

    # Display feedback
    st.success(state["feedback"])
    st.write(f"### Your Score: {state['score']} / {state['trials']}")

# Final Report
if st.button("Show Report"):
    state = st.session_state.app_state
    st.subheader("Final Report")
    st.write(f"**Your Total Score:** {state['score']} correct out of {state['trials']} attempts.")

