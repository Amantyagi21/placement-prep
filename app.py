import streamlit as st
import os
import PyPDF2
from database import init_db, log_activity, get_stats

init_db()

st.set_page_config(
    page_title="AI Placement Prep",
    page_icon="🎯",
    layout="wide"
)

st.title("AI Placement Preparation Assistant")
st.subheader("Prepare for your placement with AI!")

st.sidebar.title("Menu")
option = st.sidebar.selectbox(
    "Choose a feature:",
    [
        "Home",
        "Resume Analyzer",
        "Mock Interview",
        "DSA Practice",
        "HR Questions",
        "Aptitude Practice",
        "PDF Summarizer",
        "Progress Dashboard"
    ]
)

if option == "Home":
    st.markdown("""
    ### Welcome! This app will help you:
    - Analyze your resume
    - Practice mock interviews
    - Practice DSA questions
    - Prepare HR questions
    - Practice aptitude tests
    - Summarize PDF notes
    """)
    st.info("Choose a feature from the left menu!")

elif option == "Resume Analyzer":
    st.header("Resume Analyzer + ATS Score")
    uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")
    job_desc = st.text_area("Paste Job Description here:", height=200)
    if st.button("Analyze Resume"):
        if uploaded_file and job_desc:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            resume_text = ""
            for page in pdf_reader.pages:
                resume_text += page.extract_text()
            with st.spinner("AI is analyzing your resume..."):
                from resume_analyzer import analyze_resume
                result = analyze_resume(resume_text, job_desc)
            st.success("Analysis Complete!")
            st.write(result)
            log_activity("Resume Analyzer")
        else:
            st.warning("Please upload resume and paste job description!")

elif option == "Mock Interview":
    st.header("Mock Interview Practice")
    job_role = st.selectbox(
        "Select Job Role:",
        ["Software Engineer", "Data Analyst", "Web Developer",
         "Data Scientist", "Product Manager", "DevOps Engineer"]
    )
    num_q = st.slider("Number of questions:", 3, 10, 5)
    if st.button("Generate Questions"):
        with st.spinner("Generating questions..."):
            from mock_interview import generate_questions
            questions = generate_questions(job_role, num_q)
        st.session_state.questions = questions
        st.write(questions)
        log_activity("Mock Interview")
    if "questions" in st.session_state:
        st.divider()
        st.subheader("Practice your answer:")
        question = st.text_input("Enter the question you want to practice:")
        answer = st.text_area("Your answer:", height=150)
        if st.button("Get Feedback"):
            if question and answer:
                with st.spinner("AI is evaluating..."):
                    from mock_interview import evaluate_answer
                    feedback = evaluate_answer(question, answer, job_role)
                st.success("Feedback ready!")
                st.write(feedback)

elif option == "DSA Practice":
    st.header("DSA Practice")
    col1, col2 = st.columns(2)
    with col1:
        topic = st.selectbox(
            "Select Topic:",
            ["Arrays", "Strings", "Linked List", "Trees",
             "Graphs", "Dynamic Programming", "Sorting",
             "Binary Search", "Stack/Queue", "Recursion"]
        )
    with col2:
        difficulty = st.selectbox(
            "Select Difficulty:",
            ["Easy", "Medium", "Hard"]
        )
    if st.button("Generate Problem"):
        with st.spinner("Generating DSA problem..."):
            from dsa_practice import generate_dsa_question
            problem = generate_dsa_question(topic, difficulty)
        st.session_state.dsa_problem = problem
        st.markdown(problem)
        log_activity("DSA Practice")
    if "dsa_problem" in st.session_state:
        st.divider()
        st.subheader("Write your solution:")
        user_solution = st.text_area(
            "Write your code here:",
            height=200,
            placeholder="Write your solution in any language..."
        )
        if st.button("Check Solution"):
            if user_solution:
                with st.spinner("AI is reviewing your solution..."):
                    from dsa_practice import check_solution
                    feedback = check_solution(st.session_state.dsa_problem, user_solution)
                st.success("Review complete!")
                st.write(feedback)

elif option == "HR Questions":
    st.header("HR Questions Practice")
    col1, col2 = st.columns(2)
    with col1:
        experience = st.selectbox(
            "Experience Level:",
            ["Fresher", "1-2 years", "3-5 years"]
        )
    with col2:
        company = st.selectbox(
            "Company Type:",
            ["Service Company", "Product Startup", "MNC", "Tech Giant"]
        )
    if st.button("Generate HR Questions"):
        with st.spinner("Generating HR questions..."):
            from hr_questions import generate_hr_questions
            questions = generate_hr_questions(experience, company)
        st.write(questions)
        log_activity("HR Questions")
    st.divider()
    st.subheader("Get Perfect Answer")
    question = st.text_input("Enter any HR question:")
    background = st.text_area(
        "Your background (brief):",
        height=100,
        placeholder="BTech CSE student, built AI projects, know Python and Java..."
    )
    if st.button("Get Perfect Answer"):
        if question and background:
            with st.spinner("Generating perfect answer..."):
                from hr_questions import get_hr_answer
                answer = get_hr_answer(question, background)
            st.success("Here is your perfect answer!")
            st.write(answer)
            log_activity("HR Questions")

elif option == "Aptitude Practice":
    st.header("Aptitude Practice")
    topic = st.selectbox(
        "Select Topic:",
        [
            "Number System", "Percentages", "Time and Work",
            "Time Speed Distance", "Profit and Loss",
            "Ratio and Proportion", "Probability",
            "Logical Reasoning", "Data Interpretation", "Verbal Ability"
        ]
    )
    num_q = st.slider("Number of questions:", 3, 10, 5)
    if st.button("Generate Questions"):
        with st.spinner("Generating aptitude questions..."):
            from aptitude import generate_aptitude_questions
            questions = generate_aptitude_questions(topic, num_q)
        st.success("Questions ready!")
        st.write(questions)
        log_activity("Aptitude Practice")

elif option == "PDF Summarizer":
    st.header("PDF Notes Summarizer")
    uploaded_pdf = st.file_uploader("Upload your PDF notes:", type="pdf")
    summary_type = st.selectbox(
        "Summary type:",
        ["Brief Summary", "Detailed Summary", "Key Points", "Study Notes"]
    )
    if st.button("Summarize"):
        if uploaded_pdf:
            pdf_reader = PyPDF2.PdfReader(uploaded_pdf)
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()
            with st.spinner("AI is summarizing..."):
                from pdf_summarizer import summarize_pdf
                summary = summarize_pdf(pdf_text, summary_type)
            st.success("Summary ready!")
            st.write(summary)
            log_activity("PDF Summarizer")
        else:
            st.warning("Please upload a PDF first!")

elif option == "Progress Dashboard":
    st.header("Progress Dashboard")
    stats, recent = get_stats()
    if stats:
        st.subheader("Your Activity Summary")
        col1, col2, col3 = st.columns(3)
        total = sum([s[1] for s in stats])
        with col1:
            st.metric("Total Sessions", total)
        with col2:
            st.metric("Features Used", len(stats))
        with col3:
            st.metric("Last Active", recent[0][2] if recent else "N/A")
        st.divider()
        st.subheader("Activity Breakdown")
        for stat in stats:
            st.write(f"**{stat[0]}** — {stat[1]} sessions")
            st.progress(stat[1] / total)
        st.divider()
        st.subheader("Recent Activity")
        for r in recent:
            st.write(f"• {r[2]} — {r[1]}")
    else:
        st.info("No activity yet! Start using features to track your progress.") 