
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Vivek-00101/crop_recommend.git
    cd crop_recommend
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
    - Create a MongoDB Atlas account if you don't have one: [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register)
    - Create a new cluster and a database user.
    - Whitelist your IP address to allow connections.
    - Obtain your connection string from the MongoDB Atlas dashboard.
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

6. Place your pre-trained model (`xgboost_model.pkl`) in the `models` directory.

## Usage

The application can perform two main operations: inserting data into the database and performing predictions on the latest data record.

### Inserting Data

To insert a sample document into the database, run:
```bash
python scripts/main.py insert


### Running the appplication

To run the application:
```bash
python scripts/main.py predict
