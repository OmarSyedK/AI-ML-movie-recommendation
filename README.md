# AI/ML Movie Recommendations

A machine learning model trained on real world dataset which is processed and cleaned for best possible results using "Text Vectorization". 





## System Architecture

Broken down into five key stages:

- **Data:** Acquiring and merging the raw movie datasets.
- **Preprocessing:** Cleaning the data and engineering features to create a usable format for the model.
- **Model:** Building the recommendation logic using text vectorization and similarity metrics.
- **Deploy:** Saving the processed data and model objects for use in the application.
- **Website:** Creating a user-friendly web interface for interaction with the model.

## Tech Stack

- **Language:** **Python**
- **Core Libraries:**
    - **Pandas & NumPy:** For data manipulation and numerical operations.
    - **Scikit-learn:** For implementing the "Bag of Words" text vectorization.
    - **Pickle:** For serializing and saving the Python objects (the processed dataframe and similarity vectors) from the notebook.
- **Development Environments:**
    - **Jupyter Notebook:** Used for data cleaning, model building, and experimentation.
    - **PyCharm:** Used for developing the frontend web application.
- **Frontend:**
    - **Streamlit:** A Python library used to create a simple and effective web-based user interface.
- **API:**
    - **TMDB (The Movie Database) API:** Used to fetch movie posters dynamically for display in the UI.


### Dataset
[TMDB 5000 Movie Datase](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)


### [Documentation](https://clover-lute-ae5.notion.site/Project-Documentation-AI-Powered-Movie-Recommendation-System-291e72e046368057afe7e16f3a18cf3d)
