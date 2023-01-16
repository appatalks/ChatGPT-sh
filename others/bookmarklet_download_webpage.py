def download_webpage():
    import urllib.request
    import os

    # Get the current URL
    url = window.location.href

    # Download the webpage
    response = urllib.request.urlopen(url)
    webContent = response.read()

    # Get the filename
    filename = os.path.basename(url)
    filename = os.path.splitext(filename)[0] + ".html"

    # Write the downloaded content to a file
    with open(filename, "wb") as f:
        f.write(webContent)
