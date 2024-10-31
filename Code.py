import seaborn as sns
import matplotlib.pyplot as plt

# Data for chromosome sizes and number of genes for B. nigra
chromosome_sizes_bnigra = [54731903, 73743414, 59024541, 51417425, 67898307, 61872432, 59877746, 71984002]
num_genes_bnigra = [131, 293, 230, 237, 237, 154, 128, 203]

# Data for chromosome sizes and number of genes for S. arvensis
chromosome_sizes_sarvensis = [46408851, 43419538, 37284882, 47784266, 52171196, 49852727, 49153139, 42090328, 36737036]
num_genes_sarvensis = [129, 222, 147, 182, 236, 220, 162, 174, 150]

# Data for chromosome sizes and number of genes for S. alba
chromosome_sizes_salba = [57158731, 31689451, 31007024, 32852875, 28507362, 38871341, 29247975, 32512709, 44420566, 28290049, 30853752, 30697166]
num_genes_salba = [86, 108, 101, 128, 94, 111, 107, 90, 124, 108, 89, 100]

# Create a single figure with three subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot for B. nigra
sns.regplot(x=chromosome_sizes_bnigra, y=num_genes_bnigra, scatter_kws={'s': 100}, color='blue', ax=axes[0])
axes[0].set_xlabel('Chromosome size')
axes[0].set_ylabel('Number of genes')
axes[0].set_title('B. nigra', fontstyle='italic')

# Plot for S. arvensis
sns.regplot(x=chromosome_sizes_sarvensis, y=num_genes_sarvensis, scatter_kws={'s': 100}, color='blue', ax=axes[1])
axes[1].set_xlabel('Chromosome size')
# axes[1].set_ylabel('Number of genes')
axes[1].set_title('S. arvensis', fontstyle='italic')

# Plot for S. alba
sns.regplot(x=chromosome_sizes_salba, y=num_genes_salba, scatter_kws={'s': 100}, color='blue', ax=axes[2])
axes[2].set_xlabel('Chromosome size')
# axes[2].set_ylabel('Number of genes')
axes[2].set_title('S. alba', fontstyle='italic')

# Add a common title for the entire figure
# fig.suptitle('Relationship between chromosome size and number of RGAs')

# Show the plot
plt.show()
