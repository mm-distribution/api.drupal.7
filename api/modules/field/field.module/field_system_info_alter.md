# field_system_info_alter()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 366–395 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L366-L395)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)
- **Implements:** [hook_system_info_alter()](../../system/system.api.php/hook_system_info_alter.md)

## Signature

```php
function field_system_info_alter(&$info, $file, $type)
```

## Documentation

```text
Implements hook_system_info_alter().

Goes through a list of all modules that provide a field type, and makes them
required if there are any active fields of that type.
```

## Code

```php
function field_system_info_alter(&$info, $file, $type) {
  if ($type == 'module' && module_hook($file->name, 'field_info')) {
    $fields = field_read_fields(array('module' => $file->name), array('include_deleted' => TRUE));
    if ($fields) {
      $info['required'] = TRUE;

      // Provide an explanation message (only mention pending deletions if there
      // remains no actual, non-deleted fields)
      $non_deleted = FALSE;
      foreach ($fields as $field) {
        if (empty($field['deleted'])) {
          $non_deleted = TRUE;
          break;
        }
      }
      if ($non_deleted) {
        if (module_exists('field_ui')) {
          $explanation = t('Field type(s) in use - see <a href="@fields-page">Field list</a>', array('@fields-page' => url('admin/reports/fields')));
        }
        else {
          $explanation = t('Fields type(s) in use');
        }
      }
      else {
        $explanation = t('Fields pending deletion');
      }
      $info['explanation'] = $explanation;
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
