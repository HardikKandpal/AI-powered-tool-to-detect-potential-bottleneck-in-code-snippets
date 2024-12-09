# AI-powered-tool-to-detect-potential-bottleneck-in-code-snippets

## Features
- **AI-powered code analysis**: Uses a pre-trained **CodeBERT model** to analyze code for common bottlenecks such as inefficient algorithms, redundant code, and excessive function calls. To get better performance it was also finetuned on CodeXGLUE dataset. (refer code-assignment.ipynb)
- **Optimization suggestions**: Provides actionable suggestions for improving code based on detected issues.
- **User-friendly interface**: A simple and intuitive Streamlit interface where users can upload their Python code files and receive optimization suggestions instantly.


![Screenshot 2024-12-09 104926](https://github.com/user-attachments/assets/20a47b2b-2acf-4d21-ac72-106475aab84e)

**Simple UI**
Users can easily input their code snippet file to test for bottlenecks
![Screenshot 2024-12-09 104953](https://github.com/user-attachments/assets/e5df4ec0-e81f-43ca-9fa2-2d89ff85ab03)

**Analysis & Optimization**
It suggests the potential bottleneck analysis and also the optimization to fix that

**test 1**
![Screenshot 2024-12-09 105004](https://github.com/user-attachments/assets/0526d6de-036a-4226-8f41-80d5ef0aa81a)

**test 2**
![Screenshot 2024-12-09 105038](https://github.com/user-attachments/assets/bc66841c-bb72-40e6-adea-83320ebbb384)

## Assumptions and Limitations
# Assumptions
The code uploaded by the user is written in Python.
The CodeBERT model is capable of understanding the uploaded code, although its suggestions may not be perfect for all codebases.
The user is familiar with basic Python programming and can apply the optimization suggestions to improve their code.

# Limitations
The model's suggestions are based on common patterns and might not be applicable for every codebase. The tool is designed to offer suggestions for common bottlenecks, but it cannot guarantee that every suggestion will improve performance in all cases.
The analysis is simplified, and it does not perform a deep profiling of the code execution (e.g., measuring runtime performance).
The tool currently works with Python code and is not intended for other programming languages.
## How to Run the Project

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.7 or above
- `pip` (Python package installer)
- A web browser to access the Streamlit app

### Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/code-analysis-optimization-tool.git
