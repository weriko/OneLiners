a = lambda dictionary, rang: ["".join(  [dictionary.get((x % int(k) == 0)*str(k), ""  ) for k in dictionary.keys()  ]) or str(x) for x in range (rang[0],rang[1]) ]; print(a({"3":"fizz","5":"buzz","7":"something","13":"notcreative"},(0,200)))
