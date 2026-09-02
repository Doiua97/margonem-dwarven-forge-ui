// ==UserScript==
// @name         Margonem Dwarven Forge UI
// @namespace    doiua97
// @version      1.0.9
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
  link.href = "https://fastly.jsdelivr.net/gh/Doiua97/margonem-dwarven-forge-ui@v1.0.9/css/dwarven-forge.css";

  const mount = () => {
    if (link !== document.head.lastElementChild) document.head.appendChild(link);
  };

  mount();
  new MutationObserver(mount).observe(document.head, { childList: true });
})();
