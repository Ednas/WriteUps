About:
As seen in Episodes 1 and 2, Snort rules are powerful but difficult to write. In this episode we will take a closer look at alerting on HTTP requests.

Lab:
Question 1
Create a Snort rule that looks for ‘msn.com’ in an HTTP cookie value. Test the rule and enter the token.
This matches 8 packets, but isn't getting the cookie
alert tcp any any -> any any (msg: "msn.com in cookie"; content: "|6d 73 6e 63 6f 6d|"; http_cookie; sid:1000001;)


Question 2
Create a Snort rule that looks for an HTTP method ‘GET’ and contains ‘gif’ in the URL. Test the rule and enter the token.
alert tcp any any -> any any (msg: "msn.com in cookie"; content: "GET"; http_method; content: "|67 69 66|"; http_uri; sid:1000001;)

Question 3
https://stackoverflow.com/questions/54015580/snort-rule-http-body-content
Confusing question, it wanted file data. Also it didn't like the Hex numbers
http_client_body = the request body

file_data = the response body*
Create a rule that will alert when 'MZ' are first two characters in the HTTP body. Test the rule and enter the token.
alert tcp any any -> any any (msg: "alert MZ first 2 chars in HTTP Body"; file_data; content:"MZ"; depth: 2; sid:1000001;)

Question 4
If you wanted a rule to match on a URI string that has been URI decoded, which modifier would you use?
http_uri

The `http_raw_cookie` keyword is a content modifier that restricts the search to the
extracted UNNORMALIZED Cookie Header field of a HTTP client request or a HTTP server  response. 
As this keyword is a modifier to the previous '`content`' keyword, there must be a content in the rule before 
'`http_raw_cookie`' is specified. This keyword is dependent on the '`enable_cookie`' config option. 
The Cookie Header field will be extracted only when this option is configured.

