# openid_normalize()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 283–298 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L283-L298)
- **Module/theme:** openid

## Signature

```php
function openid_normalize($identifier)
```

## Documentation

```text
Normalize the given identifier.

The procedure is described in OpenID Authentication 2.0, section 7.2.
```

## Code

```php
function openid_normalize($identifier) {
  $methods = module_invoke_all('openid_normalization_method_info');
  drupal_alter('openid_normalization_method_info', $methods);

  // Execute each method in turn, stopping after the first method accepted
  // the identifier.
  foreach ($methods as $method) {
    $result = $method($identifier);
    if ($result !== NULL) {
      $identifier = $result;
      break;
    }
  }

  return $identifier;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
