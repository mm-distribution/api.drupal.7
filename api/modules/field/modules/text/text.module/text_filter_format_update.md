# text_filter_format_update()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 612–614 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L612-L614)
- **Module/theme:** text
- **Implements:** [hook_filter_format_update()](../../../../filter/filter.api.php/hook_filter_format_update.md)

## Signature

```php
function text_filter_format_update($format)
```

## Documentation

```text
Implements hook_filter_format_update().
```

## Code

```php
function text_filter_format_update($format) {
  field_cache_clear();
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
