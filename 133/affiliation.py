def generate_affiliation_link(url):
    x = list(url.rpartition("dp/"))
    y = x[2].rsplit("/")
    return('http://www.amazon.com/dp/' + y[0] + '/?tag=pyb0f-20')

