class SimuladorEmpresa:
    """Classe responsavel por gerenciar a saude financeira e projetar o

    crescimento anual de uma empresa com investimentos.
    """

    def __init__(
        self,
        investimento_inicial: float,
        faturamento_ano1: float,
        custos_fixos_ano1: float,
        custos_variaveis_pct: float,
        margem_perdas_pct: float,
        impostos_pct: float,
        capacidade_ociosa_pct: float,
        crescimento_anual_pct: float,
        taxa_rendimento_financeiro_pct: float,
    ) -> None:

        # Estados de Caixa (Valores Monetarios)
        self.caixa: float = investimento_inicial
        self.investimento_mercado: float = 0.0

        # Operacional e Custos
        self.faturamento: float = faturamento_ano1
        self.custos_fixos: float = custos_fixos_ano1
        self.custos_variaveis_pct: float = custos_variaveis_pct / 100

        # Eficiência, Governo e Macroeconomia (Convertidos para Decimais)
        self.margem_perdas_pct: float = margem_perdas_pct / 100
        self.impostos_pct: float = impostos_pct / 100
        self.capacidade_ociosa_pct: float = capacidade_ociosa_pct / 100
        self.crescimento_anual_pct: float = crescimento_anual_pct / 100
        self.taxa_rendimento_pct: float = (
            taxa_rendimento_financeiro_pct / 100
        )

    def alocar_no_mercado(self, porcentagem_do_caixa: float) -> None:
        """Move uma porcentagem do caixa livre para investimentos em renda

        fixa.
        """
        if not 0 <= porcentagem_do_caixa <= 100:
            print("Erro: A porcentagem de alocacao deve estar entre 0 e 100.")
            return

        valor_alocar: float = self.caixa * (porcentagem_do_caixa / 100)
        self.caixa -= valor_alocar
        self.investimento_mercado += valor_alocar
        print(f"Sucesso: R$ {valor_alocar:,.2f} alocados no mercado financeiro.")

    def simular_ano(self, numero_ano: int) -> None:
        """Executa a simulação financeira de um ano operacional, atualizando o

        caixa e projetando o próximo ciclo.
        """
        print(f"\n{'='*20} PROJEÇÃO: ANO {numero_ano} {'='*20}")

        # 1. Ajuste de Ociosidade Comercial
        faturamento_potencial: float = self.faturamento
        vendas_perdidas_ociosidade: float = (
            faturamento_potencial * self.capacidade_ociosa_pct
        )
        faturamento_real: float = (
            faturamento_potencial - vendas_perdidas_ociosidade
        )

        # 2. Custos Operacionais e Deduções
        custos_variaveis: float = faturamento_real * self.custos_variaveis_pct
        perdas_produtos: float = faturamento_real * self.margem_perdas_pct
        impostos: float = faturamento_real * self.impostos_pct

        custo_total_operacional: float = (
            self.custos_fixos + custos_variaveis + perdas_produtos + impostos
        )
        lucro_operacional: float = faturamento_real - custo_total_operacional

        # 3. Dinâmica Financeira (Rendimentos)
        rendimento: float = self.investimento_mercado * self.taxa_rendimento_pct
        self.investimento_mercado += rendimento

        # 4. Atualização do Caixa
        self.caixa += lucro_operacional

        # Exibição do Relatório Formatado
        self._exibir_relatorio(
            faturamento_potencial,
            vendas_perdidas_ociosidade,
            faturamento_real,
            impostos,
            perdas_produtos,
            custos_variaveis,
            lucro_operacional,
            rendimento,
        )

        # 5. Evolução Composta para o Próximo Período
        self.faturamento *= 1 + self.crescimento_anual_pct
        self.custos_fixos *= 1 + (
            self.crescimento_anual_pct * 0.5
        )  # Custos fixos escalam mais devagar

    def _exibir_relatorio(
        self,
        fat_potencial: float,
        perda_ociosa: float,
        fat_real: float,
        impostos: float,
        perdas_prod: float,
        c_var: float,
        lucro_op: float,
        rendimento: float,
    ) -> None:
        """Método interno auxiliar para organizar o print dos resultados."""
        print(f"Faturamento Potencial:         R$ {fat_potencial:,.2f}")
        print(f"(-) Perda por Ociosidade:      R$ {perda_ociosa:,.2f}")
        print(f"(=) Faturamento Real:           R$ {fat_real:,.2f}")
        print(f"--------------------------------------------------")
        print(f"(-) Impostos Diretos:          R$ {impostos:,.2f}")
        print(f"(-) Perda Física de Produtos:  R$ {perdas_prod:,.2f}")
        print(f"(-) Custos Fixos Ouro:         R$ {self.custos_fixos:,.2f}")
        print(f"(-) Custos Variáveis:          R$ {c_var:,.2f}")
        print(f"(=) Lucro Líquido Operacional: R$ {lucro_op:,.2f}")
        print(f"--------------------------------------------------")
        print(f"(+) Rendimento do Mercado:     R$ {rendimento:,.2f}")
        print(f"--> Saldo em Caixa Livre:      R$ {self.caixa:,.2f}")
        print(f"--> Saldo Investido (Ativos):  R$ {self.investimento_mercado:,.2f}")
        print(f"--> VALOR PATRIMONIAL TOTAL:   R$ {(self.caixa + self.investimento_mercado):,.2f}")
        print(f"{'='*52}\n")


# --- INICIALIZAÇÃO DA SIMULAÇÃO ---
if __name__ == "__main__":
    empresa = SimuladorEmpresa(
        investimento_inicial=50000.00,
        faturamento_ano1=200000.00,
        custos_fixos_ano1=48000.00,
        custos_variaveis_pct=25.0,
        margem_perdas_pct=3.0,
        impostos_pct=6.0,
        capacidade_ociosa_pct=15.0,
        crescimento_anual_pct=10.0,
        taxa_rendimento_financeiro_pct=10.75,
    )

    # Execução Estratégica
    empresa.alocar_no_mercado(porcentagem_do_caixa=40.0)

    for ano in range(1, 4):
        empresa.simular_ano(ano)