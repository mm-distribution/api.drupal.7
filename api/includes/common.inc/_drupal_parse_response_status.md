# _drupal_parse_response_status()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1180–1192 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1180-L1192)
- **Topics:** [http_handling](../../topics/http_handling.md)

## Signature

```php
function _drupal_parse_response_status($response)
```

## Documentation

```text
Splits an HTTP response status line into components.

See the @link http://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html status line definition @endlink
in RFC 2616.

@param string $respone
  The response status line, for example 'HTTP/1.1 500 Internal Server Error'.

@return array
  Keyed array containing the component parts. If the response is malformed,
  all possible parts will be extracted. 'reason_phrase' could be empty.
  Possible keys:
  - 'http_version'
  - 'response_code'
  - 'reason_phrase'
```

## Code

```php
function _drupal_parse_response_status($response) {
  $response_array = explode(' ', trim($response), 3);
  // Set up empty values.
  $result = array(
    'reason_phrase' => '',
  );
  $result['http_version'] = $response_array[0];
  $result['response_code'] = $response_array[1];
  if (isset($response_array[2])) {
    $result['reason_phrase'] = $response_array[2];
  }
  return $result;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
