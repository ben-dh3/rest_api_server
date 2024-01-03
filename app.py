import os
from flask import Flask
from flask_headers import headers
from flask_caching import Cache

# flask_cache config
config = {
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 30
}
# API response body
api_response_body = {
    "REST" : {"name": "REST", "release_year": 2000, "benefits": "uses existing standards and protocols"},
    "Soap" : {"name": "Soap", "release_year": 1998, "benefits": "strict contract ensures interoperability"},
    "GraphQL" : {"name": "GraphQL", "release_year": 2015, "benefits": "architectural style and query language"},
}
# Create a new Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
@headers({'Cache-Control':'public, max-age=30'})
def get_api_response():
    response = api_response_body
    return response

if __name__ == '__main__':  
    # tell Flask to use the above defined config
    app.config.from_mapping(config)
    cache = Cache(app)
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))