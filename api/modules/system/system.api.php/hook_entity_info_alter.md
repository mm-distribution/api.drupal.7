# hook_entity_info_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 285–289 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L285-L289)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_entity_info_alter(&$entity_info)
```

## Documentation

```text
Alter the entity info.

Modules may implement this hook to alter the information that defines an
entity. All properties that are available in hook_entity_info() can be
altered here.

@param $entity_info
  The entity info array, keyed by entity name.

@see hook_entity_info()
```

## Code

```php
function hook_entity_info_alter(&$entity_info) {
  // Set the controller class for nodes to an alternate implementation of the
  // DrupalEntityController interface.
  $entity_info['node']['controller class'] = 'MyCustomNodeController';
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_entity_info_alter()".

- [entity_crud_hook_test_entity_info_alter()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_entity_info_alter.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [book_entity_info_alter()](../../book/book.module/book_entity_info_alter.md) — `modules/book/book.module`
- [field_test_entity_info_alter()](../../field/tests/field_test.entity.inc/field_test_entity_info_alter.md) — `modules/field/tests/field_test.entity.inc`
- [forum_entity_info_alter()](../../forum/forum.module/forum_entity_info_alter.md) — `modules/forum/forum.module`
- [locale_entity_info_alter()](../../locale/locale.module/locale_entity_info_alter.md) — `modules/locale/locale.module`
- [rdf_entity_info_alter()](../../rdf/rdf.module/rdf_entity_info_alter.md) — `modules/rdf/rdf.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
