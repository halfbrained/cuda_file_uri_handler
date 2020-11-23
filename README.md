# CudaText addon: file URI handler
Opens file:/// links in CudaText, for exmple:
* file:///etc/fstab
* file:///c:/WINDOWS/clock.txt
* file:///install.inf

For this to work "links_regex" option needs to be modified:
```
\\b(mailto:)?\\w[\\w\\-\\.]*@\\w[\\w\\-\\.]*\\.\\w{2,}\\b|\\b(https?://|ftp://|magnet:\\?|www\\.|ftp\\.)\\w[\\w\\-\\.@]*(:\\d+)...
```
to
```
\\b(mailto:)?\\w[\\w\\-\\.]*@\\w[\\w\\-\\.]*\\.\\w{2}\\b|\\b(https?://|ftp://|file:///|magnet:\\?|www\\.|ftp\\.)\\w[\\w\\-\\.@]*:?(:\\d+)?(/[~\\w\\.\\-\\+\\/%]*)?(\\?[^<>'\"\\s]+)?(\\#[\\w\\-]*)?
```
