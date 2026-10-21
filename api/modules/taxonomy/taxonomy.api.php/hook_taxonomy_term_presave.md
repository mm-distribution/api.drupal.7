# hook_taxonomy_term_presave()

- **Type:** Hook (documentation function)
- **File:** [`modules/taxonomy/taxonomy.api.php`](_file.md), lines 125–127 · [local source](../../../../source/modules/taxonomy/taxonomy.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php#L125-L127)
- **Module/theme:** taxonomy
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_taxonomy_term_presave($term)
```

## Documentation

```text
Act on taxonomy terms before they are saved.

Modules implementing this hook can act on the term object before it is
inserted or updated.

@param $term
  A term object.
```

## Code

```php
function hook_taxonomy_term_presave($term) {
  $term->foo = 'bar';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_taxonomy_term_presave()".

- [entity_crud_hook_test_taxonomy_term_presave()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_taxonomy_term_presave.md) — `modules/simpletest/tests/entity_crud_hook_test.module`

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.api.php](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
