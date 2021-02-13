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
    
	funnelpy.sigmas.sigmas(
	groups,
	samplesizes,
	incidents,
	length,
	twosigma,
	threesigma,
	color_twosigma,
	color_threesigma,
	color_mean,
	color_data,
	color_face,
	funnel_size,
	plt_title,
	plt_xlabel,
	plt_ylabel
	)