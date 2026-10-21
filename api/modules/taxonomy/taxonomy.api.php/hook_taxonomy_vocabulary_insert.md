# hook_taxonomy_vocabulary_insert()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 54–58 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L54-L58)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_vocabulary_insert($vocabulary)
```

## Documentation

```text
Act on taxonomy vocabularies when inserted.

Modules implementing this hook can act on the vocabulary object when saved
to the database.

@param $vocabulary
  A taxonomy vocabulary object.
```

## Code

```php
function hook_taxonomy_vocabulary_insert($vocabulary) {
  if ($vocabulary->machine_name == 'my_vocabulary') {
    $vocabulary->weight = 100;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_vocabulary_insert()".

- [entity_crud_hook_test_taxonomy_vocabulary_insert()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_taxonomy_vocabulary_insert.md) — `modules/simpletest/tests/entity_crud_hook_test.module`

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
