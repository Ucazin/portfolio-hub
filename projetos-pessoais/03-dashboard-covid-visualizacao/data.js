// Dataset fictício para fins de demonstração visual.
// Os números não representam dados reais.

const dados = {
  resumo: {
    total_casos:    14_582_310,
    obitos:           327_415,
    recuperados:   13_980_220,
    ativos:           274_675,
  },

  linha_temporal: {
    meses: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
            'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    casos: [120_000, 240_000, 480_000, 1_200_000, 2_100_000, 1_700_000,
            1_350_000, 1_080_000,   930_000,   780_000,   620_000,   500_000],
  },

  por_regiao: {
    regioes: ['Sudeste', 'Sul', 'Nordeste', 'Centro-Oeste', 'Norte'],
    casos:   [6_120_000, 2_780_000, 3_140_000, 1_240_000, 1_302_310],
  },

  distribuicao: {
    labels: ['Recuperados', 'Ativos', 'Óbitos'],
    valores: [13_980_220, 274_675, 327_415],
  },
};
