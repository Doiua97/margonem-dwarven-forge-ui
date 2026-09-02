// ==UserScript==
// @name         Margonem Dwarven Forge UI
// @namespace    doiua97
// @version      1.0.2
// @description  Installs the complete Dwarven Forge dark fantasy UI theme for Margonem.
// @match        https://margonem.pl/*
// @match        https://*.margonem.pl/*
// @run-at       document-end
// @grant        none
// @updateURL    https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js
// @downloadURL  https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js
// ==/UserScript==

(() => {
  const id = "dwarven-forge-ui-theme";
  if (document.getElementById(id)) return;

  const primary = "https://fastly.jsdelivr.net/gh/Doiua97/margonem-dwarven-forge-ui@v1.0.2/css/dwarven-forge.css";
  const fallback = "https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/v1.0.2/css/dwarven-forge.css";
  const assetBase = "https://fastly.jsdelivr.net/gh/Doiua97/margonem-dwarven-forge-ui@v1.0.2/assets-production/";
  const style = document.createElement("style");
  style.id = id;

  const install = css => {
    style.textContent = css.replaceAll("../assets-production/", assetBase);
    const head = document.head || document.documentElement;
    head.appendChild(style);
    document.documentElement.dataset.dwarvenForgeVersion = "1.0.2";

    const observer = new MutationObserver(records => {
      const stylesheetAdded = records.some(record => [...record.addedNodes].some(node =>
        node !== style && node.nodeType === 1 &&
        (node.tagName === "STYLE" || (node.tagName === "LINK" && node.rel === "stylesheet"))
      ));
      if (stylesheetAdded && style.parentNode === head && style !== head.lastElementChild) head.appendChild(style);
    });
    observer.observe(head, { childList: true });
    console.info("[Dwarven Forge] UI theme 1.0.2 loaded");
  };

  fetch(primary, { cache: "no-cache" })
    .then(response => response.ok ? response.text() : Promise.reject(new Error(`CSS ${response.status}`)))
    .catch(() => fetch(fallback, { cache: "no-cache" }).then(response => response.ok ? response.text() : Promise.reject(new Error(`CSS ${response.status}`))))
    .then(install)
    .catch(error => console.error("[Dwarven Forge] Theme load failed", error));
})();
