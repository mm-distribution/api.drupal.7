# hook_taxonomy_term_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 155–160 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L155-L160)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_term_update($term)
```

## Documentation

```text
Act on taxonomy terms when updated.

Modules implementing this hook can act on the term object when updated.

@param $term
  A taxonomy term object.
```

## Code

```php
function hook_taxonomy_term_update($term) {
  db_update('mytable')
    ->fields(array('foo' => $term->foo))
    ->condition('tid', $term->tid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_term_update()".

- [entity_crud_hook_test_taxonomy_term_update()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_taxonomy_term_update.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [taxonomy_test_taxonomy_term_update()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_taxonomy_term_update.md) — `modules/simpletest/tests/taxonomy_test.module`
- [path_taxonomy_term_update()](../../path/path.module/path_taxonomy_term_update.md) — `modules/path/path.module`
- [trigger_taxonomy_term_update()](../../trigger/trigger.module/trigger_taxonomy_term_update.md) — `modules/trigger/trigger.module`

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
