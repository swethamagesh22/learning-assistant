import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
from typing import List, Dict
import textwrap
from datetime import datetime
import io

class ReportGenerator:
    def create_report(self, profile: Dict, materials: List[Dict]) -> str:
        """Generate comprehensive report with proper formatting and sources"""
        # Create report structure
        report = f"""
        # {profile['topic']} for {profile['knowledge_level'].capitalize()}s
        
        ## 1. Introduction
        {self._generate_introduction(profile)}
        
        ## 2. Key Concepts
        {self._generate_key_concepts(profile)}
        
        ## 3. Practical Applications
        {self._generate_applications(profile)}
        
        ## 4. Summary
        {self._generate_summary(profile)}
        
        ## 5. Sources
        {self._generate_sources(materials)}
        """
        
        # Add visualization if requested
        if "visual_focused" in profile['preferred_formats']:
            fig = self._create_concept_diagram(profile)
            img_buffer = io.BytesIO()
            fig.savefig(img_buffer, format='png', dpi=150)
            plt.close(fig)
            st.image(img_buffer, use_column_width=True)
        
        return textwrap.dedent(report)

    def _generate_introduction(self, profile: Dict) -> str:
        """Generate introduction paragraph"""
        level = profile['knowledge_level']
        if level == 'beginner':
            return f"""
            {profile['topic']} is a subset of Artificial Intelligence (AI) that involves training models to make 
            predictions or decisions without being explicitly programmed. Instead of hard-coding rules, 
            {profile['topic'].split()[0]} algorithms learn patterns from data.
            """
        elif level == 'intermediate':
            return f"""
            {profile['topic']} builds on statistical and computational techniques to enable systems to 
            automatically learn and improve from experience without being explicitly programmed.
            """
        else:
            return f"""
            Advanced {profile['topic']} involves developing sophisticated models that can extract complex 
            patterns from high-dimensional data, often using deep neural networks and other 
            state-of-the-art techniques.
            """

    def _generate_key_concepts(self, profile: Dict) -> str:
        """Generate key concepts section"""
        topic = profile['topic']
        if "Machine Learning" in topic:
            return """
            ### 2.1 Supervised Learning
            In supervised learning, the algorithm learns to predict outputs from input data based on example input-output pairs.
            
            - **Regression**: Predicts continuous outputs (e.g., housing prices)
            - **Classification**: Predicts discrete outputs (e.g., spam/not spam)
            
            ### 2.2 Unsupervised Learning
            Finds patterns in data without prior labeling.
            
            - **Clustering**: Groups similar data points (e.g., customer segmentation)
            - **Dimensionality Reduction**: Reduces features while retaining information (e.g., PCA)
            
            ### 2.3 Neural Networks
            Inspired by the human brain, consisting of interconnected nodes or "neurons":
            
            - **Input Layer**: Receives input data
            - **Hidden Layers**: Process data and extract features
            - **Output Layer**: Produces final output
            - **Training Process**: Forward propagation, backpropagation, gradient descent
            """
        else:
            return "Key concepts would be generated based on the specific topic."

    def _generate_applications(self, profile: Dict) -> str:
        """Generate practical applications section"""
        if "Machine Learning" in profile['topic']:
            return """
            - **Image Recognition**: CNNs identify objects in images
            - **Speech Recognition**: RNNs/LSTMs transcribe speech to text
            - **Recommender Systems**: Suggest products based on user behavior
            """
        else:
            return "Practical applications would be generated based on the specific topic."

    def _generate_summary(self, profile: Dict) -> str:
        """Generate summary paragraph"""
        if "Machine Learning" in profile['topic']:
            return f"""
            {profile['topic']} enables computers to learn from and make predictions on data. 
            Neural networks are a powerful technique inspired by the human brain. 
            They learn through training processes like forward propagation and backpropagation.
            """
        else:
            return f"A summary of key {profile['topic']} concepts and applications."

    def _generate_sources(self, materials: List[Dict]) -> str:
        """Generate properly formatted sources section"""
        return "\n".join(
            f"- {m['title']}: {m['url']}" 
            for m in materials
        )

    def _create_concept_diagram(self, profile: Dict) -> plt.Figure:
        """Create concept diagram for the topic"""
        plt.switch_backend('Agg')
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if "Machine Learning" in profile['topic']:
            G = nx.DiGraph()
            G.add_edges_from([
                ("Input Data", "Preprocessing"),
                ("Preprocessing", "Model Training"),
                ("Model Training", "Evaluation"),
                ("Evaluation", "Deployment")
            ])
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=2000, 
                    node_color="skyblue", font_size=10, ax=ax)
            plt.title("Machine Learning Pipeline", pad=20)
        else:
            G = nx.Graph()
            G.add_node(profile['topic'])
            for interest in profile['interests']:
                G.add_edge(profile['topic'], interest)
            nx.draw(G, with_labels=True, node_color="lightgreen", ax=ax)
            plt.title(f"{profile['topic']} Concept Map", pad=20)
        
        return fig

    def update_report(self, report: str, feedback: str) -> str:
        """Update report with user feedback"""
        return f"""
        {report}
        
        ---
        
        **User Feedback Implemented:**
        {feedback}
        """