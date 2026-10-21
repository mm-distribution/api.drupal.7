# options_help()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 11–19 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L11-L19)
- **Module/theme:** options
- **Implements:** [hook_help()](../../../../system/system.api.php/hook_help.md)

## Signature

```php
function options_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function options_help($path, $arg) {
  switch ($path) {
    case 'admin/help#options':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The Options module defines checkbox, selection, and other input widgets for the Field module. See the <a href="@field-help">Field module help page</a> for more information about fields.', array('@field-help' => url('admin/help/field'))) . '</p>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
