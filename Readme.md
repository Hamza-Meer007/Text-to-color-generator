
# Text to Color Generator

This project is a web application that transforms text input into corresponding RGB color values using a pre-trained deep learning model. The application consists of a Flask backend written in Python and a frontend built with HTML, CSS, and JavaScript, styled with Tailwind CSS.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Text-to-Color Conversion**: Converts any text input into an RGB color code.
- **Frontend Interface**: User-friendly interface for entering text and displaying the generated color.
- **Copy to Clipboard**: Option to copy the RGB color value to the clipboard.
- **Loading State**: Visual indicator during the color generation process.
- **Error Handling**: Displays appropriate error messages for invalid input or server errors.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.6+**: Download Python from the [official website](https://www.python.org/downloads/).
- **pip**: Python package installer (usually included with Python installations).


## Installation

Follow these steps to set up the project locally:

1.  **Clone the Repository**

    ```
    git clone https://github.com/Hamza-Meer007/Text-to-color-generator.git
    cd Text-TO-COLOR-GENERATOR
    ```

2.  **Create a Virtual Environment**

    It is recommended to create a virtual environment to manage project dependencies.

    ```
    python -m venv venv
    ```

    Activate the virtual environment:

    -   On Windows:

        ```
        venv\Scripts\activate
        ```

    -   On macOS and Linux:

        ```
        source venv/bin/activate
        ```

3.  **Install Python Dependencies**

    Install the required Python packages using pip:

    ```
    pip install -r requirements.txt
    ```


## Usage

1.  **Run the Flask Application**

    Ensure your virtual environment is activated and run the Flask application:

    ```
    python main.py
    ```

    The application will start, and you should see a message indicating the server is running (usually on `http://127.0.0.1:5000`).

2.  **Open the Application in Your Browser**

    Open your web browser and navigate to the address provided by the Flask application (e.g., `http://127.0.0.1:5000`).

3.  **Enter Text and Generate Color**

    -   Enter any text in the input field.
    -   Click the "Generate Color" button.
    -   The generated color will be displayed, along with its RGB value.

4.  **Copy RGB Value**

    Click on the color preview to copy the RGB value to your clipboard.

## Project Structure

The project structure is organized as follows:

```
text-to-color-generator/
├── main.py             # Flask application file
├── static/            # Static files
│   ├── index.html     # Frontend HTML file
│   ├── icon_color.ico # Favicon
├── model.h5           # Pre-trained model weights
├── tokenizer.json     # Tokenizer configuration
├── README.md          # Documentation
├── venv/              # Virtual environment directory
```

## Model Training

The model used in this project is a deep learning model trained to associate text inputs with RGB color values. The model architecture consists of LSTM layers followed by dense layers to predict the RGB values.

To retrain or fine-tune the model, you would need:

1.  **Data**: A dataset of text strings and corresponding RGB color values.
2.  **Training Script**: A Python script to train the model using TensorFlow/Keras.
3.  **Tokenizer**: Use `tensorflow.keras.preprocessing.text.Tokenizer` to convert text data into numerical sequences. Save the tokenizer configuration to a JSON file for use in the Flask application.

The included `model.h5` and `tokenizer.json` files are the pre-trained model weights and tokenizer configuration, respectively.

## Contributing

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Push your changes to your fork.
5.  Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for more information.

