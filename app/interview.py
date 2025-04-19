import streamlit as st
from typing import Dict

class LearningInterview:
    def conduct_interview(self, topic: str) -> Dict:
        """Interactive learning profile builder with focused output"""
        st.session_state.profile = {
            'topic': topic,
            'interests': [],
            'knowledge_level': 'beginner',
            'preferred_formats': [],
            'word_count': 300,  # Default word count
            'interview_complete': False
        }
        
        with st.sidebar:
            st.header("Personalize Your Learning")
            
            # 1. Specific Interest Selection
            st.subheader("1. Focus Areas")
            interest_options = {
                "Fundamentals": ["Core concepts", "Basic principles"],
                "Applications": ["Real-world uses", "Case studies"],
                "Technical": ["Math behind it", "Algorithms"],
                "History": ["Origins", "Key figures"]
            }
            selected_interest = st.selectbox(
                "What aspect interests you most?",
                options=list(interest_options.keys())
            )
            st.session_state.profile['interests'] = interest_options[selected_interest]
            
            # 2. Knowledge Level with Word Count Mapping
            st.subheader("2. Your Knowledge Level")
            level_map = {
                "🧠 Beginner (300 words)": ("beginner", 300),
                "📚 Intermediate (500 words)": ("intermediate", 500),
                "🎓 Advanced (800 words)": ("advanced", 800)
            }
            level_choice = st.radio(
                "Select your level:",
                options=list(level_map.keys())
            )
            level, word_count = level_map[level_choice]
            st.session_state.profile.update({
                'knowledge_level': level,
                'word_count': word_count
            })
            
            # 3. Learning Format with Specific Output
            st.subheader("3. Preferred Learning Style")
            format_output_map = {
                "📝 Text": "text_only",
                "📊 Visuals": "visual_focused",
                "🎥 Video": "video_links",
                "🔢 Interactive": "interactive_elements"
            }
            format_choice = st.selectbox(
                "How do you learn best?",
                options=list(format_output_map.keys())
            )
            st.session_state.profile['preferred_formats'] = [format_output_map[format_choice]]
            
            if st.button("Save Preferences", type="primary"):
                st.session_state.profile['interview_complete'] = True
                st.success("Preferences saved!")
        
        return st.session_state.profile