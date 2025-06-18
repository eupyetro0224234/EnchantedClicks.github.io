/* ----------- bloqueio de duplo-toque-zoom ----------- */
let lastTouch = 0;
document.addEventListener(
  'touchend',
  e => {
    const now = Date.now();
    if (now - lastTouch <= 300) e.preventDefault();
    lastTouch = now;
  },
  { passive: false }
);

/* ------------------- clicker ------------------- */
const scoreEl = document.getElementById('score');
const btn     = document.getElementById('click-btn');

let localScore = 0;
let pending    = 0;          // cliques aguardando envio

async function pull() {
  const r = await fetch('/api/score');
  localScore = (await r.json()).score;
  scoreEl.textContent = localScore;
}

/* capturar cliques MUITO rápido */
btn.addEventListener('pointerdown', () => {
  pending     += 1;
  localScore  += 1;
  scoreEl.textContent = localScore;
});

/* a cada 100 ms, manda o pacote acumulado */
setInterval(() => {
  if (pending === 0) return;

  const delta = pending;
  pending = 0;

  fetch('/api/click', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ delta })
  })
    .then(r => r.json())
    .then(data => {
      // sincroniza caso outro dispositivo também esteja clicando
      localScore = data.score;
      scoreEl.textContent = localScore;
    })
    .catch(() => {
      // se falhar, devolve ao buffer para tentar depois
      pending += delta;
    });
}, 100);

pull();