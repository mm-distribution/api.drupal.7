# _openid_parse_message()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 372–385 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L372-L385)
- **Module/theme:** openid

## Signature

```php
function _openid_parse_message($message)
```

## Documentation

```text
Convert a direct communication message
into an associative array.
```

## Code

```php
function _openid_parse_message($message) {
  $parsed_message = array();

  $items = explode("\n", $message);
  foreach ($items as $item) {
    $parts = explode(':', $item, 2);

    if (count($parts) == 2) {
      $parsed_message[$parts[0]] = $parts[1];
    }
  }

  return $parsed_message;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
