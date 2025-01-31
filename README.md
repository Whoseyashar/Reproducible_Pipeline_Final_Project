# Reproducible_Pipeline_Final_Project

**University of Luxembourg**  
**Yashar Movahedi**

This project implements a reproducible pipeline for cleaning, analyzing, and visualizing a dataset from the Machine Learning Advanced course. It includes all necessary files, dependencies, and clear instructions to execute the pipeline efficiently.

For this project, we use the dataset on Amazon Sales Data 🛒📈, which is included in this repository under the data/ directory as amazon.csv. This project is developed to demonstrate a Reproducible Pipeline for data cleaning, analysis, and visualization. The pipeline is implemented in Python and includes all necessary dependencies and documentation to execute the workflow efficiently.

For more information on the dataset and project, please consult the Project Documentation(https://www.kaggle.com/code/mehakiftikhar/amazon-sales-dataset-eda) You can also explore the dataset by cloning the repository and running the main Python script or exploring the optional Jupyter Notebook provided in the data/ folder.

To get started, follow the instructions in the Execution Guide to install dependencies and run the pipeline seamlessly.
---

## Project Overview
**Objective:**  
Create a reproducible pipeline for data processing and visualization.

**Dataset:**  
Amazon sales dataset located in the `data/` directory as `amazon.csv`.

**Outputs:**  
Cleaned data and visualizations are stored in the `outputs/` directory:
- Cleaned Dataset: `outputs/cleaned_amazon.csv`
- Visualization: `outputs/top_10_product_ids.png`

---

## Repository Structure

```plaintext
Reproducible_Pipeline_Final_Project/
├── data/
│   ├── amazon.csv                 # Raw dataset
│   ├── Project_Part_3_Movahedi.ipynb  # Optional Jupyter notebook for exploration
├── outputs/
│   ├── cleaned_amazon.csv         # Cleaned dataset
│   ├── top_10_product_ids.png     # Visualization of top product IDs
├── WS2_FINAL_Project.py           # Main Python script
├── Dockerfile                     # Docker configuration (optional)
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```
## Instructions to Execute the Pipeline

1. Clone the Repository
  ```
git clone https://github.com/whoseyashar/Reproducible_Pipeline_Final_Project.git
cd Reproducible_Pipeline_Final_Project
 ```
2. Set Up Environment
```
python -m venv env
source env/bin/activate    # For Linux/MacOS
env\Scripts\activate       # For Windows
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Run the Pipeline
```
python WS2_FINAL_Project.py
```
5. Outputs
The cleaned dataset will be saved in outputs/cleaned_amazon.csv.
The visualization plot will be saved in outputs/top_10_product_ids.png.


Here’s a more organized and detailed structure for your README.md:
Reproducible_Pipeline_Final_Project

University of Luxembourg
Yashar Movahedi

This project implements a reproducible pipeline for cleaning, analyzing, and visualizing a dataset from the Machine Learning Advanced course. It includes all necessary files, dependencies, and clear instructions to execute the pipeline efficiently.
Project Overview

    Objective: Create a reproducible pipeline for data processing and visualization.
    Dataset: Amazon sales dataset located in the data/ directory as amazon.csv.
    Outputs: Cleaned data and visualizations stored in the outputs/ directory.

Repository Structure

Reproducible_Pipeline_Final_Project/
├── data/
│   ├── amazon.csv              # Raw dataset
│   ├── Project_Part_3_Movahedi.ipynb  # Optional Jupyter notebook for exploration
├── outputs/
│   ├── cleaned_amazon.csv      # Cleaned dataset
│   ├── top_10_product_ids.png  # Visualization of top product IDs
├── WS2_FINAL_Project.py        # Main Python script
├── Dockerfile                  # Docker configuration (optional)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

Instructions to Run Locally
1. Clone the Repository

git clone https://github.com/whoseyashar/Reproducible_Pipeline_Final_Project.git
cd Reproducible_Pipeline_Final_Project

2. Set Up Environment

    Ensure Python (version ≥3.9) is installed.
    Create a virtual environment:

    python -m venv env
    source env/bin/activate    # For Linux/MacOS
    env\Scripts\activate       # For Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the Pipeline

python WS2_FINAL_Project.py

5. Outputs

    The cleaned dataset will be saved in outputs/cleaned_amazon.csv.
    The visualization plot will be saved in outputs/top_10_product_ids.png.

Optional: we can Running with Docker

To run the pipeline in a Docker container:
1. Build the Docker Image

docker build -t reproducible_pipeline .

2. Run the Docker Container

docker run --rm -v "$(pwd):/app" reproducible_pipeline

## Key Features of the Pipeline
Data Loading: Ensures the dataset is loaded correctly or provides an error message if not found.
Data Cleaning: Handles missing values and removes unnecessary columns or rows.
Visualization: Creates a bar chart of the top 10 most frequent product IDs.
Reproducibility: Can be executed in any environment using provided dependencies or Docker.

## Future Work
Enhance visualizations with interactive plots.
Add automated tests for data validation.
Host pipeline as a web service using frameworks like Flask or FastAPI.



