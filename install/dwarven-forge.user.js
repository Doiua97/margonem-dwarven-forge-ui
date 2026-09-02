// ==UserScript==
// @name         Margonem Dwarven Forge UI
// @namespace    doiua97
// @version      1.0.20
// @description  Installs the complete Dwarven Forge dark fantasy UI theme for Margonem.
// @match        https://margonem.pl/*
// @match        https://*.margonem.pl/*
// @run-at       document-end
// @grant        none
// @updateURL    https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js
// @downloadURL  https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js
// ==/UserScript==

(() => {
  const base = "https://fastly.jsdelivr.net/gh/Doiua97/margonem-dwarven-forge-ui@v1.0.20";
  const link = document.createElement("link");
  link.id = "dwarven-forge-ui-theme";
  link.rel = "stylesheet";
  link.href = base + "/css/dwarven-forge.css";

  const mount = () => {
    if (link !== document.head.lastElementChild) document.head.appendChild(link);
  };

  const swap = (n = 120) => {
    const img = window.Engine?.imgLoader?.checkExist("/img/cross.gif", false);
    if (!img?.complete || !img.naturalWidth) {
      if (n > 1) setTimeout(swap, 500, n - 1);
      return;
    }
    const next = new Image();
    next.crossOrigin = "anonymous";
    next.onload = () => {
      const { src, crossOrigin } = img;
      img.addEventListener("error", () => Object.assign(img, { crossOrigin, src }), { once: true });
      Object.assign(img, { crossOrigin: "anonymous", src: next.src });
    };
    next.src = base + "/assets-production/lupus.margonem.pl/img/gui/dwarven-forge/v113/map-cross.svg";
  };

  mount();
  swap();
  new MutationObserver(mount).observe(document.head, { childList: true });
})();
