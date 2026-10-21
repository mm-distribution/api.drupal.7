# hook_update_last_removed()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3607–3611 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3607-L3611)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_update_last_removed()
```

## Documentation

```text
Return a number which is no longer available as hook_update_N().

If you remove some update functions from your mymodule.install file, you
should notify Drupal of those missing functions. This way, Drupal can
ensure that no update is accidentally skipped.

Implementations of this hook should be placed in a mymodule.install file in
the same directory as mymodule.module.

@return
  An integer, corresponding to hook_update_N() which has been removed from
  mymodule.install.

@see hook_update_N()
```

## Code

```php
function hook_update_last_removed() {
  // We've removed the 5.x-1.x version of mymodule, including database updates.
  // The next update function is mymodule_update_5200().
  return 5103;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_update_last_removed()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
