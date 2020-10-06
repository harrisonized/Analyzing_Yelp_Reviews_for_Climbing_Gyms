import re
import json


# Objects included in this file:

# Functions included in this file:
# # get_review_data
# # get_business_data


def get_review_data(pages, business_id):
    """Note: As of Oct. 5, 2020, this script no longer works.
    Returns a list of dictionaries, one for each page
    """
    data_list = []

    for page in pages[1:]:
        # Get useful, funny, and cool attributes
        vote_types = page.findAll("span", {"class": "vote-type"})
        vote_types = [x.get_text().strip() for x in vote_types]
        vote_counts = page.findAll("span", {"class": "count"})
        vote_counts = [0 if x.get_text() == '' else int(x.get_text()) for x in vote_counts]
        votes = dict(zip(vote_types, vote_counts))

        date = page.find('span', {"class": "rating-qualifier"}).get_text().replace("\n", "").strip()  # Get date
        date = re.search(r'^\d{1,2}\/\d{1,2}\/\d{4}', date).group(0)  # Use regex to extract text

        data_dict = {'business_id': business_id,
                     'date': date,
                     'useful': votes.get('Useful'),
                     'funny': votes.get('Funny'),
                     'cool': votes.get('Cool'),
                     'stars': int(float(page.find('div', {"class": "biz-rating biz-rating-large clearfix"}).div.div.get(
                         "title").replace(" star rating", ""))),
                     'review_id': page.get("data-review-id"),
                     'user_id': page.get("data-signup-object", '').replace("user_id:", ""),
                     'user_name': page.find('li', {'class': 'user-name'}).get_text().strip(),
                     'text': page.findAll('div', {"class": "review-content"})[0].find('p').get_text(),
                     }

        data_list.append(data_dict)

    return data_list


def get_business_data(page):
    """Note: As of Oct. 5, 2020, this script no longer works.
    """

    # Business Info
    business_info_list = page.findAll("script", {"type": "application/ld+json"})
    business_info_script = business_info_list[-1]
    business_info_text = business_info_script.get_text().strip().replace("true", "True").replace("false",
                                                                                                 "False").replace(
        "null", "None")
    business_info = json.loads(business_info_text)

    # Map info
    map_info_text = page.findAll("div", attrs={"class": "lightbox-map hidden"})[0].get("data-map-state").replace("true", "True").replace(
        "false", "False").replace("null", "None")
    map_info = json.loads(map_info_text)

    # Categories 
    category_str_list = page.find("span", attrs={"class": "category-str-list"}).findAll('a')
    categories = [category.get_text() for category in category_str_list]
    category_str = ', '.join(categories)

    # Attributes
    if page.find("div", {"class": "short-def-list"}):
        attribute_keys = page.find("div", {"class": "short-def-list"}).findAll("dt", {"class": "attribute-key"})
        attribute_keys = [key.get_text.strip for key in attribute_keys]
        attribute_values = page.find("div", {"class": "short-def-list"}).findAll("dd")
        attribute_values = [val.get_text().strip() for val in attribute_values]
        attributes = dict(zip(attribute_keys, attribute_values))
    else:
        attributes = None

    # Hours
    hours = {}
    if page.find("table", {"class": "table table-simple hours-table"}):
        day_table = page.find("table", {"class": "table table-simple hours-table"}).findAll("th")
        hours_table = page.find("table", {"class": "table table-simple hours-table"}).findAll('td')
        for i, day in enumerate(day_table):
            hours[day.get_text()] = hours_table[2 * i].get_text().strip()
    else:
        hours = None

    data = {'business_id': page.find("div", {"class": "lightbox-map hidden"}).get("data-business-id"),
            'is_open': 1 if re.findall(r'"biz_closed": \[[0-9], \"(True|False)\"\]', page.text) else 0,

            'name': business_info.get('name'),
            'telephone': business_info.get('telephone'),
            'address': business_info.get('address', {}).get('streetAddress', '').replace('\n', ' '),
            'city': business_info.get('address', {}).get('addressLocality'),
            'state': business_info('address', {}).get('addressRegion'),
            'postal_code': business_info.get('address', {}).get('postalCode'),
            'stars': business_info.get('aggregateRating', {}).get('ratingValue'),
            'review_count': business_info.get('aggregateRating', {}).get('reviewCount') or 0,

            'link_id': map_info.get('markers', [{}])[1].get('url', '').replace('/biz/', ''),
            'latitude': map_info.get('markers', [{}])[1].get('location', {}).get('latitude'),
            'longitude': map_info.get('markers', [{}])[1].get('location', {}).get('longitude'),

            'categories': category_str,
            'attributes': attributes,
            'hours': hours}

    return data
