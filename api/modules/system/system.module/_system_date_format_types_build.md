# _system_date_format_types_build()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3767–3810 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3767-L3810)
- **Module/theme:** system

## Signature

```php
function _system_date_format_types_build()
```

## Documentation

```text
Builds and returns information about available date types.

@return
  An associative array of date type information keyed by name. Each date type
  information array has the following elements:
  - type: The machine-readable name of the date type.
  - title: The human-readable name of the date type.
  - locked: A boolean indicating whether or not this date type should be
    configurable from the user interface.
  - module: The name of the module that defined this format in its
    hook_date_format_types(). An empty string if the format was user-defined.
  - is_new: A boolean indicating whether or not this date type is as of yet
    unsaved in the database.
```

## Code

```php
function _system_date_format_types_build() {
  $types = array();

  // Get list of modules that implement hook_date_format_types().
  $modules = module_implements('date_format_types');

  foreach ($modules as $module) {
    $module_types = module_invoke($module, 'date_format_types');
    foreach ($module_types as $module_type => $type_title) {
      $type = array();
      $type['module'] = $module;
      $type['type'] = $module_type;
      $type['title'] = $type_title;
      $type['locked'] = 1;
      // Will be over-ridden later if in the db.
      $type['is_new'] = TRUE;
      $types[$module_type] = $type;
    }
  }

  // Get custom formats added to the database by the end user.
  $result = db_query('SELECT dft.type, dft.title, dft.locked FROM {date_format_type} dft ORDER BY dft.title');
  foreach ($result as $record) {
    if (!isset($types[$record->type])) {
      $type = array();
      $type['is_new'] = FALSE;
      $type['module'] = '';
      $type['type'] = $record->type;
      $type['title'] = $record->title;
      $type['locked'] = $record->locked;
      $types[$record->type] = $type;
    }
    else {
      $type = array();
      $type['is_new'] = FALSE;  // Over-riding previous setting.
      $types[$record->type] = array_merge($types[$record->type], $type);
    }
  }

  // Allow other modules to modify these date types.
  drupal_alter('date_format_types', $types);

  return $types;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
