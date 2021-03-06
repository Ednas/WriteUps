# Burp Suite Basics: HTTPS
Most websites use the HTTPS protocol to securely send and receive data between the browser and the server. This process is achieved using SSL/TLS encryption.

## Lab
Tasks
1. Set proxy settings in Firefox to proxy traffic through Burp.
2. Navigate to www.mngr.io and view the certificate error message.
3. Install the Burp CA to Firefox.
4. Browse www.mngr.io and capture the cookie.

### Question 1
Proxy web traffic through Burp and navigate to 'www.mngr.io'. What is the certificate error code displayed?

Start Burp
Change firefox networking - https://portswigger.net/burp/documentation/desktop/getting-started/proxy-setup/browser/firefox
Go to https://www.mngr.io
SEC_ERROR_UNKNOWN_ISSUER

### Question 2
What is the URL entered to get the Burp CA?
http://burp

### Question 3
Using Intercept, browse to www.mngr.io. What is the value of the cookie set when the 'Test Login' button is clicked?

Start by going to http://burp
Download CA certificate
In Firefox ‘Preferences’ option. Go to the ‘Privacy and Security’ settings and click ‘View Certificates’. 
Go to the ‘Authorities’ tab and then click on ‘Import’, choosing the previously saved Burp Certificate Authority (CA). 
Ensure that the option to allow this certificate to identify web sites is checked.
Go to www.mngr.io

In burp suite, set target to www.mngr.io
On the Proxy tab, go to Intercept and just click on Forward a bunch of times
Once the web page loads, click Test Login
Click Forward in Burp suite
Go to browser, see token, this is not the token you're looking for: bb0f0d
Open Inspector, storage, Cookies
Mngr-Cookie: 8583bb

### Question 4
What does CA stand for?
Certificate Authority
