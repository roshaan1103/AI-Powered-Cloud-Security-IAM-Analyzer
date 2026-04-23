import boto3


def get_s3_buckets():
    s3 = boto3.client('s3')

    buckets = s3.list_buckets()['Buckets']
    bucket_data = []

    for bucket in buckets:
        name = bucket['Name']

        bucket_info = {
            "Name": name,
            "Public": False,
            "Encryption": False,
            "Versioning": False
        }

        #  Check Public Access (ACL)
        try:
            acl = s3.get_bucket_acl(Bucket=name)
            for grant in acl['Grants']:
                if 'URI' in grant['Grantee'] and "AllUsers" in grant['Grantee']['URI']:
                    bucket_info["Public"] = True
        except:
            pass

        #  Check Encryption
        try:
            s3.get_bucket_encryption(Bucket=name)
            bucket_info["Encryption"] = True
        except:
            pass

        # Check Versioning
        try:
            versioning = s3.get_bucket_versioning(Bucket=name)
            if versioning.get("Status") == "Enabled":
                bucket_info["Versioning"] = True
        except:
            pass

        bucket_data.append(bucket_info)

    return bucket_data