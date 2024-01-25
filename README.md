# PySpark Data Crawling for Sendo Marketplace

## Introduction

This project uses PySpark to crawl data from the Sendo marketplace (https://www.sendo.vn/).

## Prerequisites

Before you start, make sure you have the following installed on your machine:

- Python (recommended version is Python 3)
- Java Development Kit (JDK) - recommended to use OpenJDK or Oracle JDK (minimum version is Java 8)
- Apache Spark - download and install from the official website (https://spark.apache.org/downloads.html)

## Setup

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/your_username/sendodata.git
    cd sendodata
    ```

2. Run the setup script to install Python libraries.

    ```bash
    ./bin/setup_python_libs.sh
    ```

    This script installs the required Python libraries specified in the `requirements.txt` file.

## Crawling Data
3. Execute the PySpark script for crawling data from Sendo marketplace.

    ```bash
    ./bin/start.sh
    ```

## Additional Notes

- Adjust configurations and settings in the PySpark script or Spark configuration files as needed.
- Ensure that your environment variables (such as `SPARK_HOME` and `PATH`) are correctly set up.
- This project assumes basic knowledge of Apache Spark and PySpark.
