import dotenv
import requests

dotenv.load_dotenv()
config = dotenv.dotenv_values()


class PolygonClient:

    def __init__(self, url=config['POLYGON_API_URL'], key=config['POLYGON_API_KEY']):
        self.url = url
        self.key = key

    def request(self, request,
                method='GET',
                headers=None,
                payload=None,
                url_params=None,
                query_params=None):
        if method == 'GET':
            # TODO: Implement get method handler
            requests.get(self.url, params=query_params)
        elif method == 'POST':
            # TODO: Implement post method handler
            requests.post(self.url, params=query_params)
        else:
            raise Exception('Invalid method call: {}'.format(method))
