# Why?

I saw booktype a few years ago and was intrigued. I tried to follow directions but just didn't have an easy time of it.
Being that the main repo is no longer maintained, options were limited. So I learned enough python 2 and 3 to make corrections to get it running.

## What?

The docker files should be enough to get a running production environment. The image is already large with the additions (I had some issues using python:3-slim) so I did not include calibre for mobi support. It has been depracated and epub is recommended by Amazon since 2022 anyway.

I did use most of the files from <https://github.com/booktype/booktype-docker.git> in addition to this forked repo. I have also updated most of the dependencies to be as up to date as pip-compile allows.

## What else?

There are still some issues in import/export that I want to sort out, mostly toc and styling. All of the tests currently pass without error or warning. I altered some string comparisons in favor of dict values.
