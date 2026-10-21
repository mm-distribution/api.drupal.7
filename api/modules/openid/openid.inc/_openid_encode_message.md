# _openid_encode_message()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 350–366 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L350-L366)
- **Module/theme:** openid

## Signature

```php
function _openid_encode_message($message)
```

## Documentation

```text
Encode a message from _openid_create_message for HTTP Post
```

## Code

```php
function _openid_encode_message($message) {
  $encoded_message = '';

  $items = explode("\n", $message);
  foreach ($items as $item) {
    $parts = explode(':', $item, 2);

    if (count($parts) == 2) {
      if ($encoded_message != '') {
        $encoded_message .= '&';
      }
      $encoded_message .= rawurlencode(trim($parts[0])) . '=' . rawurlencode(trim($parts[1]));
    }
  }

  return $encoded_message;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
