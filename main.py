class ReverseProxied(object):
    '''Wrap the application in this middleware and configure the
    front-end server to add these headers, to let you quietly bind
    this to a URL other than / and to an HTTP scheme that is
    different than what is used locally.
    :param app: the WSGI application
    '''
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]

        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)

if __name__ == '__main__':
    from argparse import ArgumentParser
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--host <host>] [--port <port>]'
    )
    arg_parser.add_argument('-H', '--host', default='0.0.0.0')
    arg_parser.add_argument('-p', '--port', type=int, default=5000)
    arg_parser.add_argument('-d', '--debug', action='store_true')
    options = arg_parser.parse_args()
    from server import setup_app
    app = setup_app()
    app.wsgi_app = ReverseProxied(app.wsgi_app)
    app.run(host=options.host, port=options.port, debug=options.debug)
