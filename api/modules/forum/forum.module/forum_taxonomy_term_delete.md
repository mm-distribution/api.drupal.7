# forum_taxonomy_term_delete()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 476–484 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L476-L484)
- **Module/theme:** forum
- **Implements:** [hook_taxonomy_term_delete()](../../taxonomy/taxonomy.api.php/hook_taxonomy_term_delete.md)

## Signature

```php
function forum_taxonomy_term_delete($term)
```

## Documentation

```text
Implements hook_taxonomy_term_delete().
```

## Code

```php
function forum_taxonomy_term_delete($term) {
  // For containers, remove the tid from the forum_containers variable.
  $containers = variable_get('forum_containers', array());
  $key = array_search($term->tid, $containers);
  if ($key !== FALSE) {
    unset($containers[$key]);
  }
  variable_set('forum_containers', $containers);
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
