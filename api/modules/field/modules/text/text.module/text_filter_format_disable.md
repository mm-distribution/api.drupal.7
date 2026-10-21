# text_filter_format_disable()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 619–621 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L619-L621)
- **Module/theme:** text
- **Implements:** [hook_filter_format_disable()](../../../../filter/filter.api.php/hook_filter_format_disable.md)

## Signature

```php
function text_filter_format_disable($format)
```

## Documentation

```text
Implements hook_filter_format_disable().
```

## Code

```php
function text_filter_format_disable($format) {
  field_cache_clear();
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
