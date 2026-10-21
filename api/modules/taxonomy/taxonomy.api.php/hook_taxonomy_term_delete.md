# hook_taxonomy_term_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 171–175 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L171-L175)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_term_delete($term)
```

## Documentation

```text
Respond to the deletion of taxonomy terms.

Modules implementing this hook can respond to the deletion of taxonomy
terms from the database.

@param $term
  A taxonomy term object.
```

## Code

```php
function hook_taxonomy_term_delete($term) {
  db_delete('mytable')
    ->condition('tid', $term->tid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_term_delete()".

- [entity_crud_hook_test_taxonomy_term_delete()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_taxonomy_term_delete.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [taxonomy_test_taxonomy_term_delete()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_taxonomy_term_delete.md) — `modules/simpletest/tests/taxonomy_test.module`
- [forum_taxonomy_term_delete()](../../forum/forum.module/forum_taxonomy_term_delete.md) — `modules/forum/forum.module`
- [path_taxonomy_term_delete()](../../path/path.module/path_taxonomy_term_delete.md) — `modules/path/path.module`
- [taxonomy_taxonomy_term_delete()](../taxonomy.module/taxonomy_taxonomy_term_delete.md) — `modules/taxonomy/taxonomy.module`
- [trigger_taxonomy_term_delete()](../../trigger/trigger.module/trigger_taxonomy_term_delete.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
