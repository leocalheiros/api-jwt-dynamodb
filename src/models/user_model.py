import boto3


ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = ddb.Table('UsersTest')


class UserModel:

    @staticmethod
    def create_user(user_id, email, senha):
        try:
            response = table.put_item(
                Item={
                    'user_id': user_id,
                    'email': email,
                    'senha': senha
                }
            )
            return True
        except Exception as error:
            print(str(error))
            return False

    @staticmethod
    def get_all_users():
        try:
            response = table.scan()
            result = response['Items']
            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                result.extend(response['Items'])
            return result
        except Exception as error:
            print(str(error))
            return False

    @staticmethod
    def login_user(email, senha):
        try:
            response = table.scan(
                FilterExpression='email = :email AND senha = :senha',
                ExpressionAttributeValues={
                    ':email': email,
                    ':senha': senha
                }
            )
            return response.get('Items', [])
        except Exception as error:
            print(str(error))
            return []

    @staticmethod
    def delete_user(user_id):
        try:
            response = table.delete_item(
                Key={'user_id': user_id}
            )
            return True
        except Exception as error:
            print(str(error))
            return False
