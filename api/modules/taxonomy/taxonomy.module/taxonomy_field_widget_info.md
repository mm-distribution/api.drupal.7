# taxonomy_field_widget_info()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1469–1483 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1469-L1483)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_widget_info()](../../field/field.api.php/hook_field_widget_info.md)

## Signature

```php
function taxonomy_field_widget_info()
```

## Documentation

```text
Implements hook_field_widget_info().
```

## Code

```php
function taxonomy_field_widget_info() {
  return array(
    'taxonomy_autocomplete' => array(
      'label' => t('Autocomplete term widget (tagging)'),
      'field types' => array('taxonomy_term_reference'),
      'settings' => array(
        'size' => 60,
        'autocomplete_path' => 'taxonomy/autocomplete',
      ),
      'behaviors' => array(
        'multiple values' => FIELD_BEHAVIOR_CUSTOM,
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
