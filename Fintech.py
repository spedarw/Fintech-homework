
# coding: utf-8

# In[8]:

import numpy as np
k=9100
premium_call=179
premium_put=185

interval=500
st=np.arange(k-interval,k+interval)
#st


# In[9]:

payoff_longcall=np.maximum(st-k,0)-premium_call
payoff_shortcall=-payoff_longcall


# In[10]:

import matplotlib.pyplot as plt
plt.plot(st,payoff_longcall)
plt.plot(st,payoff_shortcall)
plt.show()


# In[14]:

import numpy as np
k=9100
premium_call=179
premium_put=185

interval=500
st=np.arange(k-interval,k+interval)
#st


# In[15]:

payoff_longput=np.maximum(k-st,0)-premium_put
payoff_shortput= -payoff_longput


# In[16]:

import matplotlib.pyplot as plt
plt.plot(st,payoff_longput)
plt.plot(st,payoff_shortput)
plt.show()


# In[ ]:



