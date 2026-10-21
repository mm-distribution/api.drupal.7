# hook_archiver_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4106–4108 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4106-L4108)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_archiver_info_alter(&$info)
```

## Documentation

```text
Alter archiver information declared by other modules.

See hook_archiver_info() for a description of archivers and the archiver
information structure.

@param $info
  Archiver information to alter (return values from hook_archiver_info()).
```

## Code

```php
function hook_archiver_info_alter(&$info) {
  $info['tar']['extensions'][] = 'tgz';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_archiver_info_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
