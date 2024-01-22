from amazon.paapi import AmazonAPI


#asin     = products["data"][0].asin
#price    = products["data"][0].offers.listings[0].price.amount
#url      = products["data"][0].detail_page_url
#title    = products["data"][0].item_info.title.display_value

def asin2jan(ASIN, keys):
	#"Please define keys as follows: keys = [key, secret, tag, country]"
	amazon = AmazonAPI(keys[0], keys[1], keys[2], keys[3])
	products = amazon.search_items(keywords=ASIN)
	JAN = products["data"][0].item_info.external_ids.ea_ns.display_values[0]
	return JAN

def jan2asin(JAN, keys):
	#"Please define keys as follows: keys = [key, secret, tag, country]"
	amazon = AmazonAPI(keys[0], keys[1], keys[2], keys[3])
	products = amazon.search_items(keywords=JAN)
	asin = products["data"][0].asin
	return asin
