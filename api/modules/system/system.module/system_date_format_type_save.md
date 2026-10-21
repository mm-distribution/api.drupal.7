# system_date_format_type_save()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3911–3924 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3911-L3924)
- **Module/theme:** system

## Signature

```php
function system_date_format_type_save($type)
```

## Documentation

```text
Saves a date type to the database.

@param $type
  A date type array containing the following keys:
  - type: The machine-readable name of the date type.
  - title: The human-readable name of the date type.
  - locked: A boolean indicating whether or not this date type should be
    configurable from the user interface.
  - is_new: A boolean indicating whether or not this date type is as of yet
    unsaved in the database.
```

## Code

```php
function system_date_format_type_save($type) {
  $info = array();
  $info['type'] = $type['type'];
  $info['title'] = $type['title'];
  $info['locked'] = $type['locked'];

  // Update date_format table.
  if (!empty($type['is_new'])) {
    drupal_write_record('date_format_type', $info);
  }
  else {
    drupal_write_record('date_format_type', $info, 'type');
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
