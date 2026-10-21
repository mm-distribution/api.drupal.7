# hook_multilingual_settings_changed()

- **Type:** Hook (documentation function)
- **File:** [`modules/locale/locale.api.php`](_file.md), lines 35–37 · [local source](../../../../source/modules/locale/locale.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.api.php#L35-L37)
- **Module/theme:** locale
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_multilingual_settings_changed()
```

## Documentation

```text
Allow modules to react to language settings changes.

Every module needing to act when the number of enabled languages changes
should implement this. This is an "internal" hook and should not be invoked
elsewhere. The typical implementation would trigger some kind of rebuilding,
this way system components could properly react to the change of the enabled
languages number.
```

## Code

```php
function hook_multilingual_settings_changed() {
  field_info_cache_clear();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_multilingual_settings_changed()".

- [field_multilingual_settings_changed()](../../field/field.multilingual.inc/field_multilingual_settings_changed.md) — `modules/field/field.multilingual.inc`

---
_Drupal 7.103 · [modules/locale/locale.api.php](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
