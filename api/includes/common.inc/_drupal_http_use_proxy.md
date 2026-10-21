# _drupal_http_use_proxy()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 1200–1203 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L1200-L1203)
- **Topics:** [http_handling](../../topics/http_handling.md)

## Signature

```php
function _drupal_http_use_proxy($host)
```

## Documentation

```text
Helper function for determining hosts excluded from needing a proxy.

@return
  TRUE if a proxy should be used for this host.
```

## Code

```php
function _drupal_http_use_proxy($host) {
  $proxy_exceptions = variable_get('proxy_exceptions', array('localhost', '127.0.0.1'));
  return !in_array(strtolower($host), $proxy_exceptions, TRUE);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
