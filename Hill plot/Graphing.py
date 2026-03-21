import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Example values #{bi,mono}
simulation_values = [89.36842105263158,
                     83.21052631578948,
                     73.26315789473684,
                     70.10526315789474,
                     [58.473684210526315, 38.89473684210526],
                     66.63157894736842]
experimental_values = [86, 100, 91, 90, 91.7, 90.6]
simulation_errors = [1.7784381200141166,
                     1.705003785193395,
                     1.1573438046474837,
                     1.3984060444328393,
                     [1.5664686616110966, 1.8434666997630567],
                     0.5083273852560485]

# 



# Labels for the cell type pairs
labels = ["(XO,AA)",
          "(XX,AA)",
          "(XXX,AA)",
          "(XXXX,AA)",
          "(XXX,AAA)",
          "(XXXX,AAAA)"]

# labels = ["Cooperativity",
#           "Dimer",
#           "Titration",
#           "Cascade",
#           "Experiment",
#           ""]
# Biological state colors per pair
state_colors = [
    "#E69F00",  # Inactive
    "#AA3377",  # Monoallelic
    "#F0E442",  # Biallelic
    "#0072B2",  # Triallelic
    "#F0E442",  # Bottom for stacked bar
    "#F0E442",  # Biallelic
]
# state_colors = [
#     "#F0E442",  # Inactive
#     "#F0E442",  # Monoallelic
#     "#F0E442",  # Biallelic
#     "#F0E442",  # Triallelic
#     "#F0E442",  # Bottom for stacked bar
#     "#F0E442",  # Biallelic
# ]
# Top color for the stacked bar
stack_top_color = "#AA3377"

n = len(labels)
x = np.arange(n) * 1.2  # spacing between pairs
width = 0.4

# PPT-friendly square figure
fig, ax = plt.subplots(figsize=(6,6))
ax.set_axisbelow(True)  # grid behind bars

for i in range(n):
    # Simulation bar
    if i == 4:  # XXX,AAA case -> stacked bar
        bottom_val = simulation_values[i][0]
        top_val = simulation_values[i][1]
        bottom_err = simulation_errors[i][0]
        top_err = simulation_errors[i][1]

        # Bottom stack
        ax.bar(x[i] - width/2,
               bottom_val,
               width,
               color=state_colors[i],
               edgecolor="black",
               yerr=bottom_err,
               ecolor="black",
               capsize=5)

        # Top stack
        ax.bar(x[i] - width/2,
               top_val,
               width,
               color=stack_top_color,
               edgecolor="black",
               bottom=bottom_val,
               yerr=top_err,
               ecolor="black",
               capsize=5)
    else:
        ax.bar(x[i] - width/2,
               simulation_values[i],
               width,
               color=state_colors[i],
               edgecolor="black",
               yerr=simulation_errors[i],
               ecolor="black",
               capsize=5)

    # Experimental bar
    exp_color = "#F0E442" if i == 4 else (state_colors[i] if i != 4 else stack_top_color)
    ax.bar(x[i] + width/2,
           experimental_values[i],
           width,
           color=exp_color,
           edgecolor="black",
           hatch='//')

# X-axis labels
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=11, rotation=45)
ax.tick_params(axis='x', pad=0)

# Axis labels
ax.set_ylabel("Mean % of cells", weight="bold", fontsize=14)
ax.set_xlabel("Mechanisms", weight="bold", fontsize=14)

# Grid
ax.grid(axis="y", linestyle="--", alpha=1, linewidth=0.8)
plt.margins(x=0.05)
plt.ylim(0, 110)

# Legend
legend_elements = [
    Patch(facecolor="#E69F00", edgecolor="black", label="Inactive"),
    Patch(facecolor="#AA3377", edgecolor="black", label="Monoallelic / Top Stack"),
    Patch(facecolor="#F0E442", edgecolor="black", label="Biallelic / Bottom Stack"),
    Patch(facecolor="#0072B2", edgecolor="black", label="Triallelic"),
    Patch(facecolor="white", edgecolor="black", hatch='//', label="Experimental"),
    Patch(facecolor="white", edgecolor="black", label="Simulation")
]
#ax.legend(handles=legend_elements, title="Cell State", fontsize=12, title_fontsize=12, loc='upper left')

plt.tight_layout()
#plt.show()
plt.savefig('/home/madhusud/modeling_gene_expression/FinalPlots/Xlinkedtitration_regulated', dpi=600, bbox_inches="tight")


#modelA-n1-3
# 93.35
# 2.7678735938769843
# 82.55
# 1.947365028964227
# 76.8
# 3.2375175757571664
# 71.0
# 3.0895668003487615
# [48.15, 47.65]
# [3.651443858857002, 4.111789359905731]
# 65.0
# 2.621232542862651

#Dimer #best 26

# 94.1923076923077
# 1.9919515613664527
# 89.73076923076923
# 1.80473618481261
# 85.38461538461539
# 2.5776262790126467
# 82.07692307692308
# 2.567088584877443
# [39.53846153846154, 58.61538461538461] (mono,bi)
# [3.5139167654012073, 3.495583659721499]
# 72.07692307692308
# 3.0652880560621965

#Dimer with n1=1
#22
# 92.54545454545455
# 2.2388397911108453
# 80.81818181818181
# 2.0324284037412355
# 72.81818181818181
# 2.8460217837584456
# 66.68181818181819
# 3.513554471010282
# [41.09090909090909, 54.95454545454545]
# [3.617321043250816, 3.7558806961868574]
# 59.45454545454545
# 3.040326807970283

#AR-quadratic n=1 best # 18

# 69.66666666666667 XX
# 3.377083607426809
# 84.38888888888889 XO
# 6.173869540654125
# 57.833333333333336
# 4.481279034742983
# 47.44444444444444
# 4.63124747019923
# [38.888888888888886, 53.388888888888886]
# [3.276020165144667, 3.7916068254136177] mono,bi
# 48.94444444444444
# 4.556037749983184

#AR quadratic with n1-3 (21 params)

# 86.0 XX
# 2.9709944883171033
# 94.76190476190476 XO
# 2.2936781084645883
# 82.0
# 3.8220081170623894
# 77.71428571428571
# 4.177244840469399
# [44.857142857142854, 52.80952380952381]
# [7.160147524306855, 7.395502247092104] mono,bi
# 76.38095238095238
# 3.8664112723226727

#cascade just 4 params

# 98.0
# 2.250329363228576
# 91.25
# 7.160504186889591
# 89.75
# 6.414425595830535
# 85.5
# 8.46993202113356
# [44.75, 53.75]
# [21.00474834227098, 20.185132432116397]
# 76.25
# 12.820624931634896

#cascade 20 
# 93.55
# 3.5431243191138595
# 89.6
# 2.8056221234870615
# 85.5
# 3.279617862425513
# 82.45
# 3.023467627765016
# [40.1, 58.2]
# [4.0882408081119035, 4.160080160578957]
# 73.65
# 2.8580358522766707

#cascade with n1-n3=1
#22
# 89.9090909090909
# 3.447723926944066
# 82.0
# 2.7021472621145324
# 70.27272727272727
# 2.3903199606561847
# 62.72727272727273
# 2.7610285582755125
# [38.31818181818182, 56.86363636363637]
# [3.319005786584254, 3.8901090718310276]
# 58.31818181818182
# 2.9549465662431853

#22 X linked molecular titration constitutive titer
# simulation_values = [89.77272727272727,
#                      81.04545454545455,
#                      75.63636363636364,
#                      70.54545454545455,
#                      [54.22727272727273, 39.77272727272727],
#                      65.5,
#                      69.0909090909091,
#                      56.86363636363637,
#                      47.0]
# simulation_errors = [1.1841884323076857,
#                      1.2984794182755313,
#                      1.0414472417456535,
#                      1.253095341099111,
#                      [1.3058838180487715, 1.4799260221680415],
#                      0.647171668748848,
#                      1.1394330839734326,
#                      1.5794890051889534,
#                      2.076460524953054]

#19 X linked molecular titration regulated titer

# simulation_values = [89.36842105263158,
#                      83.21052631578948,
#                      73.26315789473684,
#                      70.10526315789474,
#                      [58.473684210526315, 38.89473684210526],
#                      66.63157894736842,
#                      75.15789473684211,
#                      53.473684210526315,
#                      38.94736842105263]

# simulation_errors = [1.7784381200141166,
#                      1.705003785193395,
#                      1.1573438046474837,
#                      1.3984060444328393,
#                      [1.5664686616110966, 1.8434666997630567],
#                      0.5083273852560485,
#                      1.3290029794132793,
#                      1.5376939927485166,
#                      2.094409860002708]