# trigger_taxonomy_term_insert()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 604–606 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L604-L606)
- **Module/theme:** trigger
- **Implements:** [hook_taxonomy_term_insert()](../../taxonomy/taxonomy.api.php/hook_taxonomy_term_insert.md)

## Signature

```php
function trigger_taxonomy_term_insert($term)
```

## Documentation

```text
Implements hook_taxonomy_term_insert().
```

## Code

```php
function trigger_taxonomy_term_insert($term) {
  _trigger_taxonomy('taxonomy_term_insert', (array) $term);
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
