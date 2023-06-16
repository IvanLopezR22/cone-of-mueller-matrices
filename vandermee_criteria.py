from utils.qm_graphic import qm_graphic
import numpy as np

def vandermee_criteria(main_matrix):
  z_masked, ax, X, Y, plt = qm_graphic(main_matrix)
  xmin, ymin = np.unravel_index(np.argmin(z_masked), z_masked.shape)
  mi = (X[xmin,ymin], Y[xmin,ymin], z_masked.min())
  ax.scatter(X[xmin,ymin], Y[xmin,ymin], z_masked.min(), c='red', s=10)
  print('el punto donde se elcanza el mínimo de la función qm es',mi)
  print('el valor mínimo alcanzado por la función qm es', z_masked.min(), 'por lo tanto:')
  if z_masked.min()<0:
      print('La matriz introducida NO es de Mueller')
  else:
      print('La matriz introducida es de Mueller')
  plt.show()