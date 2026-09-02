// ==UserScript==
// @name         Margonem Dwarven Forge UI
// @namespace    doiua97
// @version      1.0.12
// @description  Installs the complete Dwarven Forge dark fantasy UI theme for Margonem.
// @match        https://margonem.pl/*
// @match        https://*.margonem.pl/*
// @run-at       document-end
// @grant        none
// @updateURL    https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js
// @downloadURL  https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js
// ==/UserScript==

(() => {
  const link = document.createElement("link");
  link.id = "dwarven-forge-ui-theme";
  link.rel = "stylesheet";
  link.href = "https://fastly.jsdelivr.net/gh/Doiua97/margonem-dwarven-forge-ui@v1.0.12/css/dwarven-forge.css";

  const mount = () => {
    if (link !== document.head.lastElementChild) document.head.appendChild(link);
  };

  const vis = el => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return s.display !== "none" && s.visibility !== "hidden" && r.width > 0 && r.height > 0;
  };

  const has = side => [...document.querySelectorAll(`.bottom-${side}-additional .widget-button:not(.empty-slot-widget)`)].some(vis);

  const sync = () => {
    const root = document.querySelector(".game-window-positioner");
    if (!root) return;
    root.classList.toggle("df-aw-l", has("left"));
    root.classList.toggle("df-aw-r", has("right"));
  };

  const mark = e => {
    if (!e.target.closest?.(".game-layer")) return;
    const el = document.createElement("i");
    el.className = "df-click";
    el.style.cssText = `left:${e.clientX}px;top:${e.clientY}px`;
    document.body.appendChild(el);
    el.addEventListener("animationend", () => el.remove(), { once: true });
  };

  let raf = 0;
  const queue = () => raf || (raf = requestAnimationFrame(() => { raf = 0; sync(); }));

  const seen = new WeakSet();
  const watch = () => {
    document.querySelectorAll(".bottom-left-additional, .bottom-right-additional").forEach(el => {
      if (seen.has(el)) return;
      seen.add(el);
      new MutationObserver(queue).observe(el, { childList: true, subtree: true, attributes: true, attributeFilter: ["class", "style"] });
    });
    sync();
  };

  mount();
  watch();
  setTimeout(watch, 1000);
  new MutationObserver(mount).observe(document.head, { childList: true });
  document.addEventListener("click", mark, true);
})();
