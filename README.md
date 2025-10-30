
# AI Powered Code Generator

An AI-powered web application that generates code based on natural language requirements. Built with Flask for the backend and HTML/CSS/JavaScript for the frontend, this tool leverages Google Gemini AI to create code snippets in various programming languages.

## Features

- **Natural Language Processing**: Input your requirements in plain English and get generated code
- **Multi-Language Support**: Supports 16+ programming languages including Python, JavaScript, Java, C++, C#, PHP, Ruby, Go, Rust, Swift, Kotlin, TypeScript, HTML, CSS, SQL
- **Real-time Code Generation**: Instant code generation with syntax validation
- **User-Friendly Interface**: Clean and intuitive web interface with copy-to-clipboard functionality
- **Team Information**: Meet the developers behind the project
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Code Generation**: Google Gemini AI
- **Styling**: Font Awesome for icons

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aps4934/AI_powered_code_generator
   cd AI_powered_code_generator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. Start the backend server:
   ```bash
   python run.py
   ```

5. Open your browser and go to `http://localhost:5000` to access the frontend.

## Deployment on Render

1. Create a new account on [Render](https://render.com) if you don't have one.

2. Connect your GitHub repository to Render.

3. Create a new Web Service from your repository.

4. Configure the service:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `python run.py`
   - **Root Directory**: Leave blank or set to root if needed

5. Add environment variables:
   - `GOOGLE_API_KEY`: Your Google Gemini API key

6. Deploy the service. Render will build and deploy your application automatically.

7. Once deployed, access your application at the provided URL (e.g., `https://your-app-name.onrender.com`).

## Usage

1. Open the application in your browser
2. Select your preferred programming language from the dropdown
3. Enter your code requirements in the input field (e.g., "Create a function to calculate factorial")
4. Click "Generate Code" to get the generated code
5. Copy the generated code using the copy button and use it in your projects

## API Endpoints

- **POST /generate**: Generate code based on requirements
  - Request body: `{"requirement": "your requirement here", "language": "python"}`
  - Response: `{"generated_code": "generated code here"}`

## Project Structure

```
ai-powered-code-generator/
├── backend/
│   ├── app.py              # Flask application
│   ├── generator.py        # Code generation logic
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html          # Main web page
│   ├── style.css           # Styling
│   ├── script.js           # Frontend JavaScript
│   └── generator.html      # Code generator page
├── run.py                  # Server startup script
├── TODO.md                 # Project tasks
└── README.md               # This file
```

## Team

- **Aditya Pratap Singh** (Full Stack Developer)
  - GitHub: https://github.com/aps4934
  - LinkedIn: https://www.linkedin.com/in/aps4934g/
  - Email: sadityapratap070@gmail.com

- **Achhansh Gupta** (AI/ML Engineer)
  - GitHub: 
  - LinkedIn: https://www.linkedin.com/in/achhansh-gupta-37440b35b/
  - Email: 2k22csaiml32331@gmail.com

- **Anupam Kumar Jha** (Backend Developer)
  - GitHub: https://github.com/Anupam-20
  - LinkedIn: https://www.linkedin.com/in/anupam-kumar-jha
  - Email: jha.anupamkumar24@gmail.com

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Flask and Google Gemini AI
- Icons from Font Awesome
- Special thanks to the development team

---

© 2024 Aditya Pratap Singh & Team | Built with Flask and Google Gemini AI



