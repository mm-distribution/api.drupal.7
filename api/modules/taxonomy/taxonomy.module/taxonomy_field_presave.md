# taxonomy_field_presave()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1902–1911 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1902-L1911)
- **Module/theme:** taxonomy
- **Topics:** [taxonomy_index](../../../topics/taxonomy_index.md)
- **Implements:** [hook_field_presave()](../../field/field.api.php/hook_field_presave.md)

## Signature

```php
function taxonomy_field_presave($entity_type, $entity, $field, $instance, $langcode, &$items)
```

## Documentation

```text
Implements hook_field_presave().

Create any new terms defined in a freetagging vocabulary.
```

## Code

```php
function taxonomy_field_presave($entity_type, $entity, $field, $instance, $langcode, &$items) {
  foreach ($items as $delta => $item) {
    if ($item['tid'] === 'autocreate') {
      $term = (object) $item;
      unset($term->tid);
      taxonomy_term_save($term);
      $items[$delta]['tid'] = $term->tid;
    }
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
