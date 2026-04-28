import google.generativeai as genai

import os

# Set up the API key
API_KEY = os.getenv("GOOGLE_API_KEY", "YOUR_API_KEY")
genai.configure(api_key=API_KEY)

def generate_code(requirement, language="python", model_name="gemini-3.0-flash"):
    """
    Generates code based on user requirements using Google Gemini AI.

    Args:
        requirement (str): The code requirement description
        language (str): The programming language to generate code in

    Returns:
        str: Generated code or error message
    """
    try:
        model = genai.GenerativeModel(model_name)
        prompt = f"Generate {language} code for the following requirement: {requirement}. Provide only the code without any explanations or markdown formatting. Include comments for clarity if needed."

        response = model.generate_content(prompt)
        code = response.text.strip()

        # Clean up markdown formatting if present
        if code.startswith('```') and code.endswith('```'):
            # Remove the first line if it contains language identifier
            lines = code.split('\n')
            if len(lines) > 1 and lines[0].startswith('```'):
                lines = lines[1:]
            if lines and lines[-1].startswith('```'):
                lines = lines[:-1]
            code = '\n'.join(lines).strip()

        return code
    except Exception as e:
        return f"# Error generating code: {str(e)}\nprint('An error occurred while generating the code.')"
