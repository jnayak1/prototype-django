class MyMiddleware(object):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = "localhost:4200"
        return response