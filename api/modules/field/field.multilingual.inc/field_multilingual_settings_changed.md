# field_multilingual_settings_changed()

- **Type:** Function
- **File:** [`modules/field/field.multilingual.inc`](_file.md), lines 68–70 · [local source](../../../../source/modules/field/field.multilingual.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc#L68-L70)
- **Module/theme:** field
- **Topics:** [field_language](../../../topics/field_language.md)
- **Implements:** [hook_multilingual_settings_changed()](../../locale/locale.api.php/hook_multilingual_settings_changed.md)

## Signature

```php
function field_multilingual_settings_changed()
```

## Documentation

```text
Implements hook_multilingual_settings_changed().
```

## Code

```php
function field_multilingual_settings_changed() {
  field_info_cache_clear();
}
```

---
_Drupal 7.103 · [modules/field/field.multilingual.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.multilingual.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
