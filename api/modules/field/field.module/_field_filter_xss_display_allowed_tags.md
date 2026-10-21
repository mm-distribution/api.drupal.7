# _field_filter_xss_display_allowed_tags()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 770–772 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L770-L772)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function _field_filter_xss_display_allowed_tags()
```

## Documentation

```text
Human-readable list of allowed tags, for display in help texts.
```

## Code

```php
function _field_filter_xss_display_allowed_tags() {
  return '<' . implode('> <', _field_filter_xss_allowed_tags()) . '>';
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
