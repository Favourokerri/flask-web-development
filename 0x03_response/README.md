### Response Cycle
    a response is triggered by a request sent by the user
    when a user sends a request, the request triggers a view function
    that in turn returns a request.

### Request Hooks
    request hooks are used to execute code before
    or after each request is made.
    we have the following request hooks

    1) before_first_request() ==> this is executed before the user 
        makes any request
    2) before_request() ==> this is executed before each request
    3) after_request() ==> executed after each request is made
    4) tear_down ==> exectued after each request even if an unhandeled 
       exception occurs.
       