# tap-exchangeratehost

A [Singer](https://singer.io) tap to extract currency exchange rate
data from [exchangerate.host](http://exchangerate.host).

## Install

```
pip install tap-exchangeratehost
```

## Run

tap-exchangeratehost -c config.json

If you omit config file, the exchange rates are pulled with EUR as
base currency for the date of execution.

## About this project

This tap was inspired by [tap-exchangeragesapi](https://github.com/singer-io/tap-exchangeratesapi).
It was developed as a replacement of it after the original data source
(https://exchangeratesapi.io) started to require a signup and access key,
which is not ideal for the first example of singer.io.

Developed by ANELEN and friends. Please check out the ANELEN's
[open innovation philosophy and other projects](https://anelen.co/open-source.html)

![ANELEN](https://avatars.githubusercontent.com/u/13533307?s=400&u=a0d24a7330d55ce6db695c5572faf8f490c63898&v=4)

---

Copyright &copy; 2021~ Anelen Co., LLC
