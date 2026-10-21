# trigger_taxonomy_term_update()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 611–613 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L611-L613)
- **Module/theme:** trigger
- **Implements:** [hook_taxonomy_term_update()](../../taxonomy/taxonomy.api.php/hook_taxonomy_term_update.md)

## Signature

```php
function trigger_taxonomy_term_update($term)
```

## Documentation

```text
Implements hook_taxonomy_term_update().
```

## Code

```php
function trigger_taxonomy_term_update($term) {
  _trigger_taxonomy('taxonomy_term_update', (array) $term);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
