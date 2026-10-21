# field_theme()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 337–346 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L337-L346)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function field_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function field_theme() {
  return array(
    'field' => array(
      'render element' => 'element',
    ),
    'field_multiple_value_form' => array(
      'render element' => 'element',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
