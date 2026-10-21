# trigger_taxonomy_term_delete()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 618–620 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L618-L620)
- **Module/theme:** trigger
- **Implements:** [hook_taxonomy_term_delete()](../../taxonomy/taxonomy.api.php/hook_taxonomy_term_delete.md)

## Signature

```php
function trigger_taxonomy_term_delete($term)
```

## Documentation

```text
Implements hook_taxonomy_term_delete().
```

## Code

```php
function trigger_taxonomy_term_delete($term) {
  _trigger_taxonomy('taxonomy_term_delete', (array) $term);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
