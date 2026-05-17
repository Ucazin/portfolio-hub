// Lucca Mariz · Dashboard COVID interativo
// Renderiza gráficos com Chart.js a partir de dados fictícios em data.js

const cores = {
  texto:      '#e6e9ef',
  grade:      '#252b3a',
  accent:     '#6c8cff',
  accent2:    '#22d3ee',
  success:    '#4ade80',
  warning:    '#fbbf24',
  danger:     '#f87171',
};

const fmt = new Intl.NumberFormat('pt-BR');

function preencherKPIs() {
  document.getElementById('kpi-casos').textContent       = fmt.format(dados.resumo.total_casos);
  document.getElementById('kpi-obitos').textContent      = fmt.format(dados.resumo.obitos);
  document.getElementById('kpi-recuperados').textContent = fmt.format(dados.resumo.recuperados);
  document.getElementById('kpi-ativos').textContent      = fmt.format(dados.resumo.ativos);
}

function configuracaoBase() {
  return {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { labels: { color: cores.texto } },
      tooltip: {
        backgroundColor: '#0b0d12',
        borderColor: cores.grade,
        borderWidth: 1,
        titleColor: cores.texto,
        bodyColor: cores.texto,
        callbacks: {
          label: (ctx) => `${ctx.dataset.label || ctx.label}: ${fmt.format(ctx.parsed.y ?? ctx.parsed)}`,
        },
      },
    },
    scales: {
      x: { ticks: { color: cores.texto }, grid: { color: cores.grade } },
      y: { ticks: { color: cores.texto }, grid: { color: cores.grade } },
    },
  };
}

function renderLinha() {
  const ctx = document.getElementById('grafico-linha').getContext('2d');
  const gradient = ctx.createLinearGradient(0, 0, 0, 300);
  gradient.addColorStop(0, 'rgba(108, 140, 255, 0.4)');
  gradient.addColorStop(1, 'rgba(108, 140, 255, 0)');

  new Chart(ctx, {
    type: 'line',
    data: {
      labels: dados.linha_temporal.meses,
      datasets: [{
        label: 'Casos',
        data: dados.linha_temporal.casos,
        borderColor: cores.accent,
        backgroundColor: gradient,
        fill: true,
        tension: 0.35,
        pointBackgroundColor: cores.accent,
        pointBorderColor: '#0b0d12',
        pointRadius: 4,
      }],
    },
    options: configuracaoBase(),
  });
}

function renderBarras() {
  const ctx = document.getElementById('grafico-barras').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: dados.por_regiao.regioes,
      datasets: [{
        label: 'Casos',
        data: dados.por_regiao.casos,
        backgroundColor: cores.accent2,
        borderRadius: 6,
      }],
    },
    options: configuracaoBase(),
  });
}

function renderDoughnut() {
  const ctx = document.getElementById('grafico-doughnut').getContext('2d');
  const cfg = configuracaoBase();
  delete cfg.scales;
  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: dados.distribuicao.labels,
      datasets: [{
        data: dados.distribuicao.valores,
        backgroundColor: [cores.success, cores.warning, cores.danger],
        borderColor: '#0b0d12',
        borderWidth: 2,
      }],
    },
    options: { ...cfg, cutout: '60%' },
  });
}

document.addEventListener('DOMContentLoaded', () => {
  preencherKPIs();
  renderLinha();
  renderBarras();
  renderDoughnut();
});
