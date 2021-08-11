### Links
* AWS Glue: https://aws.amazon.com/glue/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc
* AWS Athena: https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc
* 

### ML Workflow
* Ingest & Analyze: Data Exploration & Bias detection
  * Amazon Simple Storage Service or Amazon S3 and Amazon Athena to ingest, store and query your data. With AWS Glue, you will catalog the data in its schema. For statistical bias detection in data, you will learn how to work with Amazon SageMaker Data Wrangler and Amazon SageMaker Clarify
* Prepare & Transform: Feature Engineering & Feature store
  * Amazon SageMaker Data Wrangler, Amazon SageMaker Processing Jobs, Amazon SageMaker Feature Store
* Train & Tune: Automated ML to create baseline and then model training & tuning
  * Amazon SageMaker Autopilot, Amazon SageMaker Training & Debugger, Amazon SageMaker Hyperparameter Tuning  
* Deploy & Manage: Model deployement & Automated pipelines
  * Amazon SageMaker Endpoints, Amazon SageMaker Batch Transform, Amazon SageMaker pipelines

### Data Lakes
* Amazon S3 is a Data Lake which is used to store objects
* It is a centralized and secure repository that can store, discover, and share virtually any amount and any type of your data
* You can ingest data in its raw format without any prior data transformation.
* Whether it's **structured relational data** in the form of CSV or TSV files, **semi-structured data** such as JSON or XML files, or **unstructured data** such as images, audio, and video files. You can also ingest **streaming data**, such as an application delivering a continuous feed of log files or feeds from social media channels into your data lake.
* Data lake needs to be governed

### AWS Data Wrangler - https://github.com/awslabs/aws-data-wrangler
* AWS Data Wrangler is an open source **Python library** developed by members of the AWS professional services team. 
* It connects Pandas DataFrame with AWS data-related Services. 
* AWS Data Wrangler offers abstracted functions to load or unload data from data lakes, data warehouses or databases on AWS. 

### AWS Glue
* Create a reference to the data basically S3 to table mapping. The AWS Glue table which is created inside an AWS Glue database only contains the metadata information such as the data schema. Catalog is used to find the location of data and which schema should be used to query the data
* Glue Crawlers are used infer schema and update data catalog
* First create AWS Glue Data Catalog database using catalog.create_database function, and create a csv table within the database to store the schema and the metadata

### AWS Athena
* Used to query data in S3 using SQL using the schema lookup in AWS Glue Data Catalog
* To write SQL query directly in Jupyter Notebook use aws wranger: df = wr.athena.read_sql_query("SELECT * FROM my_table", database="my_db")
* Athena is based on presto - distributed SQL query engine









