# Sign Language to Text Using CNN

A deep learning project designed to translate sign language gestures into text using a Convolutional Neural Network (CNN). This tool aims to bridge communication barriers for individuals with hearing or speech impairments.

## Features
- Recognizes and translates hand gestures into corresponding text.
- Utilizes a robust CNN architecture for high accuracy.
- User-friendly interface for seamless interaction.
- Suitable for educational, professional, and personal use.

---

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.7 or later
- Required libraries (listed in `requirements.txt`)

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Ruksana0303/Sign_Language_To_Text_Using_CNN.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Sign_Language_To_Text_Using_CNN
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

---

## Dataset
This project uses a custom dataset of sign language images. You can download the dataset [here](#) (add dataset link).

### Dataset Details
- Classes: Alphabets
- Format: Images in `.jpg` or `.png` format.
- Preprocessing: Images resized to a fixed size (e.g., 64x64).

---

## Model Architecture
The CNN model used in this project includes:
- **Input Layer:** Preprocessed image data.
- **Hidden Layers:** Convolutional layers with ReLU activation, max-pooling layers.
- **Output Layer:** Fully connected layer with softmax activation.

### Training
- Optimizer: Adam
- Loss Function: Categorical Cross-Entropy


---

## Usage
1. Place your input images (hand gestures) in the `input` directory.
2. Run the script and view predictions in the terminal or GUI:
   ```bash
   python predict.py
   ```
3. Predictions will be saved to the `output` directory.

---

## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes and push:
   ```bash
   git add .
   git commit -m "Add your message here"
   git push origin feature-branch
   ```
4. Submit a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the license terms.

---

## Acknowledgments
- [Ruksana0303](https://github.com/Ruksana0303) for initiating this project.
- [Kaggle](https://www.kaggle.com) for datasets (if used).
- Open-source contributors and libraries.

---

Feel free to let me know if you’d like me to adjust this further!