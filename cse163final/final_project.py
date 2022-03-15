import streamlit as st
import pandas as pd
import seaborn as sns


col1, col2, col3 = st.columns([3, 1, 1])
st.text("")
st.text("")
col4, col5, col6 = st.columns([3, 3, 3])


with col1:
    st.title("CSE 163 Final Project")
    st.caption("Here I will include a short description on our project.")

# displaying data
aa = pd.read_csv('/Users/faithong/Desktop/cse163final/data_aa.csv')
ea = pd.read_csv('/Users/faithong/Desktop/cse163final/data_ea.csv')

aa['Race'] = "African-American"
ea['Race'] = "European-American"
all_races = aa.merge(ea, how='outer')
all_races = all_races.loc[:, all_races.columns != 'gene_id']
st.markdown("***")

st.text("")
st.text("")

visualization = st.radio(
     "Select the visualizations you're intererested in seeing",
     ('Gene Classifications', 'Mutations', 'Location'))

if visualization == 'Gene Classifications':
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
else:
     st.write("You didn't select gene classifications.")