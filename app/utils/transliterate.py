import re
_cyr_to_lat = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo','ж':'zh','з':'z','и':'i','й':'y',
    'к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f',
    'х':'kh','ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'','ы':'y','ь':'','э':'e','ю':'yu','я':'ya'}
_lat_to_cyr = {'shch':'щ','sh':'ш','ch':'ч','kh':'х','ts':'ц','zh':'ж','yo':'ё','yu':'ю','ya':'я',
    'a':'а','b':'б','v':'в','g':'г','d':'д','e':'е','z':'з','i':'и','y':'й','k':'к','l':'л','m':'м',
    'n':'н','o':'о','p':'п','r':'р','s':'с','t':'т','u':'у','f':'ф'}
def normalize_name(name: str) -> str:
    if not name: return ""
    s = name.strip()
    s = re.sub(r"[\s]+", " ", s)
    return s
def cyr_to_lat(name: str) -> str:
    name = normalize_name(name).lower()
    res = []
    for ch in name:
        res.append(_cyr_to_lat.get(ch, ch))
    return "".join(res)
def lat_to_cyr(name: str) -> str:
    s = name.lower()
    for digraph in sorted(_lat_to_cyr.keys(), key=lambda x: -len(x)):
        s = s.replace(digraph, _lat_to_cyr[digraph])
    s = re.sub(r'[^а-яё\s]', '', s)
    s = re.sub(r'[\s]+', ' ', s).strip()
    return s
def generate_name_variants(name: str):
    name = normalize_name(name)
    variants = [name]
    import re
    if re.search(r'[А-Яа-яЁё]', name):
        lat = cyr_to_lat(name)
        variants.append(lat)
        parts = name.split()
        if len(parts) >= 2:
            variants.append(parts[-1] + " " + (parts[0][0] + "."))
            variants.append(cyr_to_lat(parts[-1] + " " + (parts[0][0] + ".")))
    else:
        try:
            cyr = lat_to_cyr(name)
            if cyr and cyr not in variants:
                variants.append(cyr)
        except Exception:
            pass
    seen = []
    for v in variants:
        if v and v not in seen:
            seen.append(v)
    return seen
