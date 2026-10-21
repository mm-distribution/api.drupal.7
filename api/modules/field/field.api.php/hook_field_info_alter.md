# hook_field_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 196–208 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L196-L208)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_types](../../../topics/field_types.md)

## Signature

```php
function hook_field_info_alter(&$info)
```

## Documentation

```text
Perform alterations on Field API field types.

@param $info
  Array of information on field types exposed by hook_field_info()
  implementations.
```

## Code

```php
function hook_field_info_alter(&$info) {
  // Add a setting to all field types.
  foreach ($info as $field_type => $field_type_info) {
    $info[$field_type]['settings'] += array(
      'mymodule_additional_setting' => 'default value',
    );
  }

  // Change the default widget for fields of type 'foo'.
  if (isset($info['foo'])) {
    $info['foo']['default widget'] = 'mymodule_widget';
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_info_alter()".

- [user_field_info_alter()](../../user/user.module/user_field_info_alter.md) — `modules/user/user.module`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
