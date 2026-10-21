# text_field_is_empty()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 171–176 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L171-L176)
- **Module/theme:** text
- **Implements:** [hook_field_is_empty()](../../../field.api.php/hook_field_is_empty.md)

## Signature

```php
function text_field_is_empty($item, $field)
```

## Documentation

```text
Implements hook_field_is_empty().
```

## Code

```php
function text_field_is_empty($item, $field) {
  if (!isset($item['value']) || $item['value'] === '') {
    return !isset($item['summary']) || $item['summary'] === '';
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
