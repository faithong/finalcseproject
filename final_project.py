import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


col1, col2, col3 = st.columns([3, 1, 1])


with col1:
    st.title("CSE 163 Final Project")
    st.caption("There are social and economic factors that influence the rate of lung cancer in different communities. However, despite racial disparities in lung cancer, genomic level analysis of lung cancer in underserved patients of African descent remains underexplored.")

# displaying data
aa = pd.read_csv('data_aa.csv')
ea = pd.read_csv('data_ea.csv')
aa['Race'] = "African-American"
ea['Race'] = "European-American"
all_races = aa.merge(ea, how='outer')
all_races = all_races.loc[:, all_races.columns != 'gene_id']

visualization = st.selectbox(
     "",
     ('About the Dataset',
      'How Does the Average APA Site in African Americans Compare to that of European Americans?',
      'How does the average PSI index in African Americans compare to that of European Americans?',
      'Are there any commonalities between amino acid sequences among African American vs. European Americans?',
      'Length of Amino Acids'))

st.markdown("***")
st.text("")

if visualization == 'How Does the Average APA Site in African Americans Compare to that of European Americans?':
    st.subheader("Poly A Sites Mean")
    poly_a_mean = all_races.groupby('Race')['polyA_sites_in_gene'].mean()
    poly_a_mean
    st.subheader("Poly A Sites Sum")
    poly_a_sum = all_races.groupby('Race')['polyA_sites_in_gene'].sum()
    poly_a_sum
    st.subheader("Poly A Sites Median")
    poly_a_median = all_races.groupby('Race')['polyA_sites_in_gene'].median()
    poly_a_median

elif visualization == 'How does the average PSI index in African Americans compare to that of European Americans?':
    psisheet = pd.read_csv('psi_sheet.csv')
    psisheet
    psisheet['psi_mean'] = psisheet.mean(axis=1)
    all_races['gene_name_class'] = all_races['gene_name'] + all_races['gene_class']
    joined_sheets = all_races.merge(psisheet, how="inner")
    col4, col5, col6 = st.columns([3, 3, 3])
    with col4:
        race_psi_index = joined_sheets.groupby('Race')['psi_mean'].mean()
        race_psi_index
    with col5:
        race_psi_index = joined_sheets.groupby('Race')['psi_mean'].median()
        race_psi_index
    with col6:
        race_psi_index = joined_sheets.groupby('Race')['psi_mean'].sum()
        race_psi_index
elif visualization == 'Are there any commonalities between amino acid sequences among African American vs. European Americans?':
    with open('gene_sequences_aa.txt') as f: 
        gene_aa = Counter(c for line in f for c in line.strip())
    with open('gene_sequences_ea.txt') as f: 
        gene_ea = Counter(c for line in f for c in line.strip())
    diff = Counter(gene_aa) - Counter(gene_ea)

    # aa
    lists = sorted(gene_aa.items())
    x, y = zip(*lists)
    plt.bar(x, y)
    plt.title('Amino Acids and Codons in African Americans')
    plt.xlabel('Amino Acids (Upper Case) & Codons (lower case)')
    plt.ylabel('Count (n)')
    st.pyplot(fig=plt)

    # ae
    lists = sorted(gene_ea.items())
    x, y = zip(*lists)
    plt.bar(x, y)
    plt.title('Amino Acids and Codons in European Americans')
    plt.xlabel('Amino Acids (Upper Case) & Codons (lower case)')
    plt.ylabel('Count (n)')
    plt.savefig('gene_aa.png')
    st.pyplot(fig=plt)

    # both
    lists = sorted(diff.items())
    x, y = zip(*lists)
    plt.bar(x, y)
    plt.title('Amino Acids and Codons Differences in African and European Americans')
    plt.xlabel('Amino Acids (Upper Case) & Codons (lower case)')
    plt.ylabel('Count (n)')
    st.pyplot(fig=plt)

elif visualization == 'Length of Amino Acids':
    
    # length stuff for ea
    st.header("Length Observations for European American Amino Acids")
    with open ('gene_sequences_ea.txt') as f: 
        count = 0
        total = 0
        min_amino_acid = 0
        max_amino_acid = 0
        lines = f.readlines()
        for line in lines:
            count += 1
            total += len(line)
            if min_amino_acid == 0:
                min_amino_acid = len(line)
            elif len(line) < min_amino_acid:
                min_amino_acid = len(line)
            if len(line) > max_amino_acid:
                max_amino_acid = len(line)
        st.subheader("Mean Length:")
        total / count
        st.subheader("Minimum Length:")
        min_amino_acid
        st.subheader("Maximum Length:")
        max_amino_acid
    
    st.header("Length Observations for European American Amino Acids")
    with open ('gene_sequences_aa.txt') as f: 
        count = 0
        total = 0
        min_amino_acid = 0
        max_amino_acid = 0
        lines = f.readlines()
        for line in lines:
            count += 1
            total += len(line)
            if min_amino_acid == 0:
                min_amino_acid = len(line)
            elif len(line) < min_amino_acid:
                min_amino_acid = len(line)
            if len(line) > max_amino_acid:
                max_amino_acid = len(line)
        st.subheader("Mean Length:")
        total / count
        st.subheader("Minimum Length:")
        min_amino_acid
        st.subheader("Maximum Length:")
        max_amino_acid

elif visualization == 'About the Dataset':
    st.subheader("Dataset")
    all_races
    st.text("")
    col4, col5, col6 = st.columns([3, 3, 3])
    with col4:
        # visualization for gene_biotype
        st.subheader("Gene Biotypes")
        st.caption("Here I will include a short explanation of what this graph shows.")
        st.write()
        gene_biotype_graph = sns.catplot(data=all_races, x="gene_biotype", kind="count", ci=None)
        st.pyplot(gene_biotype_graph)

    with col5:
        # visualization for pair type
        st.subheader("Pair Types")
        st.caption("Here I will include a short explanation of what this graph shows.")
        pair_type_graph = sns.catplot(data=all_races, x="pair_type", kind="count", ci=None)
        st.pyplot(pair_type_graph)

    with col6:
        # visualization for gene class
        st.subheader("Gene Classes")
        st.caption("Here I will include a short explanation of what this graph shows.")
        gene_class_graph = sns.catplot(data=all_races, x="gene_class", kind="count", ci=None)
        st.pyplot(gene_class_graph)