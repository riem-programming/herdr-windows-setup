import json, sys, tomllib
schema = json.load(open(sys.argv[1], encoding="utf-8"))
theme = tomllib.load(open(sys.argv[2], "rb"))
defs = schema.get("definitions", schema.get("$defs", {}))
def resolve(node):
    while "$ref" in node:
        node = defs[node["$ref"].split("/")[-1]]
    return node
problems = []
top = schema.get("properties", {})
for section, body in theme.items():
    if section not in top:
        problems.append(f"unknown section [{section}]"); continue
    node = resolve(top[section])
    props = node.get("properties")
    if props is None or not isinstance(body, dict):
        continue
    for key in body:
        if key not in props:
            problems.append(f"unknown key [{section}].{key}")
print("sections checked:", ", ".join(theme.keys()))
print("PROBLEMS:" if problems else "OK: every section and key exists in the schema")
for p in problems: print(" -", p)
