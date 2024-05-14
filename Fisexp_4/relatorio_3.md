# Relatório 3 - Metrologia Ótica - Fisexp IV - Anexo

## Nomes
- Carlos Pereira
- Carolina Silva
- Letícia Alves

## Questão 1

- Consideramos a incerteza de $\sigma \Delta x_{\text{par}} = 10 \mu m$, pois era a escala indicada no parafuso de deslocamento do equipamento.
- Para encontrar $\Delta x_{\text{esp}}$, utilizamos:
  $$
  \Delta x_{\text{esp}} = \frac{\Delta x_{\text{par}}}{20}$$

- Já a incertez $\sigma \Delta x_{\text{esp}}$ foi calculada por meio da propagação da incerteza:
  
  $$
  \begin{align}
    \sigma \Delta x_{\text{esp}}^2 &= \left( \frac{\partial x}{\partial} \left( \frac{\Delta x_{\text{par}}}{20} \right) \right)^2 \cdot (\sigma \Delta x_{\text{par}})^2 \\
    &= \left( \frac{1}{20} \frac{\partial x}{\partial} (\Delta x_{\text{par}}) \right)^2 \cdot (\sigma \Delta x_{\text{par}})^2 \\
    &= \left( \frac{1}{20} \cdot 10 \right)^2 \cdot (10 \mu m)^2 \\
    \sigma \Delta x_{\text{esp}} &= \sqrt{\left( \frac{10}{20} \right)^2 \cdot (10 \mu m)^2} \\
    &= 0,5 \mu m   
  \end{align}$$

## Questão 2

- Os valores de $P$ (pressão dentro da cuba) foram calculados a partir da simulação com a bomba de vácuo
- Consideramos que a pressão no interior da cuba é igual a pressão atmosférica ($760 \text{mmHg}$) menos a pressão na bomba de vácuo
  $$P_1 = 760 \text{mmHg} - 100 \text{mmHg} = 660 \text{mmHg} $$
- Fizemos o procedimento de aumentar a pressão dentro da cuba para as 8 pressões simuladas
- Já a incerteza da medida $P$ ($\sigma P$), consideramos como a escala indicada na bomba de vácuo, logo $\sigma P = 10 \text{mmHg}$
- Seguindo o roteito, $\Delta P = P_{\text{cuba}} - P_{\text[atm]}$

## Questão 3

- Para calcular o comprimento de onda do laser ($\lambda$), utilizamos a relação $\Delta x_{\text{esp}} = \frac{N \lambda}{2}$
- Considrando que temos uma representação linear, podemos calcular o coeficiente da reta como $\frac{\Delta y}{\Delta x}$
  $$
  \begin{align}
    y &= ax + b \\
    \Delta x_{\text{esp}} &=y, \ N = x \\
    \frac{\Delta x_{\text{esp}}}{\Delta N} &= \frac{\lambda}{2} \\
    \lambda &= \frac{12 - 3}{40 -10} \cdot 2 = \frac{18}{30} \\
    &= 0,6 \mu m = 600 \ nm 
  \end{align}$$

- O cálculo da discrepância relativa foi feito como:
  $$
  \begin{align}
    D_R &= \frac{|\lambda_{\text{medido}} - \lambda_{\text{ref}}|}{\lambda_{\text{ref}}} \\
    &= \frac{|600 - 632,8|}{632,8} \\
    &= 0,052 = 5,2\%
  \end{align}$$

## Questão 4

- Para calcular o coeficiente angular, utilizamos a relação:
  $$
  \frac{\Delta N}{\Delta P} = \frac{19 - 8}{(360 -10) - 610} = -0,035$$

- Consideramos o ponto $(360 - 10)$ pois a reta passa pela barra de erro do ponto
- Não é possível obter para o índice do ar um valor $n < 1$, pois dada a relação $n(p) = 1 + \alpha p$, onde $\alpha = \frac{\Delta n}{\Delta p}$ é sempre um valor positivo, ou seja, $n(p)$ é sempre maior que 1
- O sinal esperado para $\frac{\Delta N}{\Delta p}$ é negativo, uma vez que estamos constantemente diminuindo a pressão dentro da cuba, e consequentemente o índice de refração do ar
- Podemos verificar essa consistência através do gráfico $N \ x \ P$, onde obtivemos uma reta decrescente com o coeficiente angular positivo

## Questão 5

- Para calcularmos o índice de refração do ar:
  $$
  \begin{align}
    \alpha &= \frac{- \lambda_0}{2l} \frac{\Delta N}{\Delta P}, \ l = 55 \text{mm}, \ \lambda_0 = 632,8 \text{nm} \\
    &= \frac{-632,8 \cdot 10^{-9}}{2 \cdot 55 \cdot 10^{-3}} \cdot (-0,035) \\
    &= 0,20 \cdot 10^{-6} \text{mm Hg}^{-1}
  \end{align}$$ 

- Com isso, podemos calcular o índice de refração do ar ($n_{\text{exp}}$) pela relação:
  $$
  \begin{align}
    n_{\text{exp}} &= 1 + \alpha p, \ p= 760 \text{mmHg} \\
    &= 1 + (0,20 \cdot 10^{6} \cdot 760 \text{mmHg}) \\
    &= 1,53 \cdot 10^{-4}
  \end{align}
  $$

- O erro relativo é:
  $$
  \begin{align}
    \frac{|2,9 - 1,53|}{2,9} = 0,47 = 47\%
  \end{align}$$

- A incerteza de $n_\text{exp}$ foi considerada como 5% do valor
- A discrepância é dada por:
  $$
  \begin{align}
    D &= |(n_{\text{atm}} - 1) - (n_{\text{exp}} -1)| \\
    &= |2,9 - 1,53| = 1,37
  \end{align}$$

- Considerando que para as medidas serem compatíveis, a discrepância deve ter valor até $3 \sigma$, nosso cálculo mostra que os valores são incompatíveis:
  $$
  \begin{align}
    D &= 1.37 > 3\sigma \\
    &= 1,37 > 0,24
  \end{align}$$