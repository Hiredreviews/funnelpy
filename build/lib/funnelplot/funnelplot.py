import statistics
import math
from operator import truediv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def funnelplot(
	groups,
	samplesizes,
	incidents,
	length = 50,
	twosigma = True,
	threesigma = True,
	color_twosigma = '#CCCCCC',
	color_threesigma = '#CCCCCC',
	color_mean = '#CCCCCC',
	color_data = '#88BDE6',
	color_face = 'white',
	funnel_size = (10, 10),
	plt_title = None,
	plt_xlabel = None,
	plt_ylabel = None
	):
    
    # add z order etc??

    # calculate key values
    incident_rates = list(map(truediv, incidents, samplesizes)) 
    mean = statistics.mean(incident_rates)
    min_groupsize = min(samplesizes)
    max_groupsize = max(samplesizes)
    spread_groupsize = max_groupsize - min_groupsize
    interval = spread_groupsize / length

    # create lists
    lst_ss = [0] * int(length)
    lst_onesigma = [0] * int(length)
    lst_twosigma = [0] * int(length)
    lst_lowertwosigma = [0] * int(length)
    lst_uppertwosigma = [0] * int(length)
    lst_threesigma = [0] * int(length)
    lst_lowerthreesigma = [0] * int(length)
    lst_upperthreesigma = [0] * int(length)
    lst_chart_index = [0] * int(length)

    # populate
    lst_ss[0] = min_groupsize
    lst_chart_index[0] = 0

    for i in range(1, len(lst_ss[1:]) + 1):
        lst_chart_index[i] = max_groupsize / (len(lst_ss[1:]) + 1) * i
        if (lst_ss[i - 1] + interval) < (max_groupsize + interval):
            lst_ss[i] = (lst_ss[i - 1] + interval)


    for i in range(length):
        lst_onesigma[i] = math.sqrt(mean * (1 - mean) / lst_ss[i])
        lst_twosigma[i] = 1.96 * lst_onesigma[i]
        lst_lowertwosigma[i] = mean - lst_twosigma[i]
        lst_uppertwosigma[i] = mean + lst_twosigma[i]
        lst_threesigma[i] = 3 * lst_onesigma[i]
        lst_lowerthreesigma[i] = mean - lst_threesigma[i]
        lst_upperthreesigma[i] = mean + lst_threesigma[i]

    # create df to plot
    limits_to_plot = pd.DataFrame(
        {'chart_index': lst_chart_index,
         'lowertwosigma': lst_lowertwosigma,
         'uppertwosigma': lst_uppertwosigma,
         'lowerthreesigma': lst_lowerthreesigma,
         'upperthreesigma': lst_upperthreesigma,
         'mean' : mean
        })

    datapoints_to_plot = pd.DataFrame(
        {'samplesizes' : samplesizes,
        'incident_rates' : incident_rates
        })

	# plot
    fig, ax = plt.subplots(figsize=(8,8))
    
    if twosigma == True:
        ax = sns.lineplot(data=limits_to_plot, x = 'chart_index', y = 'uppertwosigma', color = color_twosigma)
        ax = sns.lineplot(data=limits_to_plot, x = 'chart_index', y = 'lowertwosigma', color = color_twosigma)
    
    if threesigma == True:
        ax = sns.lineplot(data=limits_to_plot, x = 'chart_index', y = 'upperthreesigma', color = color_threesigma)
        ax = sns.lineplot(data=limits_to_plot, x = 'chart_index', y = 'lowerthreesigma', color = color_threesigma)
        
    ax = sns.lineplot(data=limits_to_plot, x = 'chart_index', y = 'mean', color = color_mean)
    
    # need to weight this average
    ax = sns.scatterplot(data = datapoints_to_plot, x = 'samplesizes', y = 'incident_rates', color = color_data)

    ax.set_facecolor(color_face)
    fig.patch.set_facecolor(color_face)

    plt.title(plt_title)
    plt.xlabel(plt_xlabel)
    plt.ylabel(plt_ylabel)

if __name__ == "funnelpy":
    funnelpy()