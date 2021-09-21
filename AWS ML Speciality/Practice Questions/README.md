* https://amazonmr.au1.qualtrics.com/jfe/form/SV_dg3duwjYBh3zZnn
* https://amazonmr.au1.qualtrics.com/jfe/form/SV_d9W72HMVJckXsUJ
* https://amazonmr.au1.qualtrics.com/jfe/form/SV_cOds6iMP7ekliD3
* The AWS Certification Quiz Show: Machine Learning - Specialty exam, Episode 1  https://www.aws.training/Details/Video?id=37281
* The AWS Certification Quiz Show: Machine Learning - Specialty exam, Episode 2  https://www.aws.training/Details/Video?id=37285
* Free with kindle unlimited https://www.amazon.com/Certified-Machine-Learning-Specialty-Practice-ebook/dp/B08BG6G4VF
* Full Length https://healthedge.udemy.com/course/aws-machine-learning-practice-exam/learn/quiz/4713752?learning_path_id=1612896#overview
* https://healthedge.udemy.com/course/aws-certified-machine-learning-specialty-full-practice-exams/learn/quiz/4755118#overview
* https://healthedge.udemy.com/course/aws-machine-learning-a-complete-guide-with-python/learn/quiz/4774522#overview
* DA Sample Questions https://d1.awsstatic.com/training-and-certification/docs-data-analytics-specialty/AWS-Certified-Data-Analytics-Specialty_Sample-Questions_v.1.1_FINAL.pdf
* https://www.braincert.com/course/22419-AWS-Certified-Machine-Learning-%E2%80%93-Specialty-Practice-Exams
* https://www.testpreptraining.com/aws-certified-machine-learning-specialty-free-practice-test
* https://www.whizlabs.com/learn/course/aws-certified-machine-learning-specialty/281/quiz/15001/practice/start

### Key notes from practice exams
* When batch size should be decreased, decrease the learning rate also. similarity when they have to increase
* object2vec to vectorize sentences
* Instance Segmentation - Autonomous vehicle model
* When model takes too long to converge: Normalize data before sending or batch normalization
* Aws Sagemaker tuning jobs to tune hyperparameters
* Glue can convert data to parquet format
* Firehose can convert from csv or json to to parquet or ORC and also supports compression
* Advantages of Edge:
  * ML models will run upto 2x better performance
  * Required framework memory is reduced 10x
  * ML model can run on multiple hardware platforms
* AWS IoT Greengrass:
  * works offline
  * Respond to local events in near real-time
* GetObject, Putobject arelegal API calls
* One should always use AES256 encryption and wildcards are allowed in JSON policies
* MoveObject API call is illegal
* Number of mosquito bites - poisson Distribution
* prob of person contacting a disease - Binomial
* freq functions for IDF - Smoth, Probabilistic, Standard
* Algos that support pipe input mode and recordIO protobuf are PCA, K-means, Factorization machines, LDA, Neural Topic modeling, Linear Learner, Randomcut forest
* For notebooks in VPC - create Amazon sagemaker VPC interface endpoints within the corporate VPC
* ML code in DocerFile to run own algo: COPY and ENTRYPOINT
* Install Docker compose for local training on his laptop
* U pay for compute, storage and transfer out of cloud
* AWS global services: IAM, CloudFront, etc
* Customer is responsible for OS< Network, firewall construction, client-side encrytion, server-side encryption, Networking traffic protection
* To access AWS: AWS Mgmt Console, AWS CLI (Command Line Interface), AWS SDK (Software Development Kit)
* IAM Access Advisor
* Bootstrap EC2 instances using EC2 User data script
* Types of Ec2 instances:
  * Accelerated Computing: Amazon EC2 P4 instances are the latest generation of GPU-based instances and provide highest performance for machine learning training and high performance computing in the cloud. Machine learning, high performance computing, computational fluid dynamics, computational finance, seismic analysis, speech recognition, autonomous vehicles, and drug discovery.
  * General purpose: workloads such as webservers or code repos - T & M
  * Compute Optimized: batch processing workloads, High performance computing, scientific modeling & ML, Gaming Servers - C. High performance computing (HPC), batch processing, ad serving, video encoding, gaming, scientific modelling, distributed analytics, and CPU-based machine learning inference.
  * Memory optimized: web scale caching store, High RDs, In memory Bi, rela-time processing of big unstructured data. Memory-intensive applications such as open-source databases, in-memory caches, and real time big data analytics
  * Storage Optimized: OLTP, Relational & No-SQL databases, cache for in-memory database, Distributed file system. NoSQL databases (e.g. Cassandra, MongoDB, Redis), in-memory databases (e.g. Aerospike), scale-out transactional databases, data warehousing, Elasticsearch, analytics workloads.
* Security groups are acting as a “firewall” on EC2 instances
* IAM and bucket policies for S#. Bucket policies for public access and cross account access
* EC2 Instances Purchasing Options
  * On-Demand Instances: short workload, predictable pricing
  * Reserved: (MINIMUM 1 year)
    * Reserved Instances: long workloads
    * Convertible Reserved Instances: long workloads with flexible instances
    * Scheduled Reserved Instances: example – every Thursday between 3 and 6 pm
  * Spot Instances: short workloads, cheap, can lose instances (less reliable). Batch jobs, data analysis, image processing, distributed workloads
  * Dedicated Hosts: book an entire physical server, control instance placement
  * Dedicated Instances: no other customers will share your hardware
* AMI - Amazon Machine Image are a customization of an EC2 instance
* EC2 image builder: Automate the creation, maintain, validate and test EC2 AMIs
* AWS storage gateway to bridge data between on-premise and cloud data in S3
* AWS API gateway: get requests from client side
* RDS, Aurora (postgres-sql, mysql), Elasticache, Redshift, Athena, Redshift spectrum, Dynamo DB, Dynamo Accelerator, Document DB (mango DB), EMR, Neptune, Quicksight, QLDB, Blockchain, Dabase Migration Service
* Glue: ETL
* Batch: Non-ETL jobs, require docker image
* Docker: Dokcerfile, Image, Container. Docker Deamon contains many containers on 1 server
* To launch docker containers on AWS EC2 instances: ECS , Fargate, 
* Lambda: function as a service, serverless, run on-demand, only short executions that are event driven, runs CRON scheduled jobs, increase allocated memory and timeout upto 15mins. API gateway is to expose lambda functions as http api
* Batch: Batch processing at scale, to run many computing jobs, relies on EBS/instance store for disk space
* Cloudwatch logs: real-time monitoring of logs
* Cloudwatch Events: cron jobs, events rules to react to a service, trigger lambda functions
* CloudTrail: governance, compliance and audit for aws account, can put logs from CloudTrail into CloudWatch logs
* 
* 
* 

![](https://d1.awsstatic.com/Products/product-name/diagrams/product-page-diagram_Amazon-Kinesis-Data-Streams.074de94302fd60948e1ad070e425eeda73d350e7.png)

















