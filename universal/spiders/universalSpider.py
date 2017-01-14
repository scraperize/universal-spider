import scrapy
import yaml

class universalSpider(scrapy.Spider):

    name = "universal"
    parameters = None

    def __init__(self, *args, **kwargs):

        worker = kwargs.get("worker")

        if not worker:
            exit("You must specify worker name : -a worker=name")

        self.parameters = yaml.load(file("./workers/" + worker + ".yml", "r"))

        super(universalSpider, self).__init__(*args, **kwargs)
        self.start_urls = self.parameters["urls"]
        self.allowed_domains = self.parameters["domains"]

    def parse(self, response):

        wrapper = "html"
        if "wrapper" in self.parameters and "css" in self.parameters["wrapper"]:
            wrapper = self.parameters["wrapper"]["css"]

        for item in response.css(wrapper):

            data = {}

            for columnName in self.parameters["columns"]:
                columnOptions = self.parameters["columns"][columnName]
                data[columnName] = str(item.css(columnOptions["css"]).extract_first().strip().encode(self.parameters["charset"])),

            yield data
