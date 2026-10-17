/* Progressive enhancement: all navigation and downloads work without this file. */
for (const button of document.querySelectorAll('[data-copy]')) {
  button.addEventListener('click', async () => {
    const code = document.getElementById(button.dataset.copy);
    const feedback = button.closest('aside')?.querySelector('[role="status"]');
    if (!code || !feedback) return;
    try {
      await navigator.clipboard.writeText(code.textContent);
      feedback.textContent = 'Example JSON copied.';
      button.querySelector('span').textContent = 'Copied';
    } catch {
      feedback.textContent = 'Copy was unavailable. Select the example text to copy it, or download the file.';
    }
  });
}
