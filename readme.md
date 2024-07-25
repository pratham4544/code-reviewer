# Code Reviewer Application

This repository contains a Streamlit application designed to review code files using a language model. The application allows users to upload code files and receive feedback based on their input questions.

## Features

- **Upload code files**: Supports `.py`, `.java`, and `.js` file types.
- **User Input**: Users can provide additional information or specific questions related to the uploaded code.
- **Rate Limiting**: Ensures the application adheres to rate limits, making up to 2 requests per minute.
- **Logging**: Basic logging is configured to capture information and errors.

## Requirements

- Python 3.7 or higher
- Streamlit
- aiohttp
- aiolimiter
- Custom module: `src.helper` containing `ResponseLLM` class

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/pratham4544/code-reviewer.git
    cd code-reviewer
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

3. Upload your code file and provide additional information or questions in the text input.

4. Click the **Submit** button to receive a review summary of the uploaded code.

## Code Overview

- `main()`: Entry point of the application, initializes and runs the main asynchronous function.
- `main_async()`: Manages the Streamlit interface, handling file uploads and user inputs.
- `handle_review_requests(user_question, uploaded_file)`: Fetches the GPT response for the provided user question and uploaded file.
- `fetch_gpt_response(user_question, file_name)`: Core function to interact with the language model, including loading text, creating embeddings, and fetching the response.

## Logging

Basic logging is configured to capture key events and errors:
- Information logs for each request processed.
- Error logs for any issues encountered during processing.

## Rate Limiting

Rate limiting is enforced using `aiolimiter`, allowing up to 2 requests per minute to ensure compliance with usage policies and prevent overloading the system.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to the authors of the `aiolimiter` and `Streamlit` libraries for their excellent tools.

---

For any issues or contributions, feel free to open an issue or submit a pull request on the GitHub repository.

## Example

Here's an example of how to use the application:

1. **Upload a File**: Click on the "Choose a file" button and select a code file (`.py`, `.java`, or `.js`).
2. **Provide Additional Information**: Enter any specific questions or information you want the review to address in the text input field.
3. **Submit**: Click the "Submit" button. The application will process the file and display a review summary.

## Directory Structure
code-reviewer/
│
├── src/
│ └── helper.py # Contains the ResponseLLM class
│
├── app.py # Main application file
├── requirements.txt # Dependencies
└── README.md # This file




