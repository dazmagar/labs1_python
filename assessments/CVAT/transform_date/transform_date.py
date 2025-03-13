import re


def transform_date_format(dates):
    result = []
    for date in dates:
        if match := re.fullmatch(r"(\d{4})/(\d{2})/(\d{2})", date):
            result.append(f"{match[1]}{match[3]}{match[2]}")
        elif match := re.fullmatch(r"(\d{2})-(\d{2})-(\d{4})", date):
            result.append(f"{match[3]}{match[2]}{match[1]}")
        elif match := re.fullmatch(r"(\d) (\d{3})p (\d{2})p (\d{2})", date):
            result.append(f"{match[1]}{match[2]}{match[3]}{match[4]}")
    
    return result

if __name__ == "__main__":
    dates = transform_date_format(["2010/02/20", "2 016p 19p 12", "11-18-2012", "2018 12 24", "20130720"])
    print(dates)
