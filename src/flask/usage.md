## Flask Data Server

  Simple http server for exchanging json data in a relatively civilized manner.

### Features:

    - Serve and store JSON compatable data structures.
    - Intelligently handle multiple separate deployment databases. (partially implimented)
    - Be as light as frickin possible!

### Uplaod:

    - `http post` of `json` to `http://hostname/usecase/deployment`.
    - Deployment section of uri is treated like a variable.
    - Response code 200 upon successful save of data.

### Download:
    - `http get` to `http://hostname/usecase/deployment`.
    -  
