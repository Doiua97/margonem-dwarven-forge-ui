// ==UserScript==
// @name         Margonem Dwarven Forge UI
// @namespace    doiua97
// @version      1.0.0
// @description  Installs the complete Dwarven Forge dark fantasy UI theme for Margonem.
// @match        https://margonem.pl/*
// @match        https://*.margonem.pl/*
// @run-at       document-start
// @grant        none
// @updateURL    https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js
// @downloadURL  https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js
// ==/UserScript==

(() => {
  const id = "dwarven-forge-ui-theme";
  if (document.getElementById(id)) return;

  const primary = "https://fastly.jsdelivr.net/gh/Doiua97/margonem-dwarven-forge-ui@v1.0.0/css/dwarven-forge.css";
  const fallback = "https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/v1.0.0/css/dwarven-forge.css";
  const link = document.createElement("link");
  link.id = id;
  link.rel = "stylesheet";
  link.href = primary;
  link.addEventListener("error", () => {
    if (link.href !== fallback) link.href = fallback;
  }, { once: true });
  (document.head || document.documentElement).appendChild(link);
})();
