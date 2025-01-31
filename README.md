# Kifiya-AIM-Week-7

## Project Overview

This project involves building a data warehouse to store data on Ethiopian medical businesses scraped from the web and Telegram channels. The project includes several key steps to ensure the data warehouse is robust, scalable, and capable of handling the unique challenges associated with scraping and data collection from Telegram channels. Additionally, it integrates object detection capabilities using YOLO (You Only Look Once) to enhance data analysis.

## Features

- **Data Scraping and Collection Pipeline**: Extract data from public Telegram channels relevant to Ethiopian medical businesses.
- **Data Cleaning and Transformation**: Clean and transform the scraped data to ensure it is ready for analysis.
- **Object Detection using YOLO**: Enhance data analysis with object detection capabilities.
- **Data Warehouse Design and Implementation**: Store and manage the cleaned and transformed data.
- **Data Integration and Enrichment**: Integrate and enrich the data for comprehensive analysis.

## Setup Instructions

### Prerequisites

- Python 3.6+
- pip
- SQLite (or any other database of your choice)
- DBT (Data Build Tool)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Kifiya-AIM-Week-7.git
    cd Kifiya-AIM-Week-7
    ```

2. Install the required Python packages:

    ```bash
    pip install telethon pandas sqlite3 dbt
    ```

### Data Scraping and Collection

1. Create a Python script `telegram_scraper.py` to scrape data from Telegram channels:

    ```python
    import logging
    from telethon import TelegramClient, events

    # Configure logging
    logging.basicConfig(filename='scraping.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    # Use your own values from my.telegram.org
    api_id = 'YOUR_API_ID'
    api_hash = 'YOUR_API_HASH'

    # Create the client and connect
    client = TelegramClient('session_name', api_id, api_hash)

    async def main():
        # List of channels to scrape
        channels = [
            'https://t.me/DoctorsET',
            'https://t.me/lobelia4cosmetics',
            'https://t.me/yetenaweg',
            'https://t.me/EAHCI'
        ]

        data = []

        for channel in channels:
            async for message in client.iter_messages(channel):
                logging.info(f"Message from {channel}: {message.text}")
                data.append({
                    'channel': channel,
                    'message': message.text
                })

        # Save data to a file
        with open('scraped_data.json', 'w') as f:
            json.dump(data, f)

    with client:
        client.loop.run_until_complete(main())
    ```

2. Run the script:

    ```bash
    python telegram_scraper.py
    ```

### Data Cleaning and Transformation

1. Create a Python script `data_cleaning.py` for data cleaning:

    ```python
    import pandas as pd
    import logging

    # Configure logging
    logging.basicConfig(filename='cleaning.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    # Load raw data
    data = pd.read_json('scraped_data.json')

    # Remove duplicates
    data.drop_duplicates(inplace=True)

    # Handle missing values
    data.fillna(method='ffill', inplace=True)

    # Standardize formats (example: converting all text to lowercase)
    data['message'] = data['message'].str.lower()

    # Data validation (example: ensuring no empty messages)
    data = data[data['message'].str.strip() != '']

    # Save cleaned data
    data.to_json('cleaned_data.json', orient='records')

    logging.info('Data cleaning completed successfully.')
    ```

2. Run the script:

    ```bash
    python data_cleaning.py
    ```

3. Store the cleaned data in a database:

    ```python
    import sqlite3
    import pandas as pd

    # Connect to SQLite database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Create table
    c.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        channel TEXT,
        message TEXT
    )
    ''')

    # Insert cleaned data
    data = pd.read_json('cleaned_data.json')
    data.to_sql('messages', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

    logging.info('Cleaned data stored in database successfully.')
    ```

### DBT for Data Transformation

1. Install DBT:

    ```bash
    pip install dbt
    ```

2. Initialize a DBT project:

    ```bash
    dbt init my_project
    ```

3. Define DBT models:

    Create a model file in `my_project/models/transform.sql`.

    ```sql
    -- filepath: my_project/models/transform.sql
    WITH cleaned_data AS (
        SELECT
            id,
            channel,
            message
        FROM
            {{ ref('messages') }}
    )
    SELECT
        id,
        channel,
        message
    FROM
        cleaned_data
    ```

4. Run DBT models:

    ```bash
    cd my_project
    dbt run
    ```

5. Test and document transformations:

    ```bash
    dbt test
    dbt docs generate
    dbt docs serve
    ```

### Monitoring and Logging

Ensure logging is implemented in all scripts to track processes and capture errors.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.