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
* AWS Glue is a serverless data integration service that makes registering, discovering, preparing, and combining data easy for analytics and machine learning
* First create AWS Glue Data Catalog database using catalog.create_database function, and create a csv table within the database to store the schema and the metadata

### AWS Athena
* Used to query data in S3 using SQL using the schema lookup in AWS Glue Data Catalog
* To write SQL query directly in Jupyter Notebook use aws wranger: df = wr.athena.read_sql_query("SELECT * FROM my_table", database="my_db")
* Athena is based on presto - distributed SQL query engine
* When you register an Amazon Athena table with your S3 data, Athena uses the AWS Glue Data Catalog to store the schema and table-to-S3 mapping.

### AWS Data Wrangler - Python library
* Visualization
* Transform
* Statistical Bias Report - Visualizable format - Wrangler uses only subset of data to detect bias
* Feature Importance

### Amazon SageMaker Clarify - Python library
* https://github.com/sandhyaparna/AWS/blob/master/AWS%20ML%20Speciality/Practical%20Data%20Science%20with%20AWS/Jupyter%20Notebooks/02_Biased_Reports_SageMaker_Clarify.ipynb
* SageMakerClarifyProcessor is a construct/component/function that allows you to **scale the bias detection process into a distributed cluster**. By using two parameters, instance type and instance count, you can scale up the distributed cluster to the capacity that you need. Instant count represents the number of nodes that are included in the cluster, and instance type represents the processing capacity of each individual node in the cluster.
* Bias report output path is the location to save bias report in S3 - Detailed report Imbalanced Data: https://github.com/sandhyaparna/AWS/blob/master/AWS%20ML%20Speciality/Images/Statistical%20Bias%20Report.pdf </br>
On Balanced data: https://github.com/sandhyaparna/AWS/blob/master/AWS%20ML%20Speciality/Images/Statistical%20Bias%20Report%20on%20Balanced%20Data.pdf
* DataCaonfig object represents details about the data. It has input and output location of your data on S3, label
* BiasConfig captures the interested features that we want to look at to evaluate bias or imbalnces 
* All the objects objects are passed as parameters into run_pre_training_bias object/function. Methods used to evaluate can be mentioned
* Once the configuration of the pre-training bias method is done, you launch this job. In the background, SageMaker Clarify is using a construct called SageMaker Processing Job to execute the bias detection at scale.
* Clarity is a scalable API
* SageMaker Processing Jobs is a construct that allows you to perform any data-related tasks at scale. These tasks could be executing pre-processing, or post-processing tasks, or even using data to evaluate your model.
![](https://github.com/sandhyaparna/AWS/blob/master/AWS%20ML%20Speciality/Images/Amazon%20SageMaker%20Processing%20Job.PNG)
* Amazon SageMaker Clarify is used for 
  * Statistical Bias Detection
  * Statistical Bias Report
  * ML explainability
  * Detecting drift in data and models

### Bias Detection
* Using AWS Data Wrangler and Amazon SageMaker Clarify https://github.com/sandhyaparna/AWS/blob/master/AWS%20ML%20Speciality/Practical%20Data%20Science%20with%20AWS/Jupyter%20Notebooks/02_Biased_Reports_SageMaker_Clarify.ipynb
* Detection Methods: https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-measure-data-bias.html
  * Count of different groups within a feature - CI Class Imbalance
  * Count of different groups with respect to the Target groups - DPL
* Statistical Bias: Some elements/groups are more heavily weighted or represented. Imbalanced in Target class or 
  * Activity Bias: Social Media Content - Very few people are active on social media and hence their data doesn't represent the entire population
  * Societal Bias: Biases in data that is generated by humans. These biases could be introduced because of preconceived notions that exist in society. 
  * Selection Bias: Take, for example, a streaming service. You want to watch a movie on the streaming service and the streaming service makes a few recommendations for you and you decide to watch Dancing with Wolves. You like the movie and you rate it high. From then on, the streaming service is recommending you the movies that have wolves in them. It's partly because of the feedback you provided to the service. But in reality, maybe you watched that movie because you like the actress in the movie and you don't even particularly like wolves. Situations like this could result in selection bias that includes a feedback loop that involves both the model consumers and the Machine Learning model itself. 
  * Data Drift: Data drift happens, especially when the data distribution significantly varies from the distribution of the training data that was used to initially train the model. This is called data drift and also data shift.
    * Covariant drift: Sometimes the distribution of the independent variables or the features that make up your dataset can change
    * Prior probability drift: Sometimes the data distribution of your labels or the targeted variables might change
    * Concept drift: Sometimes the relationship between the two, that is the relationship between the features and the labels can change as well. It can happen when the definition of the label itself changes based on a particular feature like age or geographical location. Take, for example, my experience. Last time when we traveled a few years ago across US on a road trip, we quickly found out that the soft drinks are not called the same across US. So when we stopped for meals and ordered soft drinks, we realized that soda is not called soda across US. In some areas, it's called pop, and in some areas, it's called soda. Now, if you think about all the geographies across the world, you can only imagine the interesting combinations, different labels, you can come up with. 
* It is really important to continuously monitor and detect various biases that could be prevalent in to your training datasets before and after you train your models.

### Feature Importance
* Feature importance is the idea of explaining the individual features that make up your training data set using a score called important score. 
* How useful or valuable the feature is relative to other features.
* Uses SHAP framework - can create both local & global explanations
* From SageMaker Studio, start a new Dataflow, connect data to S3 or Athena, select the data that we are interested to identify features importances based on a label, import the dataset - this will import data from S3 to data wrangler environment, add analysis, choose 'Quick Model' to do feature importance  and choose the label. When preview is hit, Data Wrangler is working in the background to create a quick model out of a subset of your data. It uses 70% of the subset of the data for training and 30% for test. It will build that quick model to analyze the F1 score and Data Wrangler calculates the feature importance score on data set. Behind the scene, Data Wrangler ran a Random Cut Forest algorithm on the subset of my data using 70% for training and 30% for testing. And it has calculated a quick model to give me the feature importance scores as well as the F1 score.     https://www.coursera.org/learn/automl-datasets-ml-models/lecture/lvtm4/feature-importance-shap

### SageMaker Autopilot
https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html </br>
* Autopilot includes performing data exploration, identifying the machine learning problem, selecting the algorithm based on the machine learning problem, transforming the data to get it into the format that is expected by your algorithm, and finally, training and performing hyperparameter tuning to find the optimal set of hyperparameters that result in the most performant model. In addition to covering the workflow steps and tasks that I highlighted, autopilot is also fully transparent, meaning it will automatically generate and share the feature engineering code, generate Jupiter notebooks that walk you through how the models were built. This includes the data processing as well as the algorithms, the hyperparameters, and the training configuration. You can then use those automatically generated notebooks to reproduce the same experiment or perform modifications to that example to continue to refine your model.
* After the data analysis step, autopilot will generate two types of notebooks that describe the plan that autopilot fellows to create the candidate models. First, there's a data exploration Notebook that describes what Autopilot learned about your data. This Notebook also identifies areas of investigation that may indicate potential issues in your source data that could require further analysis or impact your model performance. The second type of Notebook is a candidate generation Notebook, which contains each suggested data preprocessing step. The algorithm and the hyperparameter ranges that will be used for the tuning job.
![](https://docs.aws.amazon.com/sagemaker/latest/dg/images/Autopilot-process-graphic-1.png)





