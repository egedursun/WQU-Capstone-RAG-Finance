import weaviate
import dotenv

dotenv.load_dotenv()
config = dotenv.dotenv_values()


class WeaviateClient:

    def __init__(self,
                 url=config["WEAVIATE_URL"],
                 api_key=config["WEAVIATE_API_KEY"],
                 openai_api_key=config["OPENAI_API_KEY"]):
        self.connection = weaviate.Client(
            url=url,
            auth_client_secret=weaviate.AuthApiKey(api_key=api_key),
            additional_headers={
                "X-OpenAI-Api-Key": openai_api_key
            }
        )
        self.connection.timeout_config = (30, 60)

    def add_class(self, class_schema):
        try:
            self.connection.schema.create_class(class_schema)
        except Exception as e:
            print(e)
            return False
        return True

    def add_object(self, class_name, data):
        try:
            self.connection.data_object.create(data_object=data, class_name=class_name)
        except Exception as exception:
            print(exception)
            return False

    def delete_object(self, uuid):
        try:
            self.connection.data_object.delete(uuid=uuid)
        except Exception as exception:
            print(exception)
            return False


if __name__ == "__main__":
    try:
        weave = WeaviateClient()
        client = weave.connection
        print(client)
    except Exception as e:
        print(e)



