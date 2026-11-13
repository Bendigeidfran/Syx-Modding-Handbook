// The tooltip for interactive sprite sheets (see site_sheets.py). Without this
// script the sheet still shows and lifts, but its sections have no visible text.
(function () {
  var tip = null;
  var current = null;

  function element() {
    if (!tip) {
      tip = document.createElement("div");
      tip.className = "sheet-tip";
      tip.setAttribute("role", "tooltip");
      tip.appendChild(document.createElement("strong"));
      tip.appendChild(document.createElement("code"));
      tip.appendChild(document.createElement("span"));
      document.body.appendChild(tip);
    }
    return tip;
  }

  function place(part) {
    var box = part.getBoundingClientRect();
    var t = element();
    var gap = 10;
    var edge = 8;
    var left = box.left + box.width / 2 - t.offsetWidth / 2;
    left = Math.max(edge, Math.min(left, document.documentElement.clientWidth - t.offsetWidth - edge));
    // Above the section, unless there's no room there.
    var top = box.top - t.offsetHeight - gap;
    if (top < edge) top = box.bottom + gap;
    t.style.left = left + "px";
    t.style.top = top + "px";
  }

  function show(part) {
    var t = element();
    current = part;
    t.children[0].textContent = part.getAttribute("data-title");
    t.children[1].textContent = part.getAttribute("data-pos");
    t.children[2].textContent = part.getAttribute("data-tip");
    t.classList.add("is-open");
    place(part);
  }

  function hide() {
    clearTimeout(leaving);
    current = null;
    if (tip) tip.classList.remove("is-open");
  }

  function partOf(event) {
    var el = event.target;
    return el && el.closest ? el.closest(".sheet-part") : null;
  }

  function onTip(el) {
    return tip && el && tip.contains(el);
  }

  // WCAG 1.4.13: the pointer can cross the gap onto the tooltip and stay there
  // without it closing, so it closes a moment after the pointer leaves both.
  var leaving = null;
  function leave() {
    clearTimeout(leaving);
    leaving = setTimeout(function () {
      // Keep showing the section that has keyboard or tap focus.
      var focused = document.activeElement;
      if (focused && focused.classList && focused.classList.contains("sheet-part")) show(focused);
      else hide();
    }, 300);
  }

  document.addEventListener("mouseover", function (e) {
    var part = partOf(e);
    if (part) {
      clearTimeout(leaving);
      show(part);
    } else if (onTip(e.target)) {
      clearTimeout(leaving);
    }
  });
  document.addEventListener("mouseout", function (e) {
    if ((partOf(e) || onTip(e.target)) && !onTip(e.relatedTarget)) leave();
  });
  document.addEventListener("focusin", function (e) {
    var part = partOf(e);
    if (part) show(part);
  });
  document.addEventListener("focusout", function (e) {
    if (partOf(e)) hide();
  });
  // Some browsers don't focus a button when it's tapped.
  document.addEventListener("click", function (e) {
    var part = partOf(e);
    if (part) show(part);
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && current) {
      if (document.activeElement === current) current.blur();
      hide();
    }
  });
  window.addEventListener("scroll", function () {
    if (current) place(current);
  }, { passive: true });
  window.addEventListener("resize", function () {
    if (current) place(current);
  });
})();
