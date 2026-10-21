# taxonomy_taxonomy_vocabulary_update()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 531–551 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L531-L551)
- **Module/theme:** taxonomy
- **Implements:** [hook_taxonomy_vocabulary_update()](../taxonomy.api.php/hook_taxonomy_vocabulary_update.md)

## Signature

```php
function taxonomy_taxonomy_vocabulary_update($vocabulary)
```

## Documentation

```text
Implements hook_taxonomy_vocabulary_update().
```

## Code

```php
function taxonomy_taxonomy_vocabulary_update($vocabulary) {
  // Reflect machine name changes in the definitions of existing 'taxonomy'
  // fields.
  if (!empty($vocabulary->old_machine_name) && $vocabulary->old_machine_name != $vocabulary->machine_name) {
    $fields = field_read_fields();
    foreach ($fields as $field_name => $field) {
      $update = FALSE;
      if ($field['type'] == 'taxonomy_term_reference') {
        foreach ($field['settings']['allowed_values'] as $key => &$value) {
          if ($value['vocabulary'] == $vocabulary->old_machine_name) {
            $value['vocabulary'] = $vocabulary->machine_name;
            $update = TRUE;
          }
        }
        if ($update) {
          field_update_field($field);
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
