import scrapy

class DictionarySpider(scrapy.Spider):
    name = "dictionary"
    start_urls = [
        'https://www.dictionary.com/browse/ab',
    ]

    def parse(self, response):
        word = response.css('section.entry-headword h1::text').get()
        ipa_word = response.css('span.pron-ipa-content::text').get()
        yield {
            'word': word,
            'ipa_word': ipa_word,
        }
        # WIP only visit the exact adjacent word
        # adjacent_word_div = response.css('div.css-1qy26rb')
        # adjacent_word_list = []


        # -------------- Full Scrape ----------------
        # Scrapy should automatically reject already visited pages, therefore we can simply create requests for all adjacent words
        # TODO: Make more robust. I am not sure if the same class is used everywhere. Although i assume it is
        # for href in response.css('div.css-1qy26rb a::attr(href)'):
        #     print(href)
        #     yield response.follow(href, callback=self.parse)

        # ----------------- Reduced Scrape ---------------------
        href = response.css('div.css-1qy26rb a::attr(href)')[-1]
        yield response.follow(href, callback=self.parse)
