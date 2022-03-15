import streamlit as st
import pandas as pd
import seaborn as sns


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
     print("apa")

elif visualization == 'How does the average PSI index in African Americans compare to that of European Americans?':
    psisheet = pd.read_csv('/home/psi_sheet.csv')
    psisheet
    psisheet['psi_mean'] = psisheet.mean(axis=1)
    all_races['gene_name_class'] = all_races['gene_name'] + all_races['gene_class']
    joined_sheets = all_races.merge(psisheet, how="inner")
    race_psi_index = joined_sheets.groupby('Race')['psi_mean'].mean()
    race_psi_index
    race_psi_index = joined_sheets.groupby('Race')['psi_mean'].median()
    race_psi_index
    race_psi_index = joined_sheets.groupby('Race')['psi_mean'].sum()
    race_psi_index
elif visualization == 'Are there any commonalities between amino acid sequences among African American vs. European Americans?':
    print("commonalites")
elif visualization == 'Length of Amino Acids':
    print("length")
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