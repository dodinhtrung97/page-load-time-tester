# Page Load Time Tester

## Description
A simple webpage performance tester using selenium <br/>

Require chromedriver, downloadable from `http://chromedriver.chromium.org/downloads`

## Language
Python

## Usage

Running `py src\main.py -h` will return

```
usage: main.py [-h] DRIVER URL LOG

Page loading performance test

positional arguments:
  DRIVER      Relative path to chromedriver
  URL         URL of page to do performance test
  LOG         Name of output json log file

optional arguments:
  -h, --help  show this help message and exit
```

Running `py src\main.py chromedriver.exe http://chromedriver.chromium.org/downloads performance.json` will return a log file in `/log` folder whose data is in json format <br/>

For example: </br>

```
{
  "loadingTime": 4610.885000001872,
  "resultSet": [
    {
      "entryType": "navigation",
      "initiatorType": "navigation",
      "loadingTime": 2151.194999998552,
      "name": "http://chromedriver.chromium.org/downloads"
    },
    {
      "entryType": "resource",
      "initiatorType": "link",
      "loadingTime": 155.13500000088243,
      "name": "http://www.gstatic.com/sites/p/d6fdbe/system/app/themes/ski/standard-css-ski-ltr-ltr.css"
    },
    {
      "entryType": "resource",
      "initiatorType": "link",
      "loadingTime": 1394.894999997632,
      "name": "http://chromedriver.chromium.org/_/rsrc/1553869715000/system/app/css/overlay.css?cb=ski10a250goog-ws-leftnone30themedefaultstandard"
    },
    ...
}
```