def remove_output(model, **kwargs):
    if model['type'] != 'notebook':
        return
    for cell in model['content']['cells']:
        if cell['cell_type'] == 'code':
            cell['execution_count'] = None
            cell['outputs'] = []

c.FileContentsManager.pre_save_hook = remove_output