# hook_date_formats_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4241–4245 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4241-L4245)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_date_formats_alter(&$formats)
```

## Documentation

```text
Alter date formats declared by another module.

Called by _system_date_format_types_build() to allow modules to alter the
return values from implementations of hook_date_formats().
```

## Code

```php
function hook_date_formats_alter(&$formats) {
  foreach ($formats as $id => $format) {
    $formats[$id]['locales'][] = 'en-ca';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_date_formats_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
