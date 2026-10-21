# hook_stream_wrappers_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 2821–2824 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L2821-L2824)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_stream_wrappers_alter(&$wrappers)
```

## Documentation

```text
Alters the list of PHP stream wrapper implementations.

@see file_get_stream_wrappers()
@see hook_stream_wrappers()
```

## Code

```php
function hook_stream_wrappers_alter(&$wrappers) {
  // Change the name of private files to reflect the performance.
  $wrappers['private']['name'] = t('Slow files');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_stream_wrappers_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
