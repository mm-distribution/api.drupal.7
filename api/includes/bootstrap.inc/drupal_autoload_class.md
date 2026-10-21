# drupal_autoload_class()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3504–3506 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3504-L3506)
- **Topics:** [registry](../../topics/registry.md)

## Signature

```php
function drupal_autoload_class($class)
```

## Documentation

```text
Confirms that a class is available.

This function is rarely called directly. Instead, it is registered as an
spl_autoload()  handler, and PHP calls it for us when necessary.

@param $class
  The name of the class to check or load.

@return
  TRUE if the class is currently available, FALSE otherwise.
```

## Code

```php
function drupal_autoload_class($class) {
  return _registry_check_code('class', $class);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
