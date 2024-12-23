import django.http as dh
import os

def simple_http_response(request):
    return dh.HttpResponse("This is a simple HTTP response.")

def redirect_response(request):
    return dh.HttpResponseRedirect("https://www.djangoproject.com/")

def permanent_redirect_response(request):
    return dh.HttpResponsePermanentRedirect("https://www.djangoproject.com/")

def not_modified_response(request):
    return dh.HttpResponseNotModified()

def bad_request_response(request):
    return dh.HttpResponseBadRequest("Bad request: Your input is invalid.")

def forbidden_response(request):
    return dh.HttpResponseForbidden("You are not authorized to access this resource.")

def gone_response(request):
    return dh.HttpResponseGone("This resource is no longer available.")

def server_error_response(request):
    return dh.HttpResponseServerError("An internal server error occurred.")

def not_found_response(request):
    return dh.HttpResponseNotFound("<h1>404 - Resource Not Found</h1>")

def json_response(request):
    data = {"message": "This is a JSON response", "status": "success"}
    return dh.JsonResponse(data)

def stream_response(request):
    def stream():
        for i in range(1, 6):
            yield f"Chunk {i}\n"
    return dh.StreamingHttpResponse(stream(), content_type="text/plain")

def file_response(request):
    file_path = os.path.join(os.path.dirname(__file__), "file_response.txt")
    with open(file_path, "w") as f:
        f.write("This is a file response.")

    return dh.FileResponse(
        open(file_path, "rb"), content_type="text/plain", 
        as_attachment=True, filename="file_response.txt")
