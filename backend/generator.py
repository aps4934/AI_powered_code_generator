import google.generativeai as genai

# Set up the API key
API_KEY = "AIzaSyD69AlWbU9hqtDBF_Mle8GT_tEYtBtdUHU"
genai.configure(api_key=API_KEY)

def generate_code(requirement, language="python"):
    """
    Generates code based on user requirements using Google Gemini AI.

    Args:
        requirement (str): The code requirement description
        language (str): The programming language to generate code in

    Returns:
        str: Generated code or error message
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Generate {language} code for the following requirement: {requirement}. Provide only the code without any explanations or markdown formatting. Include comments for clarity if needed."

        response = model.generate_content(prompt)
        code = response.text.strip()

        # Return clean code without markdown formatting

        return code
    except Exception as e:
        return f"# Error generating code: {str(e)}\nprint('An error occurred while generating the code.')"
