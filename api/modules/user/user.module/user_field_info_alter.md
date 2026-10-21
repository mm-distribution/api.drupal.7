# user_field_info_alter()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 201–209 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L201-L209)
- **Module/theme:** user
- **Implements:** [hook_field_info_alter()](../../field/field.api.php/hook_field_info_alter.md)

## Signature

```php
function user_field_info_alter(&$info)
```

## Documentation

```text
Implements hook_field_info_alter().
```

## Code

```php
function user_field_info_alter(&$info) {
  // Add the 'user_register_form' instance setting to all field types.
  foreach ($info as $field_type => &$field_type_info) {
    $field_type_info += array('instance_settings' => array());
    $field_type_info['instance_settings'] += array(
      'user_register_form' => FALSE,
    );
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
