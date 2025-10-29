Make a GET request to `/ui/checksession` to grab your session from the `Set-Cookie` response header (that cookie is required unless you want to 401 unauthorize yourself) then make a POST request to `/ui/lookup`, with your session in the `Cookie` header, and send `{"query":"https://example.com","silent":true}` as the body.

Note: `silent` tells Kaspersky whether to keep your query private or not.
