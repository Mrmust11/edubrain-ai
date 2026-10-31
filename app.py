import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

st.set_page_config(page_title="EduBrain AI", layout="wide", page_icon="🎓")
st.title("🎓 EduBrain AI: Academic Assistant & Quiz Engine")

api_key = st.secrets.get("GEMINI_API_KEY") or st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)

    try:
        working_models = [
            m.name for m in genai.list_models() 
            if 'generateContent' in m.supported_generation_methods
        ]
        selected_model = next((m for m in working_models if 'gemini-1.5-flash' in m), working_models[0])
        model = genai.GenerativeModel(selected_model)
    except Exception as e:
        st.error(f"Error loading models: {e}")
        st.stop()

    uploaded_file = st.file_uploader("Upload Academic PDF Document", type=["pdf"])

    if uploaded_file is not None:
        reader = PdfReader(uploaded_file)
        text = "".join([page.extract_text() or "" for page in reader.pages])

        st.success(f"PDF Uploaded Successfully! Total pages: {len(reader.pages)}")

        tab1, tab2, tab3 = st.tabs(["📝 Summary & Concepts", "🧩 Interactive Quiz", "💬 Q&A Chat"])

        with tab1:
            if st.button("Generate Summary"):
                with st.spinner("Analyzing document..."):
                    prompt = f"Summarize the following academic text into key concepts and bullet points:\n\n{text[:10000]}"
                    response = model.generate_content(prompt)
                    st.write(response.text)

        with tab2:
            if st.button("Generate 5-Question Quiz"):
                with st.spinner("Creating quiz..."):
                    prompt = f"Create a 5-question multiple-choice quiz based on this text with correct answers at the end:\n\n{text[:10000]}"
                    response = model.generate_content(prompt)
                    st.write(response.text)

        with tab3:
            user_question = st.text_input("Ask a question about your document:")
            if user_question:
                with st.spinner("Thinking..."):
                    prompt = f"Answer this question based strictly on the text provided.\nQuestion: {user_question}\n\nText:\n{text[:10000]}"
                    response = model.generate_content(prompt)
                    st.write(response.text)
else:
    st.warning("Please enter your Gemini API Key to continue.")
