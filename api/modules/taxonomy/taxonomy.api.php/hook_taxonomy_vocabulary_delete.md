# hook_taxonomy_vocabulary_delete()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 84–88 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L84-L88)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_vocabulary_delete($vocabulary)
```

## Documentation

```text
Respond to the deletion of taxonomy vocabularies.

Modules implementing this hook can respond to the deletion of taxonomy
vocabularies from the database.

@param $vocabulary
  A taxonomy vocabulary object.
```

## Code

```php
function hook_taxonomy_vocabulary_delete($vocabulary) {
  db_delete('mytable')
    ->condition('vid', $vocabulary->vid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_vocabulary_delete()".

- [entity_crud_hook_test_taxonomy_vocabulary_delete()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_taxonomy_vocabulary_delete.md) — `modules/simpletest/tests/entity_crud_hook_test.module`

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
