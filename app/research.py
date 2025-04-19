from typing import List, Dict

class ResearchAgent:
    def gather_information(self, profile: Dict) -> List[Dict]:
        """Gather educational resources with proper citations"""
        topic = profile['topic']
        level = profile['knowledge_level']
        
        # Sample resources - in production these would be real API calls
        if "Machine Learning" in topic:
            return [
                {
                    'title': 'Introduction to Machine Learning',
                    'url': 'https://en.wikipedia.org/wiki/Machine_learning',
                    'content': 'Comprehensive overview of machine learning concepts and techniques.'
                },
                {
                    'title': 'Neural Networks and Deep Learning',
                    'url': 'https://neuralnetworksanddeeplearning.com',
                    'content': 'Free online book about neural networks and deep learning.'
                },
                {
                    'title': 'Scikit-learn Documentation',
                    'url': 'https://scikit-learn.org/stable/documentation.html',
                    'content': 'Official documentation for the scikit-learn machine learning library.'
                }
            ]
        else:
            return [
                {
                    'title': f'Wikipedia: {topic}',
                    'url': f'https://en.wikipedia.org/wiki/{topic.replace(" ", "_")}',
                    'content': f'General information about {topic} from Wikipedia.'
                },
                {
                    'title': f'Khan Academy: {topic}',
                    'url': f'https://www.khanacademy.org/search?page_search_query={topic.replace(" ", "+")}',
                    'content': f'Educational resources about {topic} from Khan Academy.'
                }
            ]