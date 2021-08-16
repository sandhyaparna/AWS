### Links

### Feature Store
* It is a centralized repo to store engineered features
* Transform the feature and store in Feature Store
* Athena query to extract stored features


### BERT
* Uses Masked Language Model or Next Sentence Prediction

### Train Custom Model
* Bring your own Script
* S3 - contain training data
* The compute resources that you want SageMaker to use for the model training. Compute resources are ml compute instances that are managed by SageMaker.
* The URL of the S3 Bucket where you want to store the output of the training job.
* The Amazon elastic container registry or Amazon ECR path, where the training code image is stored. SageMaker provides built in docker images that include deep learning framework libraries and other dependencies needed for model training and inference. Using script mode, you can leverage these pre built images for many popular frameworks, including TensorFlow, pyTorch, and Mxnet. After you create the training job, SageMaker launches the ml compute instances and uses the training code and the training data set to train the model. It saves the resulting model artifacts and other outputs in the S3 bucket you specify for the purpose.
* Steps:
  * Configure dataset & eval metrics
  * Configure hyper-parameters
  * provide training script - train.py
  * fit the model

### Debug & profile models
* List of built-in rules for debugiing: https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules.html

### SageMaker Pipelines
![](https://github.com/sandhyaparna/AWS/blob/master/AWS%20ML%20Speciality/Images/SageMaker%20Pipeline.PNG)

* Data processing step: prepare_data.py 
* train.py
* evaluate_model_merics.py to evaluate trained model on eval/test data. propertyFile
* if model satisfy a condition, store it in Model registry

### SageMaker Projects
* Creates end-to-end ML solutions with CI/CD practices like source and version control, as well as the ability to trigger downstream deployments off of an approved model in the model registry. 
* Projects have built in MLOps templates that provision and pre configure the underlying resources that are needed to build end to end CI/CD pipelines. These pipelines include things like source control for your model build and deployment code, automatic integration with SageMaker model registry, as well as approval workflows to start downstream deployments to other environments. You can use these built-in project templates or you can also create your own project templates.
  * Templates are Build, Train, Deploy; Build, Train; Deploy






