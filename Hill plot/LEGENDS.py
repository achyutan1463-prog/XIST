import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# # --- Define your 5 color-blind friendly colors ---
# colors = {
#     "No activation": "#E69F00",        
#     "Mono-allelic": "#AA3377",     
#     "Bi-allelic": "#F0E442",       
#     "Tri-allelic": "#0072B2",      
#     "Tetra-allelic": "#D55E00",   
# }

# # --- Create legend handles ---
# legend_elements = [
#     Patch(facecolor=clr, edgecolor='black', label=label)
#     for label, clr in colors.items()
# ]

# # --- Create a blank figure just for the legend ---
# fig, ax = plt.subplots(figsize=(3, 1.5))
# ax.axis('off')  # Hide axes

# # --- Add the legend ---
# legend = ax.legend(
#     handles=legend_elements,
#     loc='center',
#     frameon=True,
#     framealpha=1,
#     edgecolor='black',
#     ncol=6,  # number of columns
#     fontsize=9,
#     handlelength=1.5,
#     handleheight=1.0
# )

# # --- Save or show ---
# plt.tight_layout()
# #plt.savefig('/home/madhusud/modeling_gene_expression/FinalPlots/LegendBox.png',dpi=600,bbox_inches='tight',transparent=True)
# plt.show()

# import matplotlib.pyplot as plt
# from matplotlib.patches import Patch

# # --- Define your 5 color-blind friendly colors ---
# colors = {
#     "NO Xi": "#E69F00",        
#     "Xi": "#AA3377",     
#     "XiXi": "#F0E442",       
#     "XiXiXi": "#0072B2",      
#     "XiXiXiXi": "#D55E00",   
# }

# # --- Create legend handles ---
# legend_elements = [
#     Patch(facecolor=clr, edgecolor='black', label=label)
#     for label, clr in colors.items()
# ]

# # --- Create a blank figure just for the legend ---
# fig, ax = plt.subplots(figsize=(2, 3))  # taller figure for vertical legend
# ax.axis('off')  # Hide axes

# # --- Add the legend ---
# legend = ax.legend(
#     handles=legend_elements,
#     loc='center',
#     frameon=False,  # removed outer box
#     ncol=1,  # single column for vertical arrangement
#     fontsize=9,
#     handlelength=1.5,
#     handleheight=1.0
# )

# # --- Save or show ---
# plt.tight_layout()
# #plt.savefig('/home/madhusud/modeling_gene_expression/FinalPlots/LegendBox.png',dpi=600,bbox_inches='tight',transparent=True)
# plt.show()
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# --- Define your 5 color-blind friendly colors ---
colors = {
    "NO Xi": "#E69F00",        
    "Xi": "#AA3377",     
    "XiXi": "#F0E442",       
    "XiXiXi": "#0072B2",      
    "XiXiXiXi": "#D55E00",   
}

# --- Create legend handles ---
legend_elements = [
    Patch(facecolor=clr, edgecolor='black', label=label)
    for label, clr in colors.items()
]

# --- Create a blank figure just for the legend ---
fig, ax = plt.subplots(figsize=(2, 3))  # taller figure for vertical legend
ax.axis('off')  # Hide axes

# --- Add the legend ---
legend = ax.legend(
    handles=legend_elements,
    loc='center',
    frameon=False,  # removed outer box
    ncol=1,  # single column for vertical arrangement
    fontsize=9,
    handlelength=1.5,
    handleheight=1.0
)



# fig, ax = plt.subplots(figsize=(3, 3))

# # Create legend elements
# legend_elements = [
#     Patch(facecolor='white', edgecolor='black', label='Simulation'),       # solid
#     Patch(facecolor='white', edgecolor='black', hatch='//', label='Experiment')  # striped/dashed
# ]

# # Add horizontal legend without frame and with bold text
# ax.legend(handles=legend_elements, loc='center', fontsize=8, title_fontsize=10,
#           frameon=False, prop={'weight':'bold'}, ncol=2)

# # Hide axes
# ax.axis('off')

plt.tight_layout()
#plt.show()
plt.savefig('/home/madhusud/modeling_gene_expression/FinalPlots/LegendBoxhorizontal.png',dpi=600,bbox_inches='tight',transparent=True)


