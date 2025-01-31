from WS2_FINAL_Project import load_data  # Import your function from WS2_FINAL_Project.py

def main():
    # Define the dataset path
    data_file = "data/amazon.csv"

    print("Starting the pipeline...")

    # Load the dataset
    data = load_data(data_file)

    if data is not None:
        print("Pipeline executed successfully!")
    else:
        print("Pipeline execution failed. Please check the dataset path.")

if __name__ == "__main__":
    main()
