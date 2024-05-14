# Equações

## Elementos de física quântica e estatística

**Relação de de Broglie:**

$$
p = \frac{h}{\lambda} $$

- $p$: momento linear de uma partícula, agora onda 
- $h$: constante de Planck
- $\lambda$: comprimento de onda

**Relação de Planck:**

$$
\begin{align}
    E &= h \nu \\
    E_c & = h \nu - \phi; \ h \nu \geq \phi\\
\end{align} $$

- $\nu$: frequência da "partícula"
- $\phi$: função trablho; energia mínima necessária para extrair elétrons do metal
- Ao relacionar a energia cinética (em $eV$) com a frequência de radiação eletromagnética, o coeficiente linear será a função trabalho, enquanto o coeficiente angular será a medida da constante de Planck

**Propriedades ondulatórias (Planck e de Broglie):**

$$
\begin{align}
    \hbar &= \frac{h}{2 \pi} = 1,05 \cdot 10^{-34} J \cdot s \\
    K &= \frac{2\pi}{\lambda} \\
    p &= \frac{h}{\lambda} = \hbar K \\
    \omega &= 2 \pi \nu \\
    E &= h \nu = \hbar \omega
\end{align} 
$$

- Relação de dispersão: descreve como a energia de uma partícula ou onda se relaciona com o seu momento (número de onda), relacionando a energia, momento e outras propriedades da onda ou partícula; relação entre as frequências e comprimento de onda (ou velocidade) de uma onda

$$
\begin{align}
   \hbar &= \frac{K}{p} = \frac{E}{\omega} = \frac{h}{2 \pi} \\
   h &= \frac{p}{\lambda} = \frac{E}{\nu}
\end{align}$$

**Modelo atômico de Bohr:**

$$
\begin{align}
    r_n &= \frac{h^2 \epsilon_0}{\pi m_e Z e^2} n^2 = \frac{a_0}{Z} n^2; \ n=1,2,3, \cdots \\
    E_n &= - \left( \frac{m_e Z^2 e^4}{8 h^2 \epsilon_0^2} \right) \frac{1}{n^2} = \frac{- E_0 Z^2}{n^2}; \ n = 1,2,3,\cdots \\
\end{align}$$

- $a_0 = 0,53 \mathring{A}$: raio de Bohr
- $E_0 = 13,6 \ eV$: energia de ligação do estado fundamental do átomo de hidrogênio

**Equação de Schrodinger:**

$$- \frac{\hbar^2}{2m} \nabla^2 \Psi + V \Psi = i \hbar \frac{\partial \Psi}{\partial t} $$

- $\Psi$: função de onda associada à partícula
- Separa-se a parte temporal da parte espacial
- Utiliza-se a relação de Planck para obter-se a equação de Schrodinger independente do tempo

$$
\begin{align}
    \Psi \vec{(r, t)} &= \Psi \vec{(r)} \cdot \exp (-i \omega t) \\
    - \frac{\hbar^2}{2m} \nabla^2 \Psi + V \Psi &= E \Psi
\end{align}$$

**Função densidade de probabilidade:**

$$
\begin{align}
    |\Psi|^2 &= \Psi \cdot \Psi^{*} \\
    \int |\Psi|^2 d \tau &= 1
\end{align}$$

- Postulado: o módulo ao quadrado da função de onda é proporcional à função densidade de probabilidade associada à partícula
- Normaliza-se (integral = 1) a função de onda a partir da função densidade de probabilidade em uma certa região do espaço

**Problema da partícula livre:**

- Uma partícula livre está livre de qualquer interação, logo a parte potencial é nula
- Utiliza-se a relação de De Broglie para obter a relação de dispersão da partícula livre em função da energia cinética

$$
\begin{align}
    V &= 0 \Rightarrow \\ 
    - \frac{\hbar^2}{2m} \frac{d^2 \Psi}{dx^2} &= E \Psi \\
    \frac{d^2 \Psi}{dx} &= \frac{2 m E}{\hbar^2} \Psi \\
    \Psi (x,t) &= A \exp [-i (k x + \omega t)] \\
    \Psi (x) &= A \exp (-i k x) \\
    - A k^2 \exp (-ikx) &= - \frac{2 m E}{\hbar^2} A \exp (-i k x) \\
    k^2 &= \frac{2 m E}{\hbar^2} \\
    E &= \frac{\hbar^2 k^2}{2m} \\
    \lambda = \frac{h}{p} &\Rightarrow p = \frac{h}{\lambda} \\
    k = \frac{2 \pi}{\lambda} &\Rightarrow p = \hbar k \\
    E &= \frac{p^2}{2m}
\end{align}$$

**O poço de potencial infinito**

$$
V = 
\begin{cases}
    0; \ 0 < x < L \\
    \infty; \ x < 0, x > L
\end{cases}$$

- Fora do poço:

$$
\begin{align}
    V &= \infty \\
    - \frac{\hbar^2}{2m} \frac{d^2 \Psi}{dx^2} + V \Psi &= E \Psi \\
    \Psi &= 0
\end{align}$$

- Dentro do poço:

$$
\begin{align}
    V = 0\\
    - \frac{\hbar^2}{2m} \frac{d^2 \Psi}{dx^2} &= E \Psi \\
    \Psi (x) &= A \sin (kx) + B \cos (kx) \\
    - \frac{\hbar^2}{2m} [- A k^2 \sin (kx) - B k^2 \cos (kx)] &= E \Psi \\
    + \frac{h^2 k^2}{2m} [A \sin (kx) + B \cos (kx)] &= E \Psi \\
    E &= \frac{\hbar^2 k^2}{2m}
\end{align}$$

- Condições de contorno:

$$
\Psi (x)
\begin{cases}
    = 0, \ x=0 \\
    = 0, \ x=L
\end{cases}
$$

$$
\begin{align}
    \Psi(0) &= A \sin 0 + B \cos 0 \Rightarrow B = 0 \\
    \Psi (L) &= A \sin k L = 0 \\
    \sin k L &= 0 \\
    k L &= n \pi \\
    k_n &= n \frac{\pi}{L}, \ n = 1,2,3, \cdots, \infty 
\end{align}$$

$$
\begin{align}
    p &= \frac{h}{\lambda} \\
    \lambda &= \frac{2 \pi}{k} \\
    E &\propto k^2 \\
    E_n &= \frac{\hbar^2 \pi^2}{2 m L^2} n^2 \ \text{(Quantização da energia)} \\
    \Psi (x) &= A \sin \left( \frac{n \pi}{L} x \right) \\
    |\Psi (x)|^2 &= A^2 \sin^2 \left( \frac{n \pi}{L} x \right)  
\end{align}$$

- No mundo microscópico, $m$ e/ou $L$ são muito pequenos
- No mundo macroscópico, $n$ é absurdamente grande, ou seja, desaparecem os fenômenos de quantização, coincidindo com a física clássica

## Energia de coesão e propriedades elásticas

**Tensão:**

$$
\sigma = \frac{T}{A_0} $$

**Deformação:**

$$
\epsilon = \frac{\Delta L}{L_0} = \frac{L - L_0}{L_0}  $$

- No regime elástico, as deformações são reversíveis e ocorrem somente para deformações pequenas



## Fônons e propriedades térmicas



$$
\begin{align}
    \\
    \\
\end{align}$$
