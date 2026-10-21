# hook_taxonomy_vocabulary_update()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 68–73 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L68-L73)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_vocabulary_update($vocabulary)
```

## Documentation

```text
Act on taxonomy vocabularies when updated.

Modules implementing this hook can act on the vocabulary object when updated.

@param $vocabulary
  A taxonomy vocabulary object.
```

## Code

```php
function hook_taxonomy_vocabulary_update($vocabulary) {
  db_update('mytable')
    ->fields(array('foo' => $vocabulary->foo))
    ->condition('vid', $vocabulary->vid)
    ->execute();
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_vocabulary_update()".

- [entity_crud_hook_test_taxonomy_vocabulary_update()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_taxonomy_vocabulary_update.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [taxonomy_taxonomy_vocabulary_update()](../taxonomy.module/taxonomy_taxonomy_vocabulary_update.md) — `modules/taxonomy/taxonomy.module`

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
