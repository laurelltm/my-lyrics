(() => {
  const button = document.querySelector('#start-demo');
  const frame = document.querySelector('#app-demo-frame');
  const stage = document.querySelector('.demo-stage');
  const live = document.querySelector('#live-demo');
  const feedback = document.querySelector('#demo-feedback');
  if (!button || !frame || !stage || !live || !feedback) return;
  let started = false;
  button.addEventListener('click', () => {
    if (started) return;
    started = true;
    stage.dataset.started = 'true';
    live.hidden = false;
    feedback.textContent = 'Opening My Lyrics…';
    const timeout = window.setTimeout(() => {
      feedback.replaceChildren(document.createTextNode('Taking longer than expected? '));
      const link = document.createElement('a');
      link.href = frame.dataset.src;
      link.textContent = 'Open the app full screen.';
      feedback.append(link);
    }, 15000);
    frame.addEventListener('load', () => {
      window.clearTimeout(timeout);
      feedback.textContent = 'Your library is saved in this browser.';
    }, { once: true });
    frame.addEventListener('error', () => {
      window.clearTimeout(timeout);
      feedback.textContent = 'The embedded app could not open. Try the full-screen link above.';
    }, { once: true });
    frame.src = frame.dataset.src;
    frame.focus();
  });
})();
