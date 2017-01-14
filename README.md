# Universal Spider (beta)

Universal spider for scrapy

## Configuration example

    domains: ["stackoverflow.com"]
    charset: "utf-8"
    wrapper:
        css: "div.question-summary > div.summary"
    columns:
        title:
            type: "string"
            css: "h3 > a ::text"
        link:
            type: "string"
            css: "h3 > a ::attr(href)"
    urls:
        - "http://stackoverflow.com/"

## Usage

    scrapy crawl universal -a worker=example
