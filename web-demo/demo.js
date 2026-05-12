(function () {
  const frame = document.querySelector(".phone-frame");
  const iframe = document.querySelector("#app-demo-frame");
  const loading = document.querySelector("#iframe-loading");
  const openDemoLink = document.querySelector("#open-demo-link");
  const demoUrl = new URL("app/?demo=true", window.location.href).toString();
  let lockedScrollY = 0;
  let isPageScrollLocked = false;

  if (openDemoLink) {
    openDemoLink.setAttribute("href", demoUrl);
  }

  if (!frame || !iframe || !loading) {
    return;
  }

  function lockPageScroll() {
    if (isPageScrollLocked) {
      return;
    }

    lockedScrollY = window.scrollY;
    document.documentElement.style.setProperty(
      "--locked-scroll-y",
      `-${lockedScrollY}px`,
    );
    document.body.classList.add("phone-scroll-locked");
    isPageScrollLocked = true;
  }

  function unlockPageScroll() {
    if (!isPageScrollLocked) {
      return;
    }

    document.body.classList.remove("phone-scroll-locked");
    document.documentElement.style.removeProperty("--locked-scroll-y");
    window.scrollTo(0, lockedScrollY);
    isPageScrollLocked = false;
  }

  let finished = false;

  function setLoaded() {
    finished = true;
    frame.dataset.frameState = "loaded";
    loading.textContent = "Open Songbook demo loaded";
  }

  function setFallback() {
    if (finished) {
      return;
    }

    frame.dataset.frameState = "fallback";
    loading.innerHTML =
      `The embedded app is still loading. <a href="${demoUrl}">Open the demo full screen</a>.`;
  }

  iframe.addEventListener("load", setLoaded, { once: true });
  frame.addEventListener("pointerenter", lockPageScroll);
  frame.addEventListener("pointerleave", unlockPageScroll);
  frame.addEventListener("focusin", lockPageScroll);
  frame.addEventListener("focusout", unlockPageScroll);
  window.addEventListener("pagehide", unlockPageScroll);
  window.setTimeout(setFallback, 10000);
})();
