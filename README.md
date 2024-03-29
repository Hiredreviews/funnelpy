# FunnelPy
> A basic Python package to create funnel plots (not to be confused with funnel charts). 

This package was inspired by Stephen Few's excellent article "Variation and Its Discontents". 
https://www.perceptualedge.com/articles/visual_business_intelligence/variation_and_its_discontents.pdf


## Installation

```sh
pip install funnelpy
import funnelpy.funnelpy as fpy
```
## Functions
The module funnelpy includes two functions.

The first function **sigmas** calculates the confidence intervals for a funnel plot and returns two dataframes, one storing the calculated upper and lower sigma curves (i.e. confidence intervals) and one storing the actual observed data. 

The second function **funnelplot** first calls **sigmas** to retrieve those two dataframes, and then additionally visualises the funnel plot.

**funnelplot** exists to take your inputs and return you a -- well -- funnel plot.

Power users may prefer to use **sigmas** to simply perform the confidence interval calculations and have the flexibility to use these as inputs into their own plots.

## Warning
The statistics behind funnel plots assume the underlying data is Normally distributed. Please ensure your datapoints are approximately Normal before using this package. The **normalize** parameter of the **sigmas** function may assist in transforming skewed data.

## Parameters

### `fpy.sigmas(groups, samplesizes, incidents, [length], [normalize])`

- `groups` (`string`): a list of strings, naming the groups to be plotted.
- `samplesizes` (`int`): a list of integers, representing the sample sizes of each member of the group.
- `incidents` (`int`): a list of integers, representing the number of times an event occured for each member of the group.
- `length` (`int`): (Optional) an integer representing the number of intervals across the x axis to be plotted. Defaults to 50 if omitted. This effectively dictates the "smoothness" of the sigma curves. A small number is jarring, a large number is smooth.
- `normalize` (`string`): (Optional) a string representing the transformation to be performed on the incident rates prior to calculating sigma curves. Defaults to "no" if omitted. Can be "square" for square transform or "sqrt" for square-root transform.

### `fpy.funnelplot(groups, samplesizes, incidents, [length], [twosigma], [threesigma], [color_twosigma], [color_threesigma], [color_mean], [color_data], [color_face], [funnel_size], [plt_title], [plt_xlabel], [plt_ylabel], [plt_ylim_min], [plt_ylim_max])`

- `groups` (`string`): a list of strings, naming the groups to be plotted.
- `samplesizes` (`int`): a list of integers, representing the sample sizes of each member of the group.
- `incidents` (`int`): a list of integers, representing the number of times an event occured for each member of the group.
- `length` (`int`): (Optional) an integer representing the number of intervals across the x axis to be plotted. Defaults to 50 if omitted. This effectively dictates the "smoothness" of the sigma curves. A small number is jarring, a large number is smooth.
- `twosigma` (`bool`): (Optional) a boolean flag to return the upper/lower "two sigma" (95% confidence interval) lines. Defaults to True if omitted.
- `threesigma` (`bool`): (Optional) a boolean flag to return the upper/lower "three sigma" (99.8% confidence interval) lines. Defaults to True if omitted.
- `color_twosigma` (`string`): (Optional) a string for color of the "two sigma" lines, passed to seaborn. Any supported seaborn colors are supported. Defaults to '#CCCCCC' if omitted.
- `color_threesigma` (`string`): (Optional) a string for color of the "three sigma" lines, passed to seaborn. Any supported seaborn colors are supported. Defaults to '#CCCCCC' if omitted.
- `color_mean` (`string`): (Optional) a string for color of the mean line, passed to seaborn. Any supported seaborn colors are supported. Defaults to '#CCCCCC' if omitted.
- `color_data` (`string`): (Optional) a string for color of the data points to be plotted on the scatter plot, passed to seaborn. Any supported seaborn colors are supported. Defaults to '#88BDE6' if omitted.
- `color_face` (`string`): (Optional) a string for color of the face of the plot, passed to seaborn. Any supported seaborn colors are supported. Defaults to 'white' if omitted.
- `funnel_size` (`int`): (Optional) a tuple of integers for size of the figure to be plotted. Passed to matplotlib. Defaults to '(10,10)' if omitted.
- `plt_title` (`string`): (Optional) a string for title of the plot, passed to matplotlib. Defaults to None if omitted.
- `plt_xlabel` (`string`): (Optional) a string for title of the x axis, passed to matplotlib. Defaults to None if omitted.
- `plt_ylabel` (`string`): (Optional) a string for title of the y axis, passed to matplotlib. Defaults to None if omitted.
- `plt_ylim_min` (`float`): (Optional) a float for minimum value of the y axis, passed to matplotlib. Defaults to None if omitted.
- `plt_ylim_max` (`float`): (Optional) a float for maximum value of the y axis, passed to matplotlib. Defaults to None if omitted.


## Usage Example - funnelplot

This example replicates the sample data used by Stephen Few in "Variation and Its Discontents", i.e. the sales performance of Tony, Mike, Jan et al.
```sh
import funnelpy.funnelpy as fpy

fpy.funnelplot(

    groups = [
    'Tony',
    'Mike',
    'Jan',
    'Bob',
    'Sheila',
    'Jeff',
    'Sandy',
    'Mitch',
    'Mary',
    'John'],
    
    samplesizes = [
    2,
    400,
    100,
    1000,
    2,
    10,
    500,
    200,
    10,
    2],
    
    incidents = [
    2,
    224,
    54,
    505,
    1,
    5,
    236,
    92,
    3,
    0],
    
    length = 100,
    
    twosigma = True,
    threesigma = True,
    color_data = '#F79646',
    color_mean = '#F79646',
    color_threesigma = 'Black',
    plt_title = 'Funnel Plot of Successful Sales Conversions',
    plt_xlabel = 'Sales Opportunities',
    plt_ylabel = 'Successful Sales Conversions',
    plt_ylim_min = -0.01,
    plt_ylim_max = 1.01
)
```
### Output
![Sample funnel plot output.](https://github.com/lyonjust/funnelpy/blob/master/sampleFunnel.png?raw=true)

## Usage Example - sigmas

This example uses the same data but does not visualise the funnel plot directly through the function.

Instead, we retrieve the calulcated confidence intervals and produce a plot through manual use of seaborn and matplotlib functionality. This gives us greater flexibility over visualisation design.
```sh
import funnelpy.funnelpy as fpy

df_sigmas, df_data = fpy.sigmas(

    groups = [
    'Tony',
    'Mike',
    'Jan',
    'Bob',
    'Sheila',
    'Jeff',
    'Sandy',
    'Mitch',
    'Mary',
    'John'],
    
    samplesizes = [
    2,
    400,
    100,
    1000,
    2,
    10,
    500,
    200,
    10,
    2],
    
    incidents = [
    2,
    224,
    54,
    505,
    1,
    5,
    236,
    92,
    3,
    0]
)
```

```sh
# scale datapoints by 100 to convert to percentages
df_data['incident_rates'] = df_data['incident_rates'] * 100

for col in ['lowertwosigma', 'uppertwosigma', 'lowerthreesigma', 'upperthreesigma', 'mean']:
    df_sigmas[col] = df_sigmas[col] * 100
```

```sh
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

# build plot
fig, ax = plt.subplots(figsize=(10,10))

# plot curves, utilizing zorder to ensure data points from scatterplot are layered on top of the curves
ax = sns.lineplot(data=df_sigmas, x = 'chart_index', y = 'uppertwosigma', color = '#b2afc3', zorder = 1)
ax = sns.lineplot(data=df_sigmas, x = 'chart_index', y = 'lowertwosigma', color = '#b2afc3', zorder = 1)
ax = sns.lineplot(data=df_sigmas, x = 'chart_index', y = 'upperthreesigma', color = 'Black', zorder = 2)
ax = sns.lineplot(data=df_sigmas, x = 'chart_index', y = 'lowerthreesigma', color = 'Black', zorder = 2)
ax = sns.lineplot(data=df_sigmas, x = 'chart_index', y = 'mean', color = '#F79646')
ax = sns.scatterplot(data = df_data, x = 'samplesizes', y = 'incident_rates', color = '#F79646', s = 80, zorder  = 3)

# tighten axes limits and give labels
ax.set_ylim(ymin = -1, ymax = 101)
ax.set_xlim(xmin = 0)
plt.yticks(range(0, 110, 10))
plt.title('Successful Sales Conversions')
plt.xlabel('Sales Opportunities')
plt.ylabel(None)

ax.yaxis.set_major_formatter(mtick.PercentFormatter())

# hide the top and right borders of the plot
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# annotate Mike as the only data point that is significant (95% confidence interval)
ax.annotate('Mike', xy=(400, 56.3),  xycoords='data',
            xytext=(475, 65), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.1, width = 0.5, headwidth = 7),
            horizontalalignment='right', verticalalignment='top')

# annotate the sigma curves and mean
# for mean we pick the exact y value from the sigmas dataframe
# we choose not to do this for the sigma curves as the labels end up overlapping
# so just hardcode these to something reasonable and legible
plt.annotate('Upper 3 Sigma Limit', (1015, 55))
plt.annotate('Upper 2 Sigma Limit', (1015, 53), color = '#b2afc3')
plt.annotate('Lower 2 Sigma Limit', (1015, 47), color = '#b2afc3')
plt.annotate('Lower 3 Sigma Limit', (1015, 45))
plt.annotate('Mean', (1015, df_sigmas.iloc[[-1]]['mean']), va = 'center', color = '#F79646')
```
### Output
![Sample funnel plot output.](https://github.com/lyonjust/funnelpy/blob/master/sampleFunnelPowerUser.png?raw=true)

## Release History
* 0.8.0
    * Extended length of sigma curves such that they will be the same distance along the x-axis as the furthest point. Previously they fell one "interval" short.
* 0.7.0
    * Bug fix on **normalize** parameter of the **sigmas** function.
* 0.6.0
    * **sigmas** **sqrt_normalize** parameter replaced by **normalize** which accepts either "square" or "sqrt" to allow transforming the data prior to calculating sigma curves.
* 0.5.0
    * **sigmas** now accepts a **sqrt_normalize** parameter to allow transforming the data prior to calculating sigma curves.
* 0.4.0
    * **sigmas** now returns the group names in the dataframe of data to plot.
* 0.3.0
    * Changed calculation of mean to weighted mean by sample size. I still intend to update this further to use the inverse-variance method, but I think this is a decent improvement until then.
    * Expanded usage example for **sigmas** to show how Stephen Few's example funnel plot could be more completely replicated by a "Power User".
* 0.2.0
    * First somewhat stable release. Anything prior to this is going to be a disaster.

## Author

Justin Lyons

@lyonjust

Distributed under the MIT license.

[https://github.com/lyonjust/funnelpy]