# Page Load Time Tester

## Description
A simple webpage performance tester using selenium <br/>

Require chromedriver, downloadable from <http://chromedriver.chromium.org/downloads>

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
  "url": "https://github.com/dodinhtrung97/page-load-time-tester/blob/master/src/main.py",
  "averageLoadingTime": 1122.7141666689324,
  "resultSet": [
    {
      "loadingTime": 2974.0399999936926,
      "attempt_1": [
        {
          "entryType": "navigation",
          "initiatorType": "navigation",
          "loadingTime": 1128.8899999999558,
          "name": "https://github.com/dodinhtrung97/page-load-time-tester/blob/master/src/main.py"
        },
        {
          "entryType": "resource",
          "initiatorType": "link",
          "loadingTime": 186.60499999532476,
          "name": "https://github.githubassets.com/assets/frameworks-2322f54af916007dd939df6c24bd2264.css"
        },
        {
          "entryType": "resource",
          "initiatorType": "link",
          "loadingTime": 188.09999999939464,
          "name": "https://github.githubassets.com/assets/site-fb3830abec4858c7644fa8b4f8759252.css"
        },
        ...
      ]
      ...
    }
    ...
  ]
}
```