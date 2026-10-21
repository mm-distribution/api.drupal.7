# taxonomy_field_info()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1447–1464 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1447-L1464)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_info()](../../field/field.api.php/hook_field_info.md)

## Signature

```php
function taxonomy_field_info()
```

## Documentation

```text
Implements hook_field_info().

Field settings:
- allowed_values: a list array of one or more vocabulary trees:
  - vocabulary: a vocabulary machine name.
  - parent: a term ID of a term whose children are allowed. This should be
    '0' if all terms in a vocabulary are allowed. The allowed values do not
    include the parent term.
```

## Code

```php
function taxonomy_field_info() {
  return array(
    'taxonomy_term_reference' => array(
      'label' => t('Term reference'),
      'description' => t('This field stores a reference to a taxonomy term.'),
      'default_widget' => 'options_select',
      'default_formatter' => 'taxonomy_term_reference_link',
      'settings' => array(
        'allowed_values' => array(
          array(
            'vocabulary' => '',
            'parent' => '0',
          ),
        ),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
