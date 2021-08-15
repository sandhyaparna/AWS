# Download entire data in S3 bucket into SageMakeStudio
# bucket path is s3://sagemaker-us-east-1-421851816171
# a folder called s3_bucket_data will be created in sagemaker studio console
!aws s3 sync s3://sagemaker-us-east-1-421851816171 s3_bucket_data  
 
# Zip contents of the s3_bucket_data in SageMakeStudio console to a zipped folder and download the zipped folder
# https://stackoverflow.com/questions/54931270/download-an-entire-folder-from-aws-sagemaker-to-laptop
# RUN in TERMINAL
sudo yum install zip unzip
zip -r -X archived_folder_name.zip . # to zip all contents in studio console
zip -r -X archived_folder_name.zip s3_bucket_data  # to zip contents of a specific folder only. in this eg s3_bucket_data is zipped 





