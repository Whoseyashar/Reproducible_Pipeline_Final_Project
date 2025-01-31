# Reproducible_Pipeline_Final_Project

**University of Luxembourg**  
**Yashar Movahedi**

This project implements a reproducible pipeline for cleaning, analyzing, and visualizing a dataset from the Machine Learning Advanced course. It includes all necessary files, dependencies, and clear instructions to execute the pipeline efficiently.

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
