def wsgi_application(environ, start_response):
	data = str(environ.get(QUERY_STRING))
	data = data.replace('&', '\n')
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	start_response(status,headers)
	return [data]