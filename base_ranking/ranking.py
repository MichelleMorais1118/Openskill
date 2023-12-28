# Import openskill.py and plotting libraries.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm
from openskill.models import PlackettLuce

# Initialize Default/Starter Rating
model = PlackettLuce()
r = model.rating