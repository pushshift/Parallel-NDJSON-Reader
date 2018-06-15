# Parallel NDJSON Reader

### Purpose
This script can read and process newline delimited data extremely quickly.  For NDJSON files, my 12 core Xeon was able to decode (json.loads) 90,000 Twitter objects per second.  This script is basically limited by the amount of CPUs you have and how fast your I/O subsystem is.

### Features

- Ability to select number of cores used by setting the value of the n_chunks variable.
- If the file is too small to split into N pieces, the script will scale to the maximum number of chunks possible.  This script is not meant for small files since there is a little bit of startup time involved.  This is meant to tear through big data (gigabytes / terabytes / petabytes).

jason@pushshift.io
https://pushshift.io/donations 



### End

