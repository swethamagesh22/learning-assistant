import streamlit as st
from interview import LearningInterview
from research import ResearchAgent
from report_generator import ReportGenerator
from datetime import datetime

def main():
    """
    Main application entry point for the Enhanced Learning Assistant.
    
    Responsibilities:
    1. Configure Streamlit page
    2. Initialize application components
    3. Handle user input and learning workflow
    4. Generate and display personalized learning reports
    5. Provide feedback mechanism
    """
    # Configure Streamlit page with custom settings
    st.set_page_config(
        page_title="Enhanced Learning Assistant",
        layout="centered",
        initial_sidebar_state="expanded"
    )
    
    # Display main application title and description
    st.title("Enhanced Interactive Learning Assistant")
    st.write("Get personalized learning materials based on your needs")
    
    # Initialize application components only once in session state
    if 'components' not in st.session_state:
        st.session_state.components = {
            'interviewer': LearningInterview(),  # Personalized learning interview
            'researcher': ResearchAgent(),       # Information gathering agent
            'report_gen': ReportGenerator()      # Report generation and modification
        }
    
    # Topic input section with clear prompt
    topic = st.text_input("What do you want to learn about?", key="topic_input")
    
    if topic:
        # Conduct personalized learning interview
        profile = st.session_state.components['interviewer'].conduct_interview(topic)
        
        if profile.get('interview_complete'):
            st.write(f"**You're learning {topic}**")
            
            # Generate learning report with spinner for user feedback
            with st.spinner(f"Generating your {profile['word_count']}-word report..."):
                # Gather relevant learning materials
                materials = st.session_state.components['researcher'].gather_information(profile)
                
                # Create personalized report
                report = st.session_state.components['report_gen'].create_report(profile, materials)
            
            # Display generated report
            st.markdown("## Your Learning Report")
            st.markdown(f"The report should be around {profile['word_count']} words.")
            st.markdown(report)
            
            # Interactive feedback system
            with st.expander("Provide feedback or request changes"):
                feedback = st.text_area(
                    "How can we improve this report?",
                    height=100,
                    key="feedback_input"
                )
                
                # Feedback submission and processing
                if st.button("Submit Feedback"):
                    if feedback.strip():
                        # Update report based on user feedback
                        updated_report = st.session_state.components['report_gen'].update_report(
                            report, feedback
                        )
                        st.session_state.report = updated_report
                        st.success("✅ Your feedback has been recorded!")
                        st.rerun()
                    else:
                        st.warning("Please enter your feedback before submitting")

if __name__ == "__main__":
    main()