# ETL

------
### This repo contains the basic ETL job that reads data from an sqlite3 database and generates a report based on a predetermined format

## Folder Structure
- The ***config*** folder contains the toml file where the ETL job's changeable values are
- The ***data*** folder contains the sqlite database
- The ***lib*** folder is the location of the python code 
- The ***reports*** folder contains the generated output of the ETL job

## Fetching the repo
- ### Go to the folder where you want to clone the repo

    ```cd <absolute path to your desired folder>```

- ### Clone the repo:
    ```git clone https://github.com/Francis-Baquiran/ETL.git```

## Setting up the environment:
- ### Go to the folder where your repo was cloned:

    ```cd <absolute path to your cloned repo>\ETL```

- ### Check that python is already installed in your machine:

    ```python --version```

- ### If it is not installed, install the latest version from your browser:

    ```https://www.python.org/downloads/```

- ### Install the pandas library:
    ```pip install pandas```

- ### Install the toml library:
    ```pip install toml```


## Running the job
- ### Execute the following command:
    ```py lib/ETLJob.py```

## Viewing the report
- ### Execute the following command:
    ```cat reports/sales_report.csv```