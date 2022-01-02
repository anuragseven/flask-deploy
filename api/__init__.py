from flask_restful import Api, Resource
import config

api = Api(prefix=config.API_PREFIX)


class About(Resource):
    def get(self):
        return "This is flask server for ML Recommendation service", 200


api.add_resource(About, '/about')
