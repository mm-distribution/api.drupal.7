# field_filter_xss()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 756–758 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L756-L758)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function field_filter_xss($string)
```

## Documentation

```text
Like filter_xss_admin(), but with a shorter list of allowed tags.

Used for items entered by administrators, like field descriptions,
allowed values, where some (mainly inline) mark-up may be desired
(so check_plain() is not acceptable).
```

## Code

```php
function field_filter_xss($string) {
  return filter_xss($string, _field_filter_xss_allowed_tags());
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
