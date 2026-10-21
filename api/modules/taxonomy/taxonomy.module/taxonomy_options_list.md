# taxonomy_options_list()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1496–1499 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1496-L1499)
- **Module/theme:** taxonomy
- **Implements:** [hook_options_list()](../../field/modules/options/options.api.php/hook_options_list.md)

## Signature

```php
function taxonomy_options_list($field, $instance, $entity_type, $entity)
```

## Documentation

```text
Implements hook_options_list().
```

## Code

```php
function taxonomy_options_list($field, $instance, $entity_type, $entity) {
  $function = !empty($field['settings']['options_list_callback']) ? $field['settings']['options_list_callback'] : 'taxonomy_allowed_values';
  return $function($field);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
