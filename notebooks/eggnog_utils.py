from io import StringIO

import pandas as pd


s = '''A	RNA processing and modification
B	Chromatin Structure and dynamics
C	Energy production and conversion
D	Cell cycle control and mitosis
E	Amino Acid metabolism and transport
F	Nucleotide metabolism and transport
G	Carbohydrate metabolism and transport
H	Coenzyme metabolism
I	Lipid metabolism
J	Translation
K	Transcription
L	Replication and repair
M	Cell wall/membrane/envelope biogenesis
N	Cell motility
O	Post-translational modification, protein turnover, chaperone functions
P	Inorganic ion transport and metabolism
Q	Secondary Structure
T	Signal Transduction
U	Intracellular trafficking and secretion
V	Defense mechanisms
Y	Nuclear structure
W	Extracellular structures
Z	Cytoskeleton
R	General Functional Prediction only
S	Function Unknown'''

cog_categories = pd.read_table(StringIO(s), names=['letter', 'function'], index_col=0, squeeze=True)
cog_categories.head()


COLUMN_NAMES = ['query', 'seed_ortholog', 'evalue', 'score', 'predicted_name', 'go_terms', 
                'kegg_ko', 'bigg_reactions',
           'tax_scope', 'eggnog_ogs', 'best_og', 'cog_cat', 'eggnog_hmmm_desc']


def read_eggnog(filename):
    eggnog = pd.read_table(filename, header=None, names=COLUMN_NAMES)
    eggnog['cog_category_full'] = eggnog.cog_cat.map(
        lambda x: '; '.join([cog_categories[i] for i in x.split(', ')]) if pd.notnull(x) else x)
    return eggnog