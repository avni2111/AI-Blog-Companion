import streamlit as st
import google.generativeai as genai
import os

# Configure the Gemini API with your key
genai.configure(api_key="AIzaSyDhA-EH-UXkWNtMh4aK1M0d8o408TXyCuU")

# Model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 65536,
    "response_mime_type": "text/plain",
}

# Initialize model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-preview-04-17",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(history=[])

# Set app to wide mode
st.set_page_config(layout='wide')

# Title of the app
st.title('✍️🤖 BlogCraft: Your AI writing companion')

# Subheader
st.subheader('Now you can craft perfect blogs with the help of AI - BlogCraft is your New AI Blog Companion')

# Sidebar for user input
with st.sidebar:
    st.title("Input your Blog details")
    st.subheader("Enter the details of your Blog you want to generate")

    blog_title = st.text_input("Blog Title")
    keywords = st.text_area("Keywords (comma separated)")
    num_words = st.slider("Number of Words", min_value=250, max_value=1000, step=250)
    
    submit_button = st.button("Generate Blog")

# Generate the blog
if submit_button:
    if blog_title.strip() == "" or keywords.strip() == "":
        st.error("Please fill out both Blog Title and Keywords.")
    else:
        prompt = f"""
        Write a blog titled: '{blog_title}'.
        Use the following keywords: {keywords}.
        The blog should be approximately {num_words} words.
        
        Format the blog with proper headings and structure.
        """
        with st.spinner("Crafting your blog..."):
            response = chat_session.send_message(prompt)
            st.success("✅ Blog generated!")
            st.markdown("## ✨ Generated Blog")
            st.markdown(response.text)
            st.download_button("📄 Download Blog", response.text, file_name="blog.txt")
