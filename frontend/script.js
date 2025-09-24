document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('codeForm');
    const loadingDiv = document.getElementById('loading');
    const resultDiv = document.getElementById('result');
    const generatedCodeDiv = document.getElementById('generatedCode');
    const copyBtn = document.getElementById('copyBtn');
    const toast = document.getElementById('toast');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();

        const language = document.getElementById('language').value;
        const requirement = document.getElementById('requirement').value.trim();

        if (!language) {
            showToast('Please select a programming language.', 'error');
            return;
        }

        if (!requirement) {
            showToast('Please enter a code requirement.', 'error');
            return;
        }

        // Show loading state
        loadingDiv.style.display = 'block';
        resultDiv.style.display = 'none';

        try {
            const response = await fetch('http://localhost:5000/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ requirement: requirement, language: language }),
            });

            const data = await response.json();

            // Hide loading state
            loadingDiv.style.display = 'none';

            if (response.ok) {
                generatedCodeDiv.textContent = data.generated_code;
                resultDiv.style.display = 'block';
                // Scroll to result
                resultDiv.scrollIntoView({ behavior: 'smooth' });
            } else {
                showToast(`Error: ${data.error}`, 'error');
            }
        } catch (error) {
            loadingDiv.style.display = 'none';
            showToast(`Network error: ${error.message}`, 'error');
        }
    });

    // Copy to clipboard functionality
    copyBtn.addEventListener('click', function() {
        const code = generatedCodeDiv.textContent;

        if (navigator.clipboard) {
            navigator.clipboard.writeText(code).then(function() {
                showToast('Code copied to clipboard!');
            }).catch(function(err) {
                fallbackCopyTextToClipboard(code);
            });
        } else {
            fallbackCopyTextToClipboard(code);
        }
    });

    function fallbackCopyTextToClipboard(text) {
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.top = '0';
        textArea.style.left = '0';
        textArea.style.position = 'fixed';
        textArea.style.opacity = '0';

        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();

        try {
            const successful = document.execCommand('copy');
            if (successful) {
                showToast('Code copied to clipboard!');
            } else {
                showToast('Failed to copy code.', 'error');
            }
        } catch (err) {
            showToast('Failed to copy code.', 'error');
        }

        document.body.removeChild(textArea);
    }

    function showToast(message, type = 'success') {
        toast.className = `toast ${type}`;
        toast.querySelector('span').textContent = message;
        toast.classList.add('show');

        setTimeout(function() {
            toast.classList.remove('show');
        }, 3000);
    }

    // Add some visual feedback for form interactions
    const textarea = document.getElementById('requirement');
    const button = document.querySelector('.generate-btn');

    textarea.addEventListener('input', function() {
        if (this.value.trim()) {
            button.style.opacity = '1';
        } else {
            button.style.opacity = '0.7';
        }
    });

    // Initialize button state
    button.style.opacity = textarea.value.trim() ? '1' : '0.7';
});
