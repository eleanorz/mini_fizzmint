from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	return render_to_response('index.html', context_instance = RequestContext(request))

def contact(request):
	return render_to_response('contact.html', context_instance = RequestContext(request))

# OLD INLINE HTML:   from django.http import HttpResponse

# def home(request):
# 	message = """
# 	<html>
# 		<body>
# 			<h1>Welcome to Django</h1>
# 				<form action=''>
# 					<select>
# 						<option value="">Billy</option>
# 						<option value="">Sandra</option>
# 						<option value="">Joseph	</option>
# 						<option value="">Kesha</option>
# 					</select>
# 				</form>
# 		</body>
# 	</html>
# 	"""
# 	return HttpResponse(message)
