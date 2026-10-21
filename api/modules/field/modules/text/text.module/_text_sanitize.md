# _text_sanitize()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 315–325 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L315-L325)
- **Module/theme:** text

## Signature

```php
function _text_sanitize($instance, $langcode, $item, $column)
```

## Documentation

```text
Sanitizes the 'value' or 'summary' data of a text value.

Depending on whether the field instance uses text processing, data is run
through check_plain() or check_markup().

@param $instance
  The instance definition.
@param $langcode
 The language associated to $item.
@param $item
  The field value to sanitize.
@param $column
  The column to sanitize (either 'value' or 'summary').

@return
 The sanitized string.
```

## Code

```php
function _text_sanitize($instance, $langcode, $item, $column) {
  // If the value uses a cacheable text format, text_field_load() precomputes
  // the sanitized string.
  if (isset($item["safe_$column"])) {
    return $item["safe_$column"];
  }
  if ($item[$column] === '') {
    return '';
  }
  return $instance['settings']['text_processing'] ? check_markup($item[$column], $item['format'], $langcode) : check_plain($item[$column]);
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
