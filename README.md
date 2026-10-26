# Relatório Técnico: Classificação de Avaliações de Produtos

**Disciplina:** Processamento de Linguagem Natural / Inteligência Artificial  
**Instituição:** FATEC Registro  
**Aluno:** Lucas Gomes Fagundes

**Arquivo processado:** `avaliacoes (1).xlsx` (100 avaliações)  
**Arquivo gerado:** `resultado_classificacao.xlsx`  

---

## 1. Descrição da Atividade

O trabalho consiste em desenvolver um programa em Python para classificar 100 avaliações de clientes sobre um produto como **POSITIVA** ou **NEGATIVA**, utilizando duas métricas de similaridade e distância textual:
1. **Similaridade de Jaccard** (baseada em conjuntos de palavras).
2. **Distância de Levenshtein** (baseada em distância de edição de caracteres).

As avaliações foram comparadas com duas frases de referência:
* **Positiva:** *"O produto possui excelente qualidade, chegou rapidamente e atendeu completamente às minhas expectativas. Gostei muito da compra e recomendo este produto para outras pessoas."*
* **Negativa:** *"O produto possui péssima qualidade, apresentou problemas logo após a compra e não atendeu às minhas expectativas. Fiquei muito decepcionado e não recomendo este produto."*

---

## 2. Pré-processamento e Métricas

### Pré-processamento
Todos os textos passaram pelas etapas:
1. Conversão para minúsculas.
2. Remoção de pontuação (com `re.sub(r'[^\w\s]', '', texto)`).
3. Remoção de espaços extras.

### Métricas
- **Jaccard:** $J(A,B) = \frac{|A \cap B|}{|A \cup B|}$. Se $J_{pos} > J_{neg} \implies \text{POSITIVA}$, caso contrário $\text{NEGATIVA}$.
- **Levenshtein:** número mínimo de inserções, remoções e substituições de caracteres. Se $\text{Lev}_{pos} < \text{Lev}_{neg} \implies \text{POSITIVA}$, caso contrário $\text{NEGATIVA}$.

---

## 3. Respostas das Questões de Análise (Seção 9)

1. **Quantas avaliações foram classificadas como positivas por Jaccard?**  
   **29**
2. **Quantas avaliações foram classificadas como negativas por Jaccard?**  
   **71**
3. **Quantas avaliações foram classificadas como positivas por Levenshtein?**  
   **43**
4. **Quantas avaliações foram classificadas como negativas por Levenshtein?**  
   **57**
5. **Em quantas avaliações as duas métricas produziram a mesma classificação?**  
   **66**
6. **Em quantas avaliações as métricas produziram classificações diferentes?**  
   **34**
7. **Por que Jaccard e Levenshtein podem produzir resultados diferentes para uma mesma avaliação?**  
   O Jaccard compara apenas o conjunto de palavras únicas sem considerar a ordem das palavras ou o tamanho da frase. Se a avaliação usar sinônimos diferentes da referência, a intersecção fica baixa. Já o Levenshtein opera na sequência inteira de caracteres, considerando a ordem das letras e o tamanho total do texto.
8. **Qual das duas métricas apresentou maior sensibilidade às diferenças entre os textos? Justifique.**  
   A distância de **Levenshtein** apresentou maior sensibilidade. Por analisar o texto caractere por caractere, ela captura variações sutis na estrutura e tamanho das frases. O Jaccard mostrou-se mais rígido ao exigir palavras idênticas, classificando 71 avaliações como negativas por falta de sobreposição exata de vocabulário.

---

## 4. Arquivos Entregues

- `classificador_avaliacoes.py`: Código Python responsável pela leitura, processamento e cálculo das métricas.
- `resultado_classificacao.xlsx`: Planilha com os resultados de cada avaliação.
- `RELATORIO_FINAL_ESTUDO_DE_CASO.md`: Este relatório com as respostas.

