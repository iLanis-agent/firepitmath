(function (root) {
  "use strict";
  var BLOCK_CM = 40;  // labeled block face length, cm
  var COURSES = 3;    // labeled courses in the ring
  var MARGIN_CM = 30; // labeled gravel margin each side, cm
  var GRAVEL_CM = 10; // labeled gravel base depth, cm
  var BAG_L = 25;     // labeled gravel bag, L
  var CLEAR_M = 3;    // labeled clearance each side, m

  function round1(x) { return Math.round(x * 10) / 10; }
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }

  function ringPlan(diamCm) {
    if (!(diamCm > 0)) return { error: "the pit diameter must be positive" };
    var perCourse = Math.ceil(Math.PI * diamCm / BLOCK_CM);
    var blocks = perCourse * COURSES;
    var verdict;
    if (diamCm <= 60) verdict = "a tabletop ring";
    else if (diamCm <= 100) verdict = "a classic ring";
    else verdict = "a bonfire ring";
    return { perCourse: perCourse, blocks: blocks, verdict: verdict };
  }

  function gravelPlan(diamCm) {
    if (!(diamCm > 0)) return { error: "the pit diameter must be positive" };
    var baseCm = diamCm + 2 * MARGIN_CM;
    var r = baseCm / 200;
    var area = round1(Math.PI * r * r);
    var liters = round1(area * GRAVEL_CM * 10);
    var bags = Math.ceil(liters / BAG_L);
    var verdict;
    if (liters <= 100) verdict = "a wheelbarrow load";
    else if (liters <= 400) verdict = "a few trips";
    else verdict = "a delivery job";
    return { baseCm: baseCm, area: area, liters: liters, bags: bags, verdict: verdict };
  }

  function clearancePlan(diamCm, spaceM) {
    if (!(diamCm > 0) || !(spaceM > 0)) return { error: "the pit diameter and the space must be positive" };
    var need = round1(diamCm / 100 + 2 * CLEAR_M);
    var spare = round1(spaceM - need);
    var verdict;
    if (spare >= 1) verdict = "fits with room to spare";
    else if (spare >= 0) verdict = "fits, right at the labeled clearance";
    else verdict = "is too tight - move it or shrink it";
    return { need: need, spare: spare, verdict: verdict };
  }

  function renderRing(r, diamCm) {
    return "A fire ring " + diamCm + " cm across takes " + plural(r.perCourse, "block") + " of a labeled "
      + BLOCK_CM + " cm per course - " + plural(r.blocks, "block") + " over a labeled " + COURSES + " courses, " + r.verdict + ".";
  }

  function renderGravel(r, diamCm) {
    return "A " + diamCm + " cm ring plus a labeled " + MARGIN_CM + " cm margin each side asks a base " + r.baseCm
      + " cm across: " + r.area + " m2 at a labeled " + GRAVEL_CM + " cm deep is " + r.liters + " L - "
      + plural(r.bags, "bag") + " of labeled " + BAG_L + " L, " + r.verdict + ".";
  }

  function renderClearance(r, diamCm, spaceM) {
    return "A " + diamCm + " cm ring asks a labeled " + CLEAR_M + " m clearance each side - a clear circle "
      + r.need + " m across; your " + spaceM + " m space " + r.verdict + ".";
  }

  var api = { ringPlan: ringPlan, gravelPlan: gravelPlan, clearancePlan: clearancePlan, renderRing: renderRing, renderGravel: renderGravel, renderClearance: renderClearance };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.FirepitMath = api;
})(this);
