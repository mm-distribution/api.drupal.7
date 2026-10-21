# list_help()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.module`](_file.md), lines 11–19 · [local source](../../../../../../source/modules/field/modules/list/list.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module#L11-L19)
- **Module/theme:** list
- **Implements:** [hook_help()](../../../../system/system.api.php/hook_help.md)

## Signature

```php
function list_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function list_help($path, $arg) {
  switch ($path) {
    case 'admin/help#list':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The List module defines various fields for storing a list of items, for use with the Field module. Usually these items are entered through a select list, checkboxes, or radio buttons. See the <a href="@field-help">Field module help page</a> for more information about fields.', array('@field-help' => url('admin/help/field'))) . '</p>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.module) · Licensed GPL-2.0-or-later (see LICENSE)._
