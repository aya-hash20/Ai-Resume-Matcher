# AI Resume Matcher

AI Resume Matcher is a web application that compares a candidate's CV with a job or internship description and generates a compatibility score using Natural Language Processing techniques.

The application helps candidates understand how well their CV matches a specific offer by identifying matched keywords, missing keywords, and improvement recommendations.

## Features

- Upload a CV in PDF format
- Paste a job or internship description
- Extract text automatically from the PDF
- Clean and preprocess text data
- Calculate a compatibility score
- Identify matched keywords
- Identify missing keywords
- Generate CV improvement recommendations
- Download a text report with the analysis results

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- PyPDF

## How It Works

1. The user uploads a CV as a PDF file.
2. The user pastes a job or internship description.
3. The application extracts text from the CV.
4. Both texts are cleaned and preprocessed.
5. TF-IDF transforms the texts into numerical vectors.
6. Cosine similarity calculates the compatibility score.
7. The app compares keywords from the job description with the CV.
8. A report is generated with matched keywords, missing keywords, and recommendations.

## Installation

Clone the repository:

```bash
git clone https://github.com/aya-hash20/ai-resume-matcher.git
cd ai-resume-matcher
