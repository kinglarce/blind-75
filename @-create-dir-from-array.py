"""
Input:
files = [
  '/webapp/assets/html/a.html',
  '/webapp/assets/html/b.html',
  '/webapp/assets/js/c.js',
  '/webapp/index.html',
]

Output:
-- webapp
  -- assets
    -- html
      -- a.html
      -- b.html
    -- js
      -- c.js
  -- index.html
"""

class TrieNode:
  def __init__(self):
    self.children = {}
    self.filename = None

root = TrieNode()

def printing_dir(node, space, level):
  if not node:
    return
  for filename in node.children.keys():
    print(space * level, '--', filename)
    printing_dir(node.children[filename], space, level + 1)

def create_dir(files):

  for i in range(len(files)):
    files_root = root
    file = files[i]
    left, right = 0, 1

    while right < len(file):

      if file[right] == '/' or right == len(file)-1:
        filename = file[left+1:right+1]
        # Create Trie
        if filename not in files_root.children:
          files_root.children[filename] = TrieNode()
          files_root.filename = filename
        files_root = files_root.children[filename]
        left, right = right, right + 1
      right += 1

  output_files_root = root
  printing_dir(output_files_root, " ", 1)

files = [
  '/webapp/assets/html/a.html',
  '/webapp/assets/html/b.html',
  '/webapp/assets/js/c.js',
  '/webapp/index.html',
]

create_dir(files)





