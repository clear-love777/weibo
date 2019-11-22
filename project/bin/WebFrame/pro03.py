from PIL import Image
import numpy as np

I = Image.open('./static/img/author-main1.jpg')
ip=np.array(I)
I.show()
I_array = np.array(I)
print(I_array.shape)