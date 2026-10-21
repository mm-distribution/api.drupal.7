# _openid_create_message()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 335–345 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L335-L345)
- **Module/theme:** openid

## Signature

```php
function _openid_create_message($data)
```

## Documentation

```text
Create a serialized message packet as per spec: $key:$value\n .
```

## Code

```php
function _openid_create_message($data) {
  $serialized = '';

  foreach ($data as $key => $value) {
    if ((strpos($key, ':') !== FALSE) || (strpos($key, "\n") !== FALSE) || (strpos($value, "\n") !== FALSE)) {
      return NULL;
    }
    $serialized .= "$key:$value\n";
  }
  return $serialized;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
