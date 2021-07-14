# TWOC CI

## Discover TWOC FAIR Data Points
[![.github/workflows/count-twoc-fdp.yml](https://github.com/TrustedWorldOfCorona/ci/actions/workflows/count-twoc-fdp.yml/badge.svg)](https://github.com/TrustedWorldOfCorona/ci/actions/workflows/count-twoc-fdp.yml)

- query the [index](https://twoc-index.fair-dtls.surf-hosted.nl)
- resolve each entry
- count the entries
  - fails if the expected number of entries is not met

## Query aggregate results
[![.github/workflows/query-aggregate-fdp.yml](https://github.com/TrustedWorldOfCorona/ci/actions/workflows/query-aggregate-fdp.yml/badge.svg)](https://github.com/TrustedWorldOfCorona/ci/actions/workflows/query-aggregate-fdp.yml)

- query the index
- resolve each entry
  - find a sparql distribution
  - query aggregate results from the sparql endpoint
- aggregate the results from each query
  - fails if there are zero results
