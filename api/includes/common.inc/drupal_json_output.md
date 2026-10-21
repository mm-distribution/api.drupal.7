# drupal_json_output()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5321–5328 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5321-L5328)

## Signature

```php
function drupal_json_output($var = NULL)
```

## Documentation

```text
Returns data in JSON format.

This function should be used for JavaScript callback functions returning
data in JSON format. It sets the header for JavaScript output.

@param $var
  (optional) If set, the variable will be converted to JSON and output.
```

## Code

```php
function drupal_json_output($var = NULL) {
  // We are returning JSON, so tell the browser.
  drupal_add_http_header('Content-Type', 'application/json');

  if (isset($var)) {
    echo drupal_json_encode($var);
  }
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
