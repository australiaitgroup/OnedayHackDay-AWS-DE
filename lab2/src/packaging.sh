[ -e extract_rds.zip ] && rm extract_rds.zip
[ -d package ] && rm -r package
pip3 install --target ./package pymysql pandas
cd package
zip -r ../extract_rds.zip .
cd ..
zip -g extract_rds.zip extract_rds.py
aws s3 cp extract_rds.zip s3://chao-mu-deployment/deployment/extract_rds.zip