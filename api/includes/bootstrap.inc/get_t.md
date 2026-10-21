# get_t()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3042–3050 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3042-L3050)
- **Topics:** [sanitization](../../topics/sanitization.md)

## Signature

```php
function get_t()
```

## Documentation

```text
Returns the name of the proper localization function.

get_t() exists to support localization for code that might run during
the installation phase, when some elements of the system might not have
loaded.

This would include implementations of hook_install(), which could run
during the Drupal installation phase, and might also be run during
non-installation time, such as while installing the module from the
module administration page.

Example usage:
@code
  $t = get_t();
  $translated = $t('translate this');
@endcode

Use t() if your code will never run during the Drupal installation phase.
Use st() if your code will only run during installation and never any other
time. Use get_t() if your code could run in either circumstance.

@see t()
@see st()
@ingroup sanitization
```

## Code

```php
function get_t() {
  static $t;
  // This is not converted to drupal_static because there is no point in
  // resetting this as it can not change in the course of a request.
  if (!isset($t)) {
    $t = drupal_installation_attempted() ? 'st' : 't';
  }
  return $t;
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
