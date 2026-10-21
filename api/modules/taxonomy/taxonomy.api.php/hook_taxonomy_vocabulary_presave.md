# hook_taxonomy_vocabulary_presave()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 41–43 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L41-L43)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_vocabulary_presave($vocabulary)
```

## Documentation

```text
Act on taxonomy vocabularies before they are saved.

Modules implementing this hook can act on the vocabulary object before it is
inserted or updated.

@param $vocabulary
  A taxonomy vocabulary object.
```

## Code

```php
function hook_taxonomy_vocabulary_presave($vocabulary) {
  $vocabulary->foo = 'bar';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_vocabulary_presave()".

- [entity_crud_hook_test_taxonomy_vocabulary_presave()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_taxonomy_vocabulary_presave.md) — `modules/simpletest/tests/entity_crud_hook_test.module`

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
