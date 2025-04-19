# Contributing to Enhanced Learning Assistant

## Welcome Contributors! 🌟

We're thrilled that you're interested in contributing to the Enhanced Learning Assistant. This document provides guidelines for contributing to our project.

## Code of Conduct

Please be respectful, inclusive, and considerate of others. We aim to maintain a welcoming environment for all contributors.

## How to Contribute

### 1. Reporting Issues
- Use GitHub Issues
- Provide detailed description
- Include reproduction steps
- Specify your environment details

#### Issue Template
```markdown
### Description
[Detailed description of the issue]

### Steps to Reproduce
1. 
2. 
3. 

### Expected Behavior
[What you expected to happen]

### Actual Behavior
[What actually happened]

### Environment
- OS: 
- Python Version: 
- Package Versions: 
```

### 2. Feature Requests
- Open a GitHub Issue
- Describe the feature
- Explain the use case
- Provide potential implementation suggestions

### 3. Pull Request Process
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write tests
5. Ensure all tests pass
6. Submit pull request

#### Pull Request Template
```markdown
## Description
[Describe your changes]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## How Tested
[Describe tests performed]

## Checklist
- [ ] I have performed a self-review
- [ ] I have commented my code
- [ ] I have added tests
- [ ] Documentation updated
```

## Development Setup

### Prerequisites
- Python 3.9+
- pip or conda
- Git

### Local Development
```bash
# Clone repository
git clone https://github.com/yourusername/learning-assistant.git

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install dev dependencies
pip install -r requirements-dev.txt
```

## Running Tests
```bash
# Run unit tests
pytest tests/

# Run coverage
pytest --cov=app tests/

# Run type checking
mypy app/
```

## Code Style
- Follow PEP 8 guidelines
- Use type hints
- Write docstrings
- Use black for formatting
- Use flake8 for linting

## Commit Message Guidelines
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, missing semicolons
- `refactor`: Code restructuring
- `test`: Adding/modifying tests
- `chore`: Maintenance tasks

## Review Process
- Maintainers will review pull requests
- Feedback will be provided
- At least one approval required for merge

## Security
- Report security issues privately
- Do not open public issues for security vulnerabilities

## Recognition
Contributors will be recognized in our README and documentation!

## Questions?
Open an issue or contact maintainers directly.

Happy Contributing! 🚀 