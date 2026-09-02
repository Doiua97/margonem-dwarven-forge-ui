// ==UserScript==
// @name         Margonem Dwarven Forge UI
// @namespace    doiua97
// @version      1.0.13
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
  link.href = "https://fastly.jsdelivr.net/gh/Doiua97/margonem-dwarven-forge-ui@v1.0.13/css/dwarven-forge.css";

  const mount = () => {
    if (link !== document.head.lastElementChild) document.head.appendChild(link);
  };

  // MapGoMark keeps this cached image; only its pixels change.
  const url = "https://fastly.jsdelivr.net/gh/Doiua97/margonem-dwarven-forge-ui@v1.0.13/assets-production/lupus.margonem.pl/img/gui/dwarven-forge/v113/map-cross.svg";
  let tries = 0;
  const swap = () => {
    const img = window.Engine?.imgLoader?.checkExist("/img/cross.gif", false);
    if (!img?.complete || !img.naturalWidth) {
      if (++tries < 120) setTimeout(swap, 500);
      return;
    }
    const next = new Image();
    next.crossOrigin = "anonymous";
    next.onload = () => {
      const src = img.src, cors = img.crossOrigin;
      img.addEventListener("error", () => { img.crossOrigin = cors; img.src = src; }, { once: true });
      img.crossOrigin = "anonymous";
      img.src = url;
    };
    next.src = url;
  };

  mount();
  swap();
  new MutationObserver(mount).observe(document.head, { childList: true });
})();
