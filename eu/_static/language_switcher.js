/**
 * Conmutador de idioma dinámico ES / EU para Jupyter Book
 * Inserta el selector en dos lugares para máxima visibilidad:
 * 1. En la barra lateral (debajo del título/logo del libro)
 * 2. En la barra superior de herramientas (.article-header-buttons)
 */

(function () {
  function getUrls() {
    const href = window.location.href;
    const isEuskera = href.includes("/eu/") || href.endsWith("/eu") || href.endsWith("/eu/");
    const currentLang = isEuskera ? "eu" : "es";

    let esUrl, euUrl;
    if (isEuskera) {
      euUrl = href;
      esUrl = href.replace(/\/eu(\/|$)/, "/es$1");
    } else {
      esUrl = href;
      euUrl = href.replace(/\/es(\/|$)/, "/eu$1");
    }

    return { esUrl, euUrl, currentLang, isEuskera };
  }

  function insertHeaderSwitcher(urls) {
    const headerButtons = document.querySelector(".article-header-buttons");
    if (!headerButtons) return false;
    if (document.querySelector(".header-lang-switcher")) return true;

    const wrapper = document.createElement("div");
    wrapper.className = "header-lang-switcher btn-group";
    wrapper.setAttribute("role", "group");
    wrapper.setAttribute("aria-label", "Hizkuntza / Idioma");

    wrapper.innerHTML = `
      <a href="${urls.esUrl}" class="btn btn-sm lang-btn ${urls.currentLang === 'es' ? 'active' : ''}" title="Castellano">ES</a>
      <a href="${urls.euUrl}" class="btn btn-sm lang-btn ${urls.currentLang === 'eu' ? 'active' : ''}" title="Euskara">EU</a>
    `;

    headerButtons.prepend(wrapper);
    return true;
  }

  function insertSidebarSwitcher(urls) {
    const logoBrand = document.querySelector(".navbar-brand.logo");
    if (!logoBrand) return false;
    if (document.querySelector(".sidebar-lang-switcher")) return true;

    const wrapper = document.createElement("div");
    wrapper.className = "sidebar-lang-switcher";
    wrapper.innerHTML = `
      <div class="sidebar-lang-group" role="group" aria-label="Hizkuntza aukeratu">
        <a href="${urls.esUrl}" class="sidebar-lang-btn ${urls.currentLang === 'es' ? 'active' : ''}">ES · Castellano</a>
        <a href="${urls.euUrl}" class="sidebar-lang-btn ${urls.currentLang === 'eu' ? 'active' : ''}">EU · Euskara</a>
      </div>
    `;

    logoBrand.parentNode.insertBefore(wrapper, logoBrand.nextSibling);
    return true;
  }

  function init() {
    const urls = getUrls();
    insertHeaderSwitcher(urls);
    insertSidebarSwitcher(urls);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  // Fallback por si el tema hidrata elementos tras el DOMContentLoaded
  setTimeout(init, 300);
  setTimeout(init, 1000);
})();
