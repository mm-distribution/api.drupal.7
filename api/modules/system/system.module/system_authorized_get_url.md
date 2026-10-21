# system_authorized_get_url()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1835–1842 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1835-L1842)
- **Module/theme:** system
- **Topics:** [authorize](../../../topics/authorize.md)

## Signature

```php
function system_authorized_get_url(array $options = array())
```

## Documentation

```text
Return the URL for the authorize.php script.

@param array $options
  Optional array of options to pass to url().
@return
  The full URL to authorize.php, using HTTPS if available.

@see system_authorized_init()
```

## Code

```php
function system_authorized_get_url(array $options = array()) {
  global $base_url;
  // Force HTTPS if available, regardless of what the caller specifies.
  $options['https'] = TRUE;
  // We prefix with $base_url so we get a full path even if clean URLs are
  // disabled.
  return url($base_url . '/authorize.php', $options);
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
