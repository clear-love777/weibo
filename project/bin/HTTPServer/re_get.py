import re
def res(str):
    str=re.search(r"\.?\..+$", str).group().lstrip(".")
    try:
        str = re.search(r"\.(.+)$", str).group().lstrip(".")
        try:
            str=re.search(r"\.(.+)$", str).group().lstrip(".")
            return str
        except Exception:
            return str
    except Exception:
        return str
re1="\.?\..+$"
re2="\.(.+)$"
re3=""