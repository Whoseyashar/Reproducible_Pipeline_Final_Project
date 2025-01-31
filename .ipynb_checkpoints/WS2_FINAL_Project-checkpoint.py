import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """Loads the dataset."""
    try:
        data = pd.read_csv(filepath)
        print(f"File {filepath} loaded successfully!")
        return data
    except FileNotFoundError:
        print(f"File {filepath} not found!")
        return None

if __name__ == "__main__":
    # Define the path to the dataset
    data_file = "data/amazon.csv"

    # Load the data
    data = load_data(data_file)
    if data is not None:
        # Display the first 5 rows
        print(data.head())

        # Example Visualization: Count plot for top 10 product IDs
        plt.figure(figsize=(10, 6))
        sns.countplot(y=data['product_id'], order=data['product_id'].value_counts().index[:10])
        plt.title("Top 10 Product IDs")
        plt.xlabel("Count")
        plt.ylabel("Product ID")

        # Save the plot BEFORE showing it
        plt.savefig("outputs/top_10_product_ids.png")
        print("Plot saved as 'outputs/top_10_product_ids.png'")

        # Show the plot
        plt.show()

        # Save the cleaned dataset
        cleaned_file = "outputs/cleaned_amazon.csv"
        data.to_csv(cleaned_file, index=False)
        print(f"Cleaned dataset saved as {cleaned_file}")
