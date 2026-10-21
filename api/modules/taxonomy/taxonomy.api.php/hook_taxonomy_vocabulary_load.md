# hook_taxonomy_vocabulary_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 22–30 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L22-L30)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_vocabulary_load($vocabularies)
```

## Documentation

```text
Act on taxonomy vocabularies when loaded.

Modules implementing this hook can act on the vocabulary objects before they
are returned by taxonomy_vocabulary_load_multiple().

@param $vocabulary
  An array of taxonomy vocabulary objects.
```

## Code

```php
function hook_taxonomy_vocabulary_load($vocabularies) {
  $result = db_select('mytable', 'm')
    ->fields('m', array('vid', 'foo'))
    ->condition('m.vid', array_keys($vocabularies), 'IN')
    ->execute();
  foreach ($result as $record) {
    $vocabularies[$record->vid]->foo = $record->foo;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_vocabulary_load()".

- [entity_crud_hook_test_taxonomy_vocabulary_load()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_taxonomy_vocabulary_load.md) — `modules/simpletest/tests/entity_crud_hook_test.module`

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
