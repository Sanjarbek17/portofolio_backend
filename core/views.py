from django.http import HttpResponse

def download_text_file(request):
    # Define the content of the text file
    with open('tex.txt') as f:

        content = f.read()

        # Create the HttpResponse object with the appropriate content type
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="example.txt"'

        return response

    return HttpResponse('no data error')