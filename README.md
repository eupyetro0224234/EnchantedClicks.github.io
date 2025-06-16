Para saber mais sobre, [clique aqui](https://eupyetro0224234.github.io/)

---

**Enchanted Clicks** é um jogo *clicker* simples feito em **Python** usando **Pygame**, onde o jogador ganha pontos clicando em um botão animado. O jogo possui sistema de upgrades e armazenamento local dos dados com criptografia simples.

---

## 🎮 Funcionalidades

- **Clique no botão animado:** O botão é um GIF animado que reproduz continuamente.
- **Animação de clique:** Ao clicar no botão, ele diminui sutilmente de tamanho para dar feedback visual.
- **Sistema de pontos:** Cada clique soma pontos à pontuação atual.
- **Clique com múltiplos botões:** Clique com botão esquerdo, direito ou meio do mouse, e a pontuação é atualizada corretamente.
- **Acúmulo de pontos ao usar a roda do mouse:** Girar a roda para cima aumenta os pontos.
- **Upgrades:** Possibilidade de comprar upgrades que aumentam o valor de pontos ganhos por clique.
- **Persistência dos dados:** Pontuação, upgrades e custo dos upgrades são salvos localmente com criptografia XOR simples.
- **Fundo colorido personalizado:** Fundo com quadrados coloridos alternando entre ciano, branco, verde claro e azul claro.
- **Interface simples e limpa:** Texto com pontuação e botão de upgrade, tudo dentro da janela do Pygame.

---

## 📁 Arquivos

- `main.py`: Arquivo principal que roda o jogo, trata eventos e atualiza a tela.
- `button.py`: Classe que controla a animação do botão e clique.
- `background.py`: Função para desenhar o fundo quadriculado colorido.
- `storage.py`: Funções para salvar e carregar dados criptografados localmente.
- `index.html`: Arquivo de teste simples com "Olá Mundo".

---

## 🚀 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/eupyetro0224234/EnchantedClicks.github.io

2. Instale o Pygame:
    ```bash
    pip install pygame