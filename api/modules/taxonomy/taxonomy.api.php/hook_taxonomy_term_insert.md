# hook_taxonomy_term_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 138–145 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L138-L145)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_term_insert($term)
```

## Documentation

```text
Act on taxonomy terms when inserted.

Modules implementing this hook can act on the term object when saved to
the database.

@param $term
  A taxonomy term object.
```

## Code

```php
function hook_taxonomy_term_insert($term) {
  db_insert('mytable')
    ->fields(array(
      'tid' => $term->tid,
      'foo' => $term->foo,
    ))
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_term_insert()".

- [entity_crud_hook_test_taxonomy_term_insert()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_taxonomy_term_insert.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [taxonomy_test_taxonomy_term_insert()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_taxonomy_term_insert.md) — `modules/simpletest/tests/taxonomy_test.module`
- [path_taxonomy_term_insert()](../../path/path.module/path_taxonomy_term_insert.md) — `modules/path/path.module`
- [trigger_taxonomy_term_insert()](../../trigger/trigger.module/trigger_taxonomy_term_insert.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
