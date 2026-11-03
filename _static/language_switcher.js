/**
 * Conmutador de idioma dinámico ES / EU para Jupyter Book
 * Detecta si la ruta actual es /es/ o /eu/ y permite cambiar con un solo clic.
 */
document.addEventListener("DOMContentLoaded", function () {
  function initLanguageSwitcher() {
    const headerButtons = document.querySelector(".article-header-buttons");
    if (!headerButtons) return;

    // Evitar duplicar si ya existe
    if (document.querySelector(".lang-switcher-wrapper")) return;

    const currentPath = window.location.pathname;
    const isEuskera = currentPath.includes("/eu/") || currentPath.endsWith("/eu") || currentPath.endsWith("/eu/");
    const currentLang = isEuskera ? "eu" : "es";

    // Calcular URLs destino
    let esUrl, euUrl;
    if (isEuskera) {
      euUrl = window.location.href;
      esUrl = window.location.href.replace(/\/eu\b/, "/es");
    } else {
      esUrl = window.location.href;
      euUrl = window.location.href.replace(/\/es\b/, "/eu");
    }

    const wrapper = document.createElement("div");
    wrapper.className = "lang-switcher-wrapper btn-group";
    wrapper.setAttribute("role", "group");
    wrapper.setAttribute("aria-label", "Hizkuntza / Idioma");

    wrapper.innerHTML = `
      <a href="${esUrl}" class="btn btn-sm lang-btn ${currentLang === 'es' ? 'active' : ''}" title="Castellano">ES</a>
      <a href="${euUrl}" class="btn btn-sm lang-btn ${currentLang === 'eu' ? 'active' : ''}" title="Euskara">EU</a>
    `;

    // Insertar al inicio de la barra de botones del artículo
    headerButtons.prepend(wrapper);
  }

  initLanguageSwitcher();
});
