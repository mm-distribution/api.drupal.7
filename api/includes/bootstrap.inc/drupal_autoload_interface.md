# drupal_autoload_interface()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3488–3490 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3488-L3490)
- **Topics:** [registry](../../topics/registry.md)

## Signature

```php
function drupal_autoload_interface($interface)
```

## Documentation

```text
Confirms that an interface is available.

This function is rarely called directly. Instead, it is registered as an
spl_autoload()  handler, and PHP calls it for us when necessary.

@param $interface
  The name of the interface to check or load.

@return
  TRUE if the interface is currently available, FALSE otherwise.
```

## Code

```php
function drupal_autoload_interface($interface) {
  return _registry_check_code('interface', $interface);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
