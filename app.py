import streamlit as st
import json
import os
import pyperclip  # for copy to clipboard (optional, works locally)

# --- Load Custom CSS ---
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --- Load vibe templates ---
def load_templates():
    with open("templates/vibes.json", "r") as f:
        return json.load(f)

templates = load_templates()

# --- App UI ---
st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")

st.title("📢 LinkedIn Post Generator")
st.write("Craft professional, casual or fun LinkedIn posts for your achievements — in seconds!")

# --- Sidebar Inputs ---
post_type = st.sidebar.selectbox("Post Type", ["project", "hackathon", "resume"])
vibe = st.sidebar.selectbox("Vibe", ["serious", "casual", "funny"])

st.sidebar.markdown("---")
project_name = st.sidebar.text_input("Project Name")
tech_stack = st.sidebar.text_input("Tech Stack")
hackathon_name = st.sidebar.text_input("Hackathon Name (if applicable)")

# --- Generate Post ---
if st.button("Generate LinkedIn Post"):
    try:
        template = templates[post_type][vibe]
        post = template.format(
            project_name=project_name or "My Project",
            tech_stack=tech_stack or "Python",
            hackathon_name=hackathon_name or "Some Hackathon"
        )

        st.subheader("📝 Your LinkedIn Post:")
        st.text_area("Generated Post", value=post, height=200)

        if st.button("📋 Copy to Clipboard"):
            try:
                pyperclip.copy(post)
                st.success("Copied to clipboard!")
            except:
                st.warning("Clipboard copy only works on local machines.")

    except KeyError:
        st.error("Something went wrong. Please check your inputs.")

