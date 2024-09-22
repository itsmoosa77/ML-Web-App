# ML-Web-App
Overview
The ML-Web-App is a web-based application designed to allow users to upload datasets and apply machine learning (ML) models to perform predictive analysis. The application provides a simple and intuitive interface for users to select a dataset, choose an ML model, and receive results based on the chosen algorithm.

The project is built using Node.js for the backend to handle server-side operations, while the actual ML model execution is performed using a Python script. The two technologies are seamlessly integrated, providing an efficient and user-friendly experience for applying machine learning models.

# Key Features
Dataset Upload: Users can upload a dataset (in CSV format) without missing values. The dataset's last column must be named target, which will be used as the labels (Y-axis) in the ML model.
Model Selection: Users can select a machine learning model from a list of available options. Once selected, the app will apply the model to the uploaded dataset.
Result Display: After the model is applied, the prediction results are displayed to the user on the web page.
Backend Integration: The server is built using Node.js, and backend processing is done through a Python script that handles ML model application and result computation.
Project Structure
* index.html : The user interface where users upload datasets, select ML models, and view the results.
* server.js : Manages the server and handles user requests, including dataset upload and communication with the Python script.
* ml_script.py : Contains the code for loading the dataset, preprocessing it, applying the selected ML model, and returning the results to the Node.js server.
