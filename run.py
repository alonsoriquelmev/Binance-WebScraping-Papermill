import papermill as pm

try:
    pm.execute_notebook('btc_webscrapping.ipynb', 'destination.ipynb')
    print('Notebook ejecutado correctamente')
except Exception as e:
    print(f'Error {e} ha ocurrido!')
