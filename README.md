# PhishBlocker

### Malicious URL detector to prevent security threat

### Problem Statement:
Security threats like phishing and spamming are very common in the world of internet today. Many times, we come across websites having URLs that may look benign but are acutually a route to security attacks like phishing and spamming. Our objective is to alert the user of such Malicious URLs so as to prvent such security threats. Therefore, we propose to create an ML model to detect malicious URLs. We can then deploy this model using a chrome extension.
Traditional Solution:
The traditional approach to prevent attacks like phishing, spam ,etc. involved balcklisting/whitelisting. However, since the list is not comprehensive and there can be other malicious URLs that can crop up.

### Abstract:
To tackle this issue and overcome limitations of the traditional solution, we are utilizing Machine Learning and Classification to find any such harmful URLs and notify user. To improve user experience, we will provide this feature as a Chrome Extension. To summeerize, the user installs the chrome extension and then for each web page the user visits, the extension will scan the page for URLs, send the URLs to a backend system which will then check the cache if the URL was checked before. If not, then it makes inference and returns the results to the front end. The front end will highlight the bad URLs for the user on the website they're on.

### Approach:
This project involves researching and building the following:
 - ML model for detection/classification
 - Back end for serving requests and making inference (includes caching)
 - Frontend that interacts with backend (this is a chrome extension)

### Dataset: http://www.sysnet.ucsd.edu/projects/url/#datasets
 
