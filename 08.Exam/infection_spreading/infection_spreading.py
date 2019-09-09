if __name__ == '__main__':
    countries_dict = {country: 0 for country in input().split(', ')}
    under_quarantine_countries_list = []

    days = int(input())

    for day in range(days):
        command, country = input().split()

        if command == 'Fast_Infect':
            # check in dict if exist
            if country in under_quarantine_countries_list:
                print(f'{country} is under quarantine')
            else:
                countries_dict[country] += 20
        elif command == 'Slow_Infect':
            if country in under_quarantine_countries_list:
                print(f'{country} is under quarantine')
            else:
                countries_dict[country] += 10
        elif command == 'Quarantine':
            if country in under_quarantine_countries_list:
                print(f'{country} is already under quarantine')
            else:
                under_quarantine_countries_list.append(country)
        elif command == 'Cure':
            countries_dict[country] = 0

    for kvp in sorted(countries_dict.items(), key=lambda kvp: -kvp[1]):
        print(f'{kvp[0]} - {kvp[1]}% infected')
