```python
from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='AI Agent Publicist API',
    description='A detailed API description for the AI Agent Publicist',
)

ns = api.namespace('ai_publicist', description='Publicist operations')

media_channel = api.model('Media Channel', {
    'id': fields.String(required=True, description='The media channel identifier'),
    'name': fields.String(required=True, description='The media channel name'),
})

@ns.route('/media_channels')
class MediaChannelList(Resource):
    '''Shows a list of all media channels, and lets you POST to add new channels'''
    @ns.doc('list_media_channels')
    def get(self):
        '''List all media channels'''
        return media_channels

    @ns.doc('create_media_channel')
    @ns.expect(media_channel)
    @ns.marshal_with(media_channel, code=201)
    def post(self):
        '''Create a new media channel'''
        return api.payload, 201

if __name__ == '__main__':
    app.run(debug=True)
```