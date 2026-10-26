import pandas as pd
import re
import os

REF_POS = "O produto possui excelente qualidade, chegou rapidamente e atendeu completamente às minhas expectativas. Gostei muito da compra e recomendo este produto para outras pessoas."
REF_NEG = "O produto possui péssima qualidade, apresentou problemas logo após a compra e não atendeu às minhas expectativas. Fiquei muito decepcionado e não recomendo este produto."

def preprocessar(texto):
    texto = str(texto).lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    return ' '.join(texto.split())

def jaccard(t1, t2):
    w1 = set(preprocessar(t1).split())
    w2 = set(preprocessar(t2).split())
    union = w1.union(w2)
    return len(w1.intersection(w2)) / len(union) if union else 0.0

def levenshtein(t1, t2):
    s1, s2 = preprocessar(t1), preprocessar(t2)
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)
            
    return dp[m][n]

def main():
    path = 'avaliacoes (1).xlsx' if os.path.exists('avaliacoes (1).xlsx') else 'avaliacoes.xlsx'
    df = pd.read_excel(path)
    
    res = []
    for _, row in df.iterrows():
        txt = row['avaliacao']
        j_pos, j_neg = jaccard(txt, REF_POS), jaccard(txt, REF_NEG)
        l_pos, l_neg = levenshtein(txt, REF_POS), levenshtein(txt, REF_NEG)
        
        res.append({
            'ID': row['ID'],
            'avaliacao': txt,
            'Jaccard Pos.': round(j_pos, 4),
            'Jaccard Neg.': round(j_neg, 4),
            'Class. Jaccard': 'POSITIVA' if j_pos > j_neg else 'NEGATIVA',
            'Lev. Pos.': l_pos,
            'Lev. Neg.': l_neg,
            'Class. Lev.': 'POSITIVA' if l_pos < l_neg else 'NEGATIVA'
        })
        
    df_out = pd.DataFrame(res)
    df_out.to_excel(os.path.abspath('resultado_classificacao.xlsx'), index=False)
    
    print(f"Total avaliações: {len(df_out)}")
    print(f"Jaccard Positivas: {(df_out['Class. Jaccard'] == 'POSITIVA').sum()}")
    print(f"Jaccard Negativas: {(df_out['Class. Jaccard'] == 'NEGATIVA').sum()}")
    print(f"Levenshtein Positivas: {(df_out['Class. Lev.'] == 'POSITIVA').sum()}")
    print(f"Levenshtein Negativas: {(df_out['Class. Lev.'] == 'NEGATIVA').sum()}")
    print(f"Concordantes: {(df_out['Class. Jaccard'] == df_out['Class. Lev.']).sum()}")
    print(f"Divergentes: {(df_out['Class. Jaccard'] != df_out['Class. Lev.']).sum()}")

if __name__ == '__main__':
    main()
