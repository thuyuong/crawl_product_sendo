import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StringType, FloatType, IntegerType, StructType, StructField
from pyspark.sql.functions import sum


# Create a Spark session
spark = SparkSession.builder.appName("SendoCrawler").getOrCreate()

# Create a base RDD from URLs to crawl
urls_to_crawl = spark.sparkContext.textFile("input/links.txt")

def schema():
    # Define the schema for the DataFrame
    schema = StructType([
        StructField("product_id", StringType(), True),
        StructField("name", StringType(), True),
        StructField("price", FloatType(), True),
        StructField("order_count", IntegerType(), True),
        StructField("shop_id", StringType(), True),
        StructField("shop_name", StringType(), True),
    ])
    # Create an empty DataFrame with the specified schema
    df = spark.createDataFrame([], schema=schema)
    return df

# Function to crawl product page and extract information
def crawl_product_page(api_url):
    df1 = schema ()
    response = requests.get(api_url)
    if response.status_code == 200:
        json_data = response.json()
        for i in range(1,int(round(json_data["data"]["total"]/24,0))+1):
              response = requests.get(api_url + str(i))
              if response.status_code == 200:
                  json_data = response.json()
                  # For example, assuming "data" is a dictionary containing a "list" key, and "list" is a list containing dictionaries
                  data_list = json_data.get("data", {}).get("list", [])
                  if data_list is not None:
                    # Iterating over the list and accessing the "product_id" key from each dictionary
                    infor_prod = spark.createDataFrame([
                          (
                              item.get("product_id"),
                              item.get("name"),
                              item.get("final_price"),
                              item.get("order_count", 0),  # Provide a default value of 0
                              item.get("admin_id"),
                              item.get("shop_name")
                          ) for item in data_list
                      ], schema=["product_id", "name", "price", "order_count", "shop_id", "shop_name"])
                    df1 = df1.union(infor_prod)
        return df1
    return []

# Map crawling function to each URL and collect results
df2 = schema()
for url in urls_to_crawl.collect():
    product_data = crawl_product_page(url)
    df2 = df2.union(product_data)

# Clean and transform data as needed
# Calculate revenue per transaction
df3 = df2.withColumn("revenue", col("price").cast("float") * col("order_count").cast("int"))
# Calculate total revenue per shop
df4 = df3.groupBy(["shop_id","shop_name"]).agg(sum("revenue").alias("total_revenue"))

# Export DataFrame to file CSV with encoding UTF-8
df3.toPandas().to_csv("output/revenue_items.csv",header=True, encoding="UTF-8", mode="w")
df4.toPandas().to_csv("output/revenue_shops.csv", header=True, encoding="UTF-8", mode="w")


# Read the CSV file again to check
df_read_rev_items = spark.read.csv("output/revenue_items.csv", header=True, encoding="UTF-8")
df_read_rev_shops = spark.read.csv("output/revenue_shops.csv", header=True, encoding="UTF-8")
df_read_rev_items.show(10)
df_read_rev_shops.show()

# Stop Spark session
spark.stop()
