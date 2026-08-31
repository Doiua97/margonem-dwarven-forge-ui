// ==UserScript==
// @name         Margonem Dwarven Forge UI
// @namespace    doiua97
// @version      0.7.1
// @description  Loads the Corner Forge black-and-red CSS-only UI theme.
// @match        https://margonem.pl/*
// @match        https://*.margonem.pl/*
// @run-at       document-end
// @grant        none
// @updateURL    https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js
// @downloadURL  https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js
// ==/UserScript==

(() => {
  const ID = "dwarven-forge-ui-theme";
  if (document.getElementById(ID)) return;

  const link = document.createElement("link");
  link.id = ID;
  link.rel = "stylesheet";
  link.href = "https://cdn.jsdelivr.net/gh/Doiua97/margonem-dwarven-forge-ui@v0.7.1/css/dwarven-forge.css";
  (document.head || document.documentElement).appendChild(link);
})();
