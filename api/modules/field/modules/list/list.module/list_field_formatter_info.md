# list_field_formatter_info()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 445–456 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L445-L456)
- **Module/theme:** list
- **Implements:** [hook_field_formatter_info()](../../../field.api.php/hook_field_formatter_info.md)

## Signature

```php
function list_field_formatter_info()
```

## Documentation

```text
Implements hook_field_formatter_info().
```

## Code

```php
function list_field_formatter_info() {
  return array(
    'list_default' => array(
      'label' => t('Default'),
      'field types' => array('list_integer', 'list_float', 'list_text', 'list_boolean'),
    ),
    'list_key' => array(
      'label' => t('Key'),
      'field types' => array('list_integer', 'list_float', 'list_text', 'list_boolean'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
