# Simple Resume Parser

This project is a simple resume parser that allows you to extract information from resumes in various formats. Please note that DOC/DOCX files are supported in only Linux environment.

## Installation

To run the project, follow these steps:

1. Create a virtual environment to isolate the project dependencies:

    ```
    python -m venv venv
    ```

2. Activate the virtual environment:

    - For Windows:

      ```
      venv\Scripts\activate
      ```

    - For macOS and Linux:

      ```
      source venv/bin/activate
      ```

3. Install the dependencies listed in `requirements.txt` by running the following command:

    ```
    pip install -r requirements.txt
    ```

4. Install LibreOffice using apt to support DOCX files:

    ```
    sudo apt install libreoffice
    ```
5. Set Environment Variable: If the environment variable is not set, you can set it by running the following command in your terminal:
On Linux or macOS: 
```
export OPENAI_API_KEY='your_api_key_here'
```

On Windows: set OPENAI_API_KEY=your_api_key_here Make sure to replace 'your_api_key_here' with your actual OpenAI API key. You'll need to run this command in the same terminal session before running your Python script.

6. Run the `app.py` file to start the application:

    ```
    python app.py
    ```

## API Endpoints

- Health Check: `/health`

  This endpoint can be used to check the health of the application.

- Upload Resume: `/upload`

  This endpoint allows you to upload a resume file and receive a parsed response.

Please note that the resume parser supports various formats, including PDF, DOC(Supported only on Linux), and TXT.

