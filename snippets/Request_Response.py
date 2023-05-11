""" request.POST  # Only handles form data. Only wokrs for 'POST' method
    request.data # Handles arbitrary daat . Works for 'POST', 'PUT' and 'PATCH' method
    
    return Response(data) # Renders to content type as requested by client
    
    """