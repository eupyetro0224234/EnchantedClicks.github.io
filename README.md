# EnchantedClicks.github.io

# ✨ Enchanted Clicks

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
<details> <summary>📌 Clique aqui para ver mais detalhes (exemplo oculto)</summary>
Aqui você pode colocar conteúdo extra, instruções avançadas, notas de desenvolvimento, imagens ou blocos de código:

python
Copiar
Editar
print("Exemplo de código dentro da seção oculta")
</details>
<details> <summary>🕒 Commits / Registros de alteração</summary>
✅ Initial commit: 16/06/2025 - 15h11
1 arquivo adicionado

README.md

✅ Segundo commit: 16/06/2025 - 15h14
Arquivo: README.md

Linhas: +30 / -1

Descrição:

Estruturação inicial com funcionalidades, arquivos e instruções.

✅ Terceiro commit: 16/06/2025 - 15h25
Total: 8 arquivos adicionados

Linhas: +212 / -0

📁 Arquivos binários:
jogo/__pycache__/background.cpython-313.pyc (852 bytes)

jogo/__pycache__/button.cpython-313.pyc (4.88 KB)

jogo/__pycache__/storage.cpython-313.pyc (2.71 KB)

📄 Arquivos de código:
jogo/background.py: +14 linhas

jogo/button.py: +82 linhas

jogo/main.py: +76 linhas

jogo/storage.py: +39 linhas

index.html: +1 linha

✅ Quarto commit: 16/06/2025 - 15h28
Arquivo modificado: README.md

Linhas: +20 / -2

Descrição:

Inclusão da seção com conteúdo oculto.

Ajustes de texto em instruções.

Primeira tentativa de registro manual de alterações.