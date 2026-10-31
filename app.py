import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

st.set_page_config(page_title="EduBrain AI", layout="wide", page_icon="🎓")
st.title("🎓 EduBrain AI: Academic Assistant & Quiz Engine")

api_key = st.secrets.get("GEMINI_API_KEY") or st.sidebar.text_input("Enter Gemini API Key", type="password")

def ask_gemini(api_key, prompt):
    genai.configure(api_key=api_key)
    
    candidate_models = ['gemini-1.5-flash', 'gemini-2.0-flash', 'gemini-1.5-pro', 'gemini-pro']
    
    try:
        fetched = [
            m.name.replace("models/", "") 
            for m in genai.list_models() 
            if 'generateContent' in m.supported_generation_methods
        ]
        for f in reversed(fetched):
            if f not in candidate_models:
                candidate_models.insert(0, f)
    except Exception:
        pass

    last_exception = None
    for model_name in candidate_models:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            last_exception = e
            continue
            
    raise last_exception


if api_key:
    uploaded_file = st.file_uploader("Upload Academic PDF Document", type=["pdf"])

    if uploaded_file is not None:
        reader = PdfReader(uploaded_file)
        text = "".join([page.extract_text() or "" for page in reader.pages])

        st.success(f"PDF Uploaded Successfully! Total pages: {len(reader.pages)}")

        tab1, tab2, tab3 = st.tabs(["📝 Summary & Concepts", "🧩 Interactive Quiz", "💬 Q&A Chat"])

        with tab1:
            if st.button("Generate Summary"):
                with st.spinner("Analyzing document..."):
                    try:
                        summary = ask_gemini(api_key, f"Summarize the following academic text into key concepts and bullet points:\n\n{text[:10000]}")
                        st.write(summary)
                    except Exception as e:
                        st.error(f"Error generating summary: {e}")

        with tab2:
            if st.button("Generate 5-Question Quiz"):
                with st.spinner("Creating quiz..."):
                    try:
                        quiz = ask_gemini(api_key, f"Create a 5-question multiple-choice quiz based on this text with correct answers at the end:\n\n{text[:10000]}")
                        st.write(quiz)
                    except Exception as e:
                        st.error(f"Error generating quiz: {e}")

        with tab3:
            user_question = st.text_input("Ask a question about your document:")
            if user_question:
                with st.spinner("Thinking..."):
                    try:
                        ans = ask_gemini(api_key, f"Answer this question based strictly on the text provided.\nQuestion: {user_question}\n\nText:\n{text[:10000]}")
                        st.write(ans)
                    except Exception as e:
                        st.error(f"Error answering question: {e}")
else:
    st.warning("Please configure your GEMINI_API_KEY in Streamlit Secrets or enter it manually in the sidebar.")
