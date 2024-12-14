import pickle

# Path to the model.pkl file
file_path = 'development/pickels/model.pkl'

# Load the pickle file
try:
    with open(file_path, 'rb') as file:
        model = pickle.load(file)

    # Display type of the object
    print("Model Type:", type(model))

    # Check the object's attributes
    print("Model Attributes:")
    for attr in dir(model):
        if not attr.startswith("_"):  # Ignore internal attributes
            print(f"- {attr}")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
