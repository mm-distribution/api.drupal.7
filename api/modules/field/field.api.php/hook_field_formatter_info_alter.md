# hook_field_formatter_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1130–1138 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1130-L1138)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_formatter](../../../topics/field_formatter.md)

## Signature

```php
function hook_field_formatter_info_alter(&$info)
```

## Documentation

```text
Perform alterations on Field API formatter types.

@param $info
  An array of information on formatter types exposed by
  hook_field_formatter_info() implementations.
```

## Code

```php
function hook_field_formatter_info_alter(&$info) {
  // Add a setting to a formatter type.
  $info['text_default']['settings'] += array(
    'mymodule_additional_setting' => 'default value',
  );

  // Let a new field type re-use an existing formatter.
  $info['text_default']['field types'][] = 'my_field_type';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_formatter_info_alter()".

_None found._

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
