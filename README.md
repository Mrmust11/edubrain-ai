
# 🎓 EduBrain AI: Interactive Academic Assistant & Quiz Engine

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlecloud&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

**EduBrain AI** is an LLM-powered educational platform designed to streamline study workflows. By ingesting academic PDFs, EduBrain extracts key concepts, generates automated interactive quizzes, and allows direct context-aware Q&A with any academic paper.

---

## ✨ Key Features

- **📄 PDF Text Extraction:** Upload complex academic documents and extract text seamlessly using `pypdf`.
- **📝 Automated Summarization:** Instantly generate concise key takeaways and bullet-point summaries.
- **🧩 Dynamic Quiz Engine:** Create 5-question multiple-choice quizzes tailored to the uploaded material with automated answer keys.
- **💬 Document Q&A Chat:** Ask specific questions about your document and get real-time answers based strictly on the text context.

---

## 🛠️ Tech Stack

- **Framework:** [Streamlit](https://streamlit.io/)
- **LLM Engine:** [Google Gemini API (`gemini-1.5-flash`)](https://aistudio.google.com/)
- **PDF Processing:** [pypdf](https://pypi.org/project/pypdf/)
- **Language:** Python 3.9+

---

## 🚀 Quick Start (Local Setup)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/edubrain-ai.git](https://github.com/YOUR_USERNAME/edubrain-ai.git)
   cd edubrain-ai

   pip install -r requirements.txt

   streamlit run app.py
