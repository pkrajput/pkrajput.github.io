(() => {
  const controls = document.querySelector('.publication-controls');
  const buttons = [...document.querySelectorAll('[data-filter]')];
  const papers = [...document.querySelectorAll('.publication')];
  const count = document.getElementById('publication-count');
  if (!controls || !count || !papers.length) return;
  controls.hidden = false;
  buttons.forEach(button => button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    let visible = 0;
    papers.forEach(paper => {
      paper.hidden = filter !== 'all' && paper.dataset.type !== filter;
      if (!paper.hidden) visible++;
    });
    count.textContent = `${visible} ${visible === 1 ? 'work' : 'works'}`;
  }));
})();
