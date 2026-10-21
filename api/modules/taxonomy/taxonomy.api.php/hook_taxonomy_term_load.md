# hook_taxonomy_term_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 106–114 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L106-L114)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_term_load($terms)
```

## Documentation

```text
Act on taxonomy terms when loaded.

Modules implementing this hook can act on the term objects returned by
taxonomy_term_load_multiple().

For performance reasons, information to be added to term objects should be
loaded in a single query for all terms where possible.

Since terms are stored and retrieved from cache during a page request, avoid
altering properties provided by the {taxonomy_term_data} table, since this
may affect the way results are loaded from cache in subsequent calls.

@param $terms
  An array of term objects, indexed by tid.
```

## Code

```php
function hook_taxonomy_term_load($terms) {
  $result = db_select('mytable', 'm')
    ->fields('m', array('tid', 'foo'))
    ->condition('m.tid', array_keys($terms), 'IN')
    ->execute();
  foreach ($result as $record) {
    $terms[$record->tid]->foo = $record->foo;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_term_load()".

- [entity_crud_hook_test_taxonomy_term_load()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_taxonomy_term_load.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [taxonomy_test_taxonomy_term_load()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_taxonomy_term_load.md) — `modules/simpletest/tests/taxonomy_test.module`

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
