class Website:
    def __init__(self, host, domain, queries=None):
        self.host = host
        self.domain = domain
        self.queries = self.set_queries(queries)

    def set_queries(self, queries):
        self.queries = []

        if queries is not None:
            self.queries.extend(queries)
        return self.queries


if __name__ == '__main__':

    data_list = input().split(" | ")

    websites_list = []

    while not data_list[0] == "end":
        curr_host = data_list[0]
        curr_domain = data_list[1]
        curr_queries = data_list[2].split(",") if len(data_list) > 2 else None

        website = Website(host=curr_host, domain=curr_domain, queries=curr_queries)

        websites_list.append(website)

        data_list = input().split(" | ")

    for website in websites_list:
        if len(website.queries) > 0:
            queries = list(map(lambda q: '[' + q + ']', website.queries))
            print(f"https://www.{website.host}.{website.domain}/query?={'&'.join(map(str, queries))}")
        else:
            print(f"https://www.{website.host}.{website.domain}")
