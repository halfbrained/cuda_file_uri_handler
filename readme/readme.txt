Plugin for CudaText.
Opens file:/// links in CudaText, for example:

file:///etc/fstab
file:///c:/WINDOWS/clock.txt
file:///install.inf

Just a filename (last line) will be looked for in the directory of the current file first, then in the directories specified in plugin's config file. 
------------------------------

For CudaText to recognise file urls, 'links_regex' option needs to be changed. For example by adding a line to 'settings/user.json' file:

"links_regex" : "\\b(mailto:)?\\w[\\w\\-\\.]*@\\w[\\w\\-\\.]*\\.\\w{2}\\b|\\b(https?://|ftp://|file:///|magnet:\\?|www\\.|ftp\\.)\\w[\\w\\-\\.@]*:?(:\\d+)?(/[~\\w\\.\\-\\+\\/%]*)?(\\?[^<>'\"\\s]+)?(\\#[\\w\\-]*)?",

------------------------------

Authors:
  @halfbrained (at GitHub)

License: MIT
