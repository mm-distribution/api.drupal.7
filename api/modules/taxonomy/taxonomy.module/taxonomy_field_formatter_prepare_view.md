# taxonomy_field_formatter_prepare_view()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1674–1716 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1674-L1716)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_formatter_prepare_view()](../../field/field.api.php/hook_field_formatter_prepare_view.md)

## Signature

```php
function taxonomy_field_formatter_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items, $displays)
```

## Documentation

```text
Implements hook_field_formatter_prepare_view().

This preloads all taxonomy terms for multiple loaded objects at once and
unsets values for invalid terms that do not exist.
```

## Code

```php
function taxonomy_field_formatter_prepare_view($entity_type, $entities, $field, $instances, $langcode, &$items, $displays) {
  $tids = array();

  // Collect every possible term attached to any of the fieldable entities.
  foreach ($entities as $id => $entity) {
    foreach ($items[$id] as $delta => $item) {
      // Force the array key to prevent duplicates.
      if ($item['tid'] !== 'autocreate') {
        $tids[$item['tid']] = $item['tid'];
      }
    }
  }
  if ($tids) {
    $terms = taxonomy_term_load_multiple(array_filter($tids));

    // Iterate through the fieldable entities again to attach the loaded term data.
    foreach ($entities as $id => $entity) {
      $rekey = FALSE;

      foreach ($items[$id] as $delta => $item) {
        // Check whether the taxonomy term field instance value could be loaded.
        if (isset($terms[$item['tid']])) {
          // Replace the instance value with the term data.
          $items[$id][$delta]['taxonomy_term'] = $terms[$item['tid']];
        }
        // Terms to be created are not in $terms, but are still legitimate.
        elseif ($item['tid'] === 'autocreate') {
          // Leave the item in place.
        }
        // Otherwise, unset the instance value, since the term does not exist.
        else {
          unset($items[$id][$delta]);
          $rekey = TRUE;
        }
      }

      if ($rekey) {
        // Rekey the items array.
        $items[$id] = array_values($items[$id]);
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
