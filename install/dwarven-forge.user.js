// ==UserScript==
// @name         Margonem Dwarven Forge UI
// @namespace    doiua97
// @version      0.1.0
// @description  Loads the Dwarven Forge CSS-only UI theme for Margonem.
// @match        https://margonem.pl/*
// @match        https://*.margonem.pl/*
// @run-at       document-start
// @grant        none
// ==/UserScript==

(() => {
  const ID = 'dwarven-forge-ui-theme';
  if (document.getElementById(ID)) return;

  const link = document.createElement('link');
  link.id = ID;
  link.rel = 'stylesheet';
  link.href = 'https://cdn.jsdelivr.net/gh/Doiua97/margonem-dwarven-forge-ui@main/css/dwarven-forge.bundle.css?v=0.1.0';

  const mount = () => (document.head || document.documentElement).appendChild(link);
  mount();
})();
