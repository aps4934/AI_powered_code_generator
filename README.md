# AI Powered Code Generator

An AI-powered web application that generates code based on natural language requirements. Built with Flask for the backend and HTML/CSS/JavaScript for the frontend, this tool leverages simple rule-based logic to create code snippets in various programming languages.

## Features

- **Natural Language Processing**: Input your requirements in plain English and get generated code
- **Multi-Language Support**: Supports Python, JavaScript, and other languages
- **Real-time Code Generation**: Instant code generation with syntax validation
- **User-Friendly Interface**: Clean and intuitive web interface
- **Team Information**: Meet the developers behind the project
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Code Generation**: Custom rule-based system
- **Styling**: Font Awesome for icons

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aps4934/AI_powered_code_generator
   cd ai-powered-code-generator
   ```

2. Navigate to the backend directory and install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   cd ..
   ```

3. Start the backend server:
   ```bash
   python run.py
   ```

4. Open your browser and go to `http://localhost:5000` to access the frontend.

## Usage

1. Open the application in your browser
2. Enter your code requirements in the input field (e.g., "Create a Python function to calculate factorial")
3. Click "Generate Code" to get the generated code
4. Copy and use the generated code in your projects

## API Endpoints

- **POST /generate**: Generate code based on requirements
  - Request body: `{"requirement": "your requirement here"}`
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



