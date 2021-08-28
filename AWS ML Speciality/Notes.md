### S3
* slides 4 -16: https://github.com/sandhyaparna/AWS/blob/master/AWS%20ML%20Speciality/Slides/AWSCertifiedMLSlides.pdf
* slides 123 - 165: https://github.com/sandhyaparna/AWS/blob/master/AWS%20Cloud%20Practitioner/AWS%20Certified%20Cloud%20Practitioner%20Slides%20v2.3.2.pdf
* slides 65 - 92: https://github.com/sandhyaparna/AWS/blob/master/AWS%20ML%20Speciality/Slides/AMSMLCompressed.pdf
* https://blog.mestwin.net/amazon-s3-in-a-nutshell-words-aws-solutions-architect-associate-exam-review/

### Kinesis
* slides 17 - 31: https://github.com/sandhyaparna/AWS/blob/master/AWS%20ML%20Speciality/Slides/AWSCertifiedMLSlides.pdf
* slides 143 - 185: https://github.com/sandhyaparna/AWS/blob/master/AWS%20ML%20Speciality/Slides/AMSMLCompressed.pdf
* Recognize customers in a store https://aws.amazon.com/blogs/machine-learning/improve-your-customer-service-using-amazon-kinesis-video-streams-and-amazon-rekognition-video/
![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2018/04/06/AmazonRekVideo-cs-2.gif) </br>
![](https://s3.amazonaws.com/brainpower-aws-blogs/artifacts/fidgetology-demo-app/attachments/Brain_Power_fidgetology_02__SystemArchitectureDiagram.png) </br>

### AI Services
* 


##### Database
* Database is specifically for Online Transaction Processing. Within each database, data is organized into tables and columns. Within each column, you can define a description of the data, such as integer, data field, or string. Tables can be organized inside of schemas, which you can think of as folders. When data is ingested, it is stored in various tables described by the schema. Query tools use the schema to determine which data tables to access and analyze.
* Data Warehouse is specifically for Online Analytical Processing. Data flows into a data warehouse from transactional systems, relational databases, and other sources, typically on a regular cadence. It consolidates data from many sources. 
* A data warehouse is specially designed for data analytics, which involves reading large amounts of data to understand relationships and trends across the data. A database is used to capture and store data, such as recording details of a transaction.
* Unlike a data warehouse, a data lake is a centralized repository for all data, including structured, semi-structured, and unstructured. A data warehouse requires that the data be organized in a tabular format, which is where the schema comes into play. The tabular format is needed so that SQL can be used to query the data. But not all applications require data to be in tabular format. 
* Data Lake vs Database vs Datawarehouse vs Datamart https://aws.amazon.com/data-warehouse/

##### Using Pipe Mode
In Pipe mode, your training job streams data directly from Amazon Simple Storage Service (Amazon S3). Streaming can provide faster start times for training jobs and better throughput. This is in contrast to File mode, in which your data from Amazon S3 is stored on the training instance volumes. File mode uses disk space to store both your final model artifacts and your full training dataset. By streaming in your data directly from Amazon S3 in Pipe mode, you reduce the size of Amazon Elastic Block Store volumes of your training instances. Pipe mode needs only enough disk space to store your final model artifacts. See the AlgorithmSpecification for additional details on the training input mode.

##### Using RecordIO Format
In the protobuf recordIO format, SageMaker converts each observation in the dataset into a binary representation as a set of 4-byte floats, then loads it in the protobuf values field. If you are using Python for your data preparation, we strongly recommend that you use these existing transformations.

##### Trained Model Deserialization
Amazon SageMaker models are stored as model.tar.gz in the S3 bucket specified in OutputDataConfig S3OutputPath parameter of the create_training_job call. You can specify most of these model artifacts when creating a hosting model. You can also open and review them in your notebook instance. When model.tar.gz is untarred, it contains model_algo-1, which is a serialized Apache MXNet object. For example, you use the following to load the k-means model into memory and view it:
* import mxnet as mx
* print(mx.ndarray.load('model_algo-1'))
