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
* Glue can convert data to parquet format. It integrates with both Athena & redshift spectrum. Runs spark or scala or pyspark code
* Firehose can convert from csv or json to to parquet or ORC (columnar data) and also supports compression
* Kinesis Data Analytics and Athena use SQL
* Kinesis Data Analytics ML algos: Random cut forest, hotspots
* Advantages of Neo:
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
* Accelerated computing family (P and G type instances) come with GPUs, and these are ideal for algorithms that are optimized for GPUs.
* General Purpose family are some of the lowest cost instances and offer balanced performance and memory configuration (T and M type instances).
* Compute Optimized family comes with the latest generation CPUs and is a higher performance system. These are suitable for CPU intensive model training and hosting (C type instances). 
* Memory-optimized family are optimized for workloads that process large datasets in memory (R type instances). 
* Besides, the sagemaker also has Elastic Inference Acceleration (partial GPUs) that provides fractional GPU capacity at a fraction of the cost of accelerated computing family. 

Elastic inference Acceleration is suitable for inference workloads that can benefit from GPUs and can be easily added to other instance families.
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
* Batch: Non-ETL jobs, require docker image. schedule batch jobs using cloudwatch events and orchestrate batch jobs using AWS step functions
* Docker: Dokcerfile, Image, Container. Docker Deamon contains many containers on 1 server
* Training container: opt/ml: input, output, model, code
* Deployement container: opt/ml/model
* Structure of your Docker image: nginx.conf, wsgi.py, train, serve, predictor.py
* Copies the training code inside the container COPY train.py /opt/ml/code/train.py, # Defines train.py as script entrypoint ENV SAGEMAKER_PROGRAM train.py
* To launch docker containers on AWS EC2 instances: ECS , Fargate
* Lambda: function as a service, serverless, run on-demand, only short executions that are event driven, runs CRON scheduled jobs, increase allocated memory and timeout upto 15mins. API gateway is to expose lambda functions as http api
* Batch: Batch processing at scale, to run many computing jobs, relies on EBS/instance store for disk space
* Cloudwatch logs: real-time monitoring of logs
* Cloudwatch Events: cron jobs, events rules to react to a service, trigger lambda functions
* CloudTrail: governance, compliance and audit for aws account, can put logs from CloudTrail into CloudWatch logs
* Data Pipeline is a Orchestration service and Allows access to EC2 or EMR instances (creates resources in your own
* Quicksight can be used for forecasting, auto narratives, anomaly detection using random cut forest
* SPICE is quick sight's in-memory calculation engine
* To connect quicksight using VPC, add quicksight's IP address range to your database security groups
* EMR / AWS Integration - EMR helps creating Hadoop clusters (Big Data) to analyze and process vast amount of data
  * Amazon EC2 for the instances that comprise the nodes in the cluster
  * Amazon VPC to configure the virtual network in which you launch your instances
  * Amazon S3 to store input and output data
  * Amazon CloudWatch to monitor cluster performance and configure alarms
  * AWS IAM to configure permissions
  * AWS CloudTrail to audit requests made to the service
  * AWS Data Pipeline to schedule and start your clusters
* Spark components: Spark Streaming, Spark SQL, MLLib, GraphX
* To decrease FPs, increase threshold - guarnateed to reduce FPs, but might inc FNs
* Dataprep for SageMaker: RecordIO / Protobuf
  * Training requires input path, output path, model(ECR path that has training image), compute resource
* Deployement: Inference pipelines, Elastic Inference, Sagemaker Neo, Auto scaling
* Ways to deploy: Persistent endpoint for making individual predictions on demand, SageMaker Batch Transform to get predictions for an entire dataset
* Linear Learner: RecordIO wrapped protobuf - Float32 data only!, File or pipe mode, first column contains label and variable names should not be headers, CPU is preferred
* XGBoost: So, it takes CSV or libsvm input, RecordIO wrapped protobuf, parquet; only CPU
* Seq2Seq: RecordIO Protobuf (tokens must be integers); Must provide training data, validation data, and vocabulary files; GPUs on a single machine. Embedding layer, Encoder, Decoder
* DeepAR: JSON, Gzip or parquet; record should contain start time stamp, target - time series values, can use CPU or GPU
* Blazing Text: __label__ followed by the label and tokenized text; word2vec modes: CBOW, skip-gram, batch skip-gram (distributed computation - multiple CPU)
* Object2Vec: Compute nearest neighbors of objects, data is tokenized to integers. JSON lines; 2 encoders ( Avg pooled embeddings, CNNs, Bi-directional LSTM) passed through camparator and then feed forward NN
* Object Detection: boxes, Uses a CNN with the Single Shot multibox Detector (SSD) algorithm. GPU
* Semantic Segmentation: 3 algos- Fully Convolutional Network, pyramid Scene Parsing, DeepLabv3, Backbones - ResNet50, ResNet101
* Factorization machines: RecordIO wrapped protobuf - Float32, recommender systems
* KNN: sample, dimensionality reduction, indexing
* K-Means: K, feature_dim
* Spark & SageMaker: Use sagemaker spark library, SageMakerEstimator. Call fit on your SageMakerEstimator to get a SageMakerModel; Call transform on the SageMakerModel to make inferences
* SageMaker Debugger: Monitor system bottlenecks, Profile model framework operations, Debug model parameters
* Data must be tabular CSV for SageMaker Autopilot
* SageMaker Model Monitor: Visualize data drift, Detect anomalies & outliers, Detect new features, Drift in model quality, Bias drift, Feature attribution drift
* Amazon Transcribe: Speaker Identificiation, Channel Identification, Custom Vocabularies
* Amazon Polly: Lexicons, SSML (Speech Synthesis Markup Language), Speech Marks
* Rekognition: Computer vision, Object and scene detection, Can use your own face collection, Image moderation, Facial analysis, Celebrity recognition, Face comparison, Text in image, Video analysis
* DeepLens: Deep learning enabled video camera Integrated with Rekognition , SageMaker , Polly, Tensorflow , MXNet , Caffe
* Contact Lens for Amazon Connect: For customer support call centers
* Amazon Kendra: Enterprise search with natural language
* Amazon Augmented AI (A2I): Very similar to Ground Truth
* AWS Security: IAM, MFA> SSL/TLS, cloud train, encryption, be careful with PHI
* KMS is accepted by notebooks and all SageMaker jobs. Training, tuning, batch transform, endpoints Notebooks and everything under /opt/ml/ and / tmp
can be encrypted with a KMS key
* AWS S3 encryption is used to encrypt S3 buckets for training data and hosting models
* Protecting Data in Transit in SageMaker: TLS, inter container traffic encryption, 
* For VPC, it needs an interface endpoint ( PrivateLink ) or NAT Gateway, and allow outbound connections, for training and hosting to work
* Predefined policies: AmazonSageMakerReadOnly, AmazonSageMakerFullAccess, AdministratorAccess, DataScientist
* Incremental Training: to train a new model using an expanded dataset that contains an underlying pattern that was not accounted for in the previous training and which resulted in poor model performance
* PCA can be run in regular or randomized mode
* Transform method is called to get inference for an entire data set using batch transform job. The predict method is used for real time inference. The deploy method is used to deploy the trained model to an Amazon SageMaker endpoint. The fit method is used to train a model using the input training dataset.
* SageMaker does not support resource-based policies and service-linked roles. Amazon SageMaker supports authorization based on resource tags. 
* After calling the create_training_job() method to start the training job, you would like to get a status about the progress of the training job, use decribe_training_job
* 

![](https://d1.awsstatic.com/Products/product-name/diagrams/product-page-diagram_Amazon-Kinesis-Data-Streams.074de94302fd60948e1ad070e425eeda73d350e7.png)

















