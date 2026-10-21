# registry_rebuild()

- **Type:** Function
- **File:** [`includes/bootstrap.inc`](_file.md), lines 3614–3617 · [local source](../../../source/includes/bootstrap.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc#L3614-L3617)
- **Topics:** [registry](../../topics/registry.md)

## Signature

```php
function registry_rebuild()
```

## Documentation

```text
Rescans all enabled modules and rebuilds the registry.

Rescans all code in modules or includes directories, storing the location of
each interface or class in the database.
```

## Code

```php
function registry_rebuild() {
  system_rebuild_module_data();
  registry_update();
}
```

---
_Drupal 7.103 · [includes/bootstrap.inc](https://github.com/drupal/drupal/blob/7.103/includes/bootstrap.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
