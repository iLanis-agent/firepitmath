import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

BLOCK_CM = 40
COURSES = 3
MARGIN_CM = 30
GRAVEL_CM = 10
BAG_L = 25
CLEAR_M = 3

def ring_plan(diamCm):
    if not (diamCm > 0):
        return {"error": "the pit diameter must be positive"}
    per_course = math.ceil(math.pi * diamCm / BLOCK_CM)
    blocks = per_course * COURSES
    if diamCm <= 60: verdict = "a tabletop ring"
    elif diamCm <= 100: verdict = "a classic ring"
    else: verdict = "a bonfire ring"
    return {"perCourse": per_course, "blocks": blocks, "verdict": verdict}

def gravel_plan(diamCm):
    if not (diamCm > 0):
        return {"error": "the pit diameter must be positive"}
    base_cm = diamCm + 2 * MARGIN_CM
    r = base_cm / 200
    area = round1(math.pi * r * r)
    liters = round1(area * GRAVEL_CM * 10)
    bags = math.ceil(liters / BAG_L)
    if liters <= 100: verdict = "a wheelbarrow load"
    elif liters <= 400: verdict = "a few trips"
    else: verdict = "a delivery job"
    return {"baseCm": base_cm, "area": area, "liters": liters, "bags": bags, "verdict": verdict}

def clearance_plan(diamCm, spaceM):
    if not (diamCm > 0) or not (spaceM > 0):
        return {"error": "the pit diameter and the space must be positive"}
    need = round1(diamCm / 100 + 2 * CLEAR_M)
    spare = round1(spaceM - need)
    if spare >= 1: verdict = "fits with room to spare"
    elif spare >= 0: verdict = "fits, right at the labeled clearance"
    else: verdict = "is too tight - move it or shrink it"
    return {"need": need, "spare": spare, "verdict": verdict}

def render_ring(r, diamCm):
    return ("A fire ring " + fmt(diamCm) + " cm across takes " + plural(r["perCourse"], "block") + " of a labeled "
            + fmt(BLOCK_CM) + " cm per course - " + plural(r["blocks"], "block") + " over a labeled "
            + fmt(COURSES) + " courses, " + r["verdict"] + ".")

def render_gravel(r, diamCm):
    return ("A " + fmt(diamCm) + " cm ring plus a labeled " + fmt(MARGIN_CM) + " cm margin each side asks a base "
            + fmt(r["baseCm"]) + " cm across: " + fmt(r["area"]) + " m2 at a labeled " + fmt(GRAVEL_CM)
            + " cm deep is " + fmt(r["liters"]) + " L - " + plural(r["bags"], "bag") + " of labeled "
            + fmt(BAG_L) + " L, " + r["verdict"] + ".")

def render_clearance(r, diamCm, spaceM):
    return ("A " + fmt(diamCm) + " cm ring asks a labeled " + fmt(CLEAR_M) + " m clearance each side - a clear circle "
            + fmt(r["need"]) + " m across; your " + fmt(spaceM) + " m space " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[90],[45],[150],[60],[100],[75],[120],[30],[0],[110]]:
    add("ringPlan", ring_plan, render_ring, a)
for a in [[90],[45],[200],[60],[120],[150],[75],[100],[0],[30]]:
    add("gravelPlan", gravel_plan, render_gravel, a)
for a in [[90,8],[90,7],[90,5],[45,4],[150,9],[60,6],[120,8],[75,7],[0,8],[90,0]]:
    add("clearancePlan", clearance_plan, render_clearance, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
