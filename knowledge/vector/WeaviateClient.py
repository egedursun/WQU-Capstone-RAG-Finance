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
            # Replace w/ your Weaviate instance API key
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

    def add_object(self):
        # TODO: Add object method
        pass

    def delete_object(self):
        # TODO: Delete object method
        pass


if __name__ == "__main__":
    try:
        weave = WeaviateClient()
        client = weave.connection
        print(client)
    except Exception as e:
        print(e)



