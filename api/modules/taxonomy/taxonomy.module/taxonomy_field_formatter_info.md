# taxonomy_field_formatter_info()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1573–1588 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1573-L1588)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_formatter_info()](../../field/field.api.php/hook_field_formatter_info.md)

## Signature

```php
function taxonomy_field_formatter_info()
```

## Documentation

```text
Implements hook_field_formatter_info().
```

## Code

```php
function taxonomy_field_formatter_info() {
  return array(
    'taxonomy_term_reference_link' => array(
      'label' => t('Link'),
      'field types' => array('taxonomy_term_reference'),
    ),
    'taxonomy_term_reference_plain' => array(
      'label' => t('Plain text'),
      'field types' => array('taxonomy_term_reference'),
    ),
    'taxonomy_term_reference_rss_category' => array(
      'label' => t('RSS category'),
      'field types' => array('taxonomy_term_reference'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
