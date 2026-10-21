# hook_admin_paths_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 525–531 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L525-L531)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_admin_paths_alter(&$paths)
```

## Documentation

```text
Redefine administrative paths defined by other modules.

@param $paths
  An associative array of administrative paths, as defined by implementations
  of hook_admin_paths().

@see hook_admin_paths()
```

## Code

```php
function hook_admin_paths_alter(&$paths) {
  // Treat all user pages as administrative.
  $paths['user'] = TRUE;
  $paths['user/*'] = TRUE;
  // Treat the forum topic node form as a non-administrative page.
  $paths['node/add/forum'] = FALSE;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_admin_paths_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
