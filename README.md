# 🧠 Interactive Learning Assistant

## Overview
An AI-powered learning system designed to provide personalized, context-aware educational assistance across various topics.

## 🌟 Features
- Interactive AI-driven research
- Personalized learning experiences
- Multi-topic support
- Web-based context retrieval
- Adaptive response generation

## 🛠 Technologies Used
- Python 3.10+
- Streamlit
- Hugging Face Transformers
- LangChain
- DuckDuckGo Search API

## 📦 Prerequisites
- Python 3.10 or higher
- pip
- Virtual environment (recommended)

## 🚀 Installation

### Virtual Environment Setup
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Docker Setup
```bash
# Build and run the application
docker-compose up --build
```

## 🖥 Usage

### Running the Application
```bash
# Activate virtual environment
source venv/bin/activate

# Run Streamlit app
streamlit run src/app/main.py
```

## 📝 Project Structure
```
interactive-learning-assistant/
├── app/
│   ├── main.py                 # Streamlit application entry point
│   ├── interview.py            # Learning interview module
│   ├── research.py             # Web research and information gathering
│   └── report_generator.py     # Personalized report creation
├── requirements.txt            # Project dependencies
├── .env                        # Environment configuration
├── Dockerfile                  # Docker configuration
├── .dockerignore               # Docker ignore file
├── CONTRIBUTING.md             # Contribution guidelines
└── README.md                   # Project documentation
```

### Directory Breakdown
- **`app/`**: Core application logic
  - `main.py`: Streamlit web interface
  - `interview.py`: AI-driven learning profile generation
  - `research.py`: Web research and information retrieval
  - `report_generator.py`: Personalized content creation


- **`docs/`**: Extended documentation
  - Provides in-depth technical details
  - Architectural decision records

### Configuration Files
- `requirements.txt`: Python dependency management
- `.env`: Secure environment configuration
- `Dockerfile`: Containerization setup
- `.dockerignore`: Build optimization

## 🔍 How It Works
1. Select a learning topic
2. Choose your learning level
3. Ask questions or select from suggested prompts
4. Receive AI-generated, context-aware responses

## 🚧 Limitations
- Responses depend on web search results
- Limited by the underlying language model
- Potential for occasional irrelevant responses

## 🔮 Future Roadmap
- Implement more advanced context tracking
- Add more learning topics
- Improve response accuracy
- Create user feedback mechanism

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License
MIT License

## 👥 Authors
- [SwethaMagesh]

## 🙏 Acknowledgments
- Hugging Face
- Streamlit
- LangChain Community 

## 🛠 Troubleshooting

### Docker Issues on Mac

#### Malware and Security Warnings
If you encounter security warnings or malware alerts when running Docker on Mac:

1. **Gatekeeper Verification**:
   - Right-click the Docker application
   - Select "Open" from the context menu
   - Click "Open" in the security dialog

2. **System Preferences**:
   - Go to System Preferences > Security & Privacy
   - Click "Allow" for the Docker application

3. **Temporary Workaround**:
   ```bash
   # Disable Gatekeeper temporarily (use with caution)
   sudo spctl --master-disable
   ```

#### Common Docker Errors
- **Permission Denied**: Ensure you have the latest Docker Desktop
- **Volume Mount Issues**: Check file permissions and Docker settings
- **Network Problems**: Restart Docker Desktop

### Hugging Face API Key Configuration

#### API Key Setup
1. **Create Hugging Face Account**:
   - Visit [Hugging Face](https://huggingface.co/)
   - Create an account
   - Generate an API token

2. **Environment Configuration**:
   ```bash
   # Create .env file in project root
   touch .env

   # Add your Hugging Face API key
   echo "HUGGINGFACE_API_KEY=your_api_key_here" >> .env
   ```

3. **Potential API Key Issues**:
   - Ensure API key is correctly copied
   - Check API key permissions
   - Verify network connectivity

#### Troubleshooting API Errors
- **Authentication Failures**:
  ```python
  # Verify API key in your code
  from huggingface_hub import login

  try:
      login(token="YOUR_API_KEY")
  except Exception as e:
      print(f"API Key Error: {e}")
  ```

### Common Installation Pitfalls

#### Python Version Compatibility
- Ensure you're using Python 3.10+
- Use `pyenv` or `conda` for version management

```bash
# Check Python version
python --version

# Create compatible virtual environment
python3.10 -m venv venv
```

#### Dependency Conflicts
```bash
# Update pip and setuptools
pip install --upgrade pip setuptools

# Clean install dependencies
pip install -r requirements.txt --no-cache-dir
```

### Debugging Tips

1. **Verbose Logging**:
   ```bash
   # Run with increased verbosity
   streamlit run src/app/main.py --logger.level=debug
   ```

2. **Check System Requirements**:
   - Minimum 8GB RAM recommended
   - Sufficient disk space
   - Stable internet connection


### Disclaimer
This project is experimental. Responses are generated using AI and may not always be 100% accurate. 