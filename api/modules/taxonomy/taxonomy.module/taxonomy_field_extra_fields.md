# taxonomy_field_extra_fields()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 154–182 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L154-L182)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_extra_fields()](../../field/field.api.php/hook_field_extra_fields.md)

## Signature

```php
function taxonomy_field_extra_fields()
```

## Documentation

```text
Implements hook_field_extra_fields().
```

## Code

```php
function taxonomy_field_extra_fields() {
  $return = array();
  $info = entity_get_info('taxonomy_term');
  foreach (array_keys($info['bundles']) as $bundle) {
    $return['taxonomy_term'][$bundle] = array(
      'form' => array(
        'name' => array(
          'label' => t('Name'),
          'description' => t('Term name textfield'),
          'weight' => -5,
        ),
        'description' => array(
          'label' => t('Description'),
          'description' => t('Term description textarea'),
          'weight' => 0,
        ),
      ),
      'display' => array(
        'description' => array(
          'label' => t('Description'),
          'description' => t('Term description'),
          'weight' => 0,
        ),
      ),
    );
  }

  return $return;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
