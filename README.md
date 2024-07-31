
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/crop-prediction-app.git
    cd crop-prediction-app
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure MongoDB connection:
    - Open the `config/config.yaml` file.
    - Replace `<username>:<password>` in the `uri` field with your MongoDB username and password.
    - Update `myDatabase` and `myCollection` with your desired database and collection names.
    ```yaml
    mongodb:
      uri: "mongodb+srv://username:password@your-cluster.mongodb.net/?retryWrites=true&w=majority&appName=your-app"
      database: "yourDatabase"
      collection: "yourCollection"

    model:
      path: "models/xgboost_model.pkl"
    ```

5. Place your pre-trained model (`xgboost_model.pkl`) in the `models` directory.

## Usage

The application can perform two main operations: inserting data into the database and performing predictions on the latest data record.

### Inserting Data

To insert a sample document into the database, run:
```bash
python scripts/main.py insert
