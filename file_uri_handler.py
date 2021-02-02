import os
import json

from cudatext import *

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_file_uri_handler.json')

_config_json = """
{
  "dirs_to_check":[
    
  ]   
}
"""
prefix = 'file:///'

user_dirs = [] 


class Command:
    
  def __init__(self):
    self.load_config()

  def config(self):
    if not os.path.isfile(fn_config):
      with open(fn_config, 'w') as f:
        f.write(_config_json)
    file_open(fn_config)
  
         
  def on_click_link(self, ed_self, state, link):
    if not link.startswith(prefix)  or  state != 'L':
      return
    
    is_rel = False
    if link[len(prefix)+1] == ':': # windows absolute, ignore third slash
      path = os.path.normcase(link[len(prefix):]) # fix slashes
    elif link.count('/') == 3: # relative
      path = link[len(prefix):]
      is_rel = True
    else: # linux absolute
      path = link[len(prefix)-1:]
      
    found = False
    if is_rel:
      f = ed_self.get_filename()
      curdir,filename = os.path.split(f)
      
      dirs = [curdir, *user_dirs]  if f else  user_dirs 
      
      for folder in dirs:
        abspath = os.path.join(folder, path)
        if os.path.isfile(abspath):
          file_open(abspath)
          found = True
          break
    else:
      if os.path.isfile(path):
        file_open(path)
        found = True
    
    if not found:
      print('file URI handler: couldn\'t find: {0} [{1}]'.format(path, link))
      
    return not found  # return False for success lol
    
 
  def load_config(self):
    try:
      user_dirs.clear()

      if not os.path.isfile(fn_config):
        print('file URI handler: Missing config file. Creating an empty one.')
        with open(fn_config, 'w') as f:
          f.write(_config_json)
          return
          
      with open(fn_config, 'r') as f:
        j = json.load(f)
          
      user_dirs.extend(j.get('dirs_to_check', []))
        
    except Exception as e:
      user_dirs.clear()
        
      print('file URI handler: Failed to load config, using empty')
      print(' - Error:{0}: {1}'.format(type(e), e)) # 'raise' here is not printed
