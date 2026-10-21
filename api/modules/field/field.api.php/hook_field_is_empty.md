# hook_field_is_empty()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 719–724 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L719-L724)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_is_empty($item, $field)
```

## Documentation

```text
Define what constitutes an empty item for a field type.

@param $item
  An item that may or may not be empty.
@param $field
  The field to which $item belongs.

@return
  TRUE if $field's type considers $item not to contain any data;
  FALSE otherwise.
```

## Code

```php
function hook_field_is_empty($item, $field) {
  if (empty($item['value']) && (string) $item['value'] !== '0') {
    return TRUE;
  }
  return FALSE;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_is_empty()".

- [field_test_field_is_empty()](../tests/field_test.field.inc/field_test_field_is_empty.md) — `modules/field/tests/field_test.field.inc`
- [file_field_is_empty()](../../file/file.field.inc/file_field_is_empty.md) — `modules/file/file.field.inc`
- [image_field_is_empty()](../../image/image.field.inc/image_field_is_empty.md) — `modules/image/image.field.inc`
- [list_field_is_empty()](../modules/list/list.module/list_field_is_empty.md) — `modules/field/modules/list/list.module`
- [number_field_is_empty()](../modules/number/number.module/number_field_is_empty.md) — `modules/field/modules/number/number.module`
- [taxonomy_field_is_empty()](../../taxonomy/taxonomy.module/taxonomy_field_is_empty.md) — `modules/taxonomy/taxonomy.module`
- [text_field_is_empty()](../modules/text/text.module/text_field_is_empty.md) — `modules/field/modules/text/text.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
