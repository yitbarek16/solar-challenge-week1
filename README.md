# solar-challenge-week1 Task 1 Setup
**Repository**: [github.com/yitbarek16/solar-challenge-week1](https://github.com/yitbarek16/solar-challenge-week1)  
**Branch**: `setup-task` → `main`  

## Environment Setup

### Prerequisites
- Python 3.9+
- Git 2.30+
- VS Code (recommended)

### 1. Clone & Initialize

git clone https://github.com/yitbarek16/solar-challenge-week1.git
cd solar-challenge-week1
git checkout setup-task 

### 2. Python Virtual Environment
#### Create environment
python -m venv venv

#### Activate (Windows)
.\venv\Scripts\activate

#### Activate (Mac/Linux)
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Structure Creation
mkdir -p .github/workflows .vscode notebooks tests scripts src data

#### Configuration
touch .gitignore requirements.txt .vscode/settings.json

#### CI/CD Pipeline
touch .github/workflows/unittests.yml

#### Python packages
touch notebooks/__init__.py scripts/__init__.py tests/__init__.py

### 5.Workflow Demonstration
git checkout main

git merge setup-task --no-ff

git push origin main
