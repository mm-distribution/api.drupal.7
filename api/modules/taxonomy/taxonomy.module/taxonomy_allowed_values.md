# taxonomy_allowed_values()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1654–1666 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1654-L1666)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_allowed_values($field)
```

## Documentation

```text
Returns the set of valid terms for a taxonomy field.

@param $field
  The field definition.
@return
  The array of valid terms for this field, keyed by term id.
```

## Code

```php
function taxonomy_allowed_values($field) {
  $options = array();
  foreach ($field['settings']['allowed_values'] as $tree) {
    if ($vocabulary = taxonomy_vocabulary_machine_name_load($tree['vocabulary'])) {
      if ($terms = taxonomy_get_tree($vocabulary->vid, $tree['parent'])) {
        foreach ($terms as $term) {
          $options[$term->tid] = str_repeat('-', $term->depth) . $term->name;
        }
      }
    }
  }
  return $options;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
