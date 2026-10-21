# number_help()

- **Type:** Function
- **File:** [`modules/field/modules/number/number.module`](_file.md), lines 11–19 · [local source](../../../../../../source/modules/field/modules/number/number.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module#L11-L19)
- **Module/theme:** number
- **Implements:** [hook_help()](../../../../system/system.api.php/hook_help.md)

## Signature

```php
function number_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function number_help($path, $arg) {
  switch ($path) {
    case 'admin/help#number':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Number module defines various numeric field types for the Field module. Numbers can be in integer, decimal, or floating-point form, and they can be formatted when displayed. Number fields can be limited to a specific set of input values or to a range of values. See the <a href="@field-help">Field module help page</a> for more information about fields.', array('@field-help' => url('admin/help/field'))) . '</p>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/number/number.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.module) · Licensed GPL-2.0-or-later (see LICENSE)._
