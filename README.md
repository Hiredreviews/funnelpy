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

The second function **funnelplot**  first calls  **sigmas** to retrieve those two dataframes, and then additionally visualises the funnel plot.

**funnelplot** exists to take your inputs and return you a -- well -- funnel plot.

Power users may prefer to use **sigmas** to simply perform the confidence interval calculations and have the flexibility to use these as inputs into their own plots.

## Parameters

### `fpy.sigmas(groups, samplesizes, incidents, [length])`

- `groups` (`string`): a list of strings, naming the groups to be plotted.
- `samplesizes` (`int`): a list of integers, representing the sample sizes of each member of the group.
- `incidents` (`int`): a list of integers, representing the number of times an event occured for each member of the group.
- `length` (`int`): (Optional) an integer representing the number of intervals across the x axis to be plotted. Defaults to 50 if omitted. This effectively dictates the "smoothness" of the sigma curves. A small number is jarring, a large number is smooth.

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

This example uses the same data but does not visualise the funnel plot.
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

## Release History
* 0.2.0
    * First somewhat stable release. Anything prior to this is going to be a disaster.

## Author

Justin Lyons

Distributed under the MIT license.

[https://github.com/lyonjust/funnelpy]