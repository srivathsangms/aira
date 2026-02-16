# AIRA - AI Resume Analyzer 📄

**AIRA** (Artificial Intelligence Resume Analyzer) is a powerful, modern web application designed to help job seekers optimize their resumes. Powered by Google's Gemini 2.5 Flash model, AIRA provides instant, detailed feedback, scoring, and sector identification to help you land your dream job.


<table>
  <tr>
    <td align="center">
      <img src="https://github.com/srivathsangms/aira/blob/main/aira_ss1.jpeg" alt="AIRA Dashboard" width="400"/>
      <br>
      <i>Dashboard & Settings</i>
    </td>
    <td align="center">
      <img src="https://github.com/srivathsangms/aira/blob/main/aira_ss2.jpeg" alt="Analysis Results" width="400"/>
      <br>
      <i>Analysis Results</i>
    </td>
  </tr>
</table>

## 🚀 Features

- **Instant Analysis**: Upload your resume (PDF) and get feedback in seconds.
- **📊 Smart Scoring**: Receive a rating out of 10 based on industry standards.
- **🏢 Sector Detection**: Automatically identifies the professional sector of the candidate.
- **💡 Detailed Insights**:
  - **Strengths**: What makes your resume stand out.
  - **Weaknesses**: Areas that need improvement.
  - **Actionable Advice**: Specific tips to enhance your CV.
- **🎯 Interview Prep**: Get tailored interview questions based on your profile.
- **✨ Modern UI**: A sleek, high-contrast dark mode interface designed for clarity and focus.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Model**: [Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/)
- **PDF Processing**: [pdfplumber](https://github.com/jsvine/pdfplumber)
- **Language**: Python 3.12+

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/srivathsangms/aira.git
   cd aira
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Key**
   - The application currently uses a hardcoded API key for demonstration.
   - For production, it is recommended to replace the key in `app.py` or use environment variables.

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## 📂 Project Structure

```
aira/
├── app.py              # Main application logic and UI
├── chatbot.py          # AI interaction logic (Gemini API)
├── requirements.txt    # Python dependencies
├── .streamlit/
│   └── config.toml     # Streamlit theme configuration
└── README.md           # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
*Built with ❤️ by Srivathsan GMS*
