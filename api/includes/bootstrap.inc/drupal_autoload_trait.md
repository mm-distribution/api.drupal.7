# drupal_autoload_trait()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3520–3522 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3520-L3522)
- **Topics:** [registry](../../topics/registry.md)

## Signature

```php
function drupal_autoload_trait($trait)
```

## Documentation

```text
Confirms that a trait is available.

This function is rarely called directly. Instead, it is registered as an
spl_autoload() handler, and PHP calls it for us when necessary.

@param string $trait
  The name of the trait to check or load.

@return bool
  TRUE if the trait is currently available, FALSE otherwise.
```

## Code

```php
function drupal_autoload_trait($trait) {
  return _registry_check_code('trait', $trait);
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
