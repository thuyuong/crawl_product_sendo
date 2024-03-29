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
    https://github.com/thuyuong/crawl_product_sendo.git
    cd crawl_product_sendo
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
   Output result:
    - Calculate revenue per transaction
      ![image](https://github.com/thuyuong/crawl_product_sendo/assets/75436571/7b537186-2431-46bc-9b48-a7543c14e681)
    - Calculate total revenue per shop
      ![image](https://github.com/thuyuong/crawl_product_sendo/assets/75436571/b66490f3-e068-4b9d-a96e-b3e91da2817a)
## Additional Notes

- Adjust configurations and settings in the PySpark script or Spark configuration files as needed.
- Ensure that your environment variables (such as `SPARK_HOME` and `PATH`) are correctly set up.
- This project assumes basic knowledge of Apache Spark and PySpark.
