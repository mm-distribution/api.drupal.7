# EntityCrudHookTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.test`](_file.md), lines 19–338 · [local source](../../../../../source/modules/simpletest/tests/entity_crud_hook_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test#L19-L338)
- **Module/theme:** batch_test

## Signature

```php
class EntityCrudHookTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests invocation of hooks when performing an action.

Tested hooks are:
- hook_entity_insert()
- hook_entity_load()
- hook_entity_update()
- hook_entity_delete()
As well as all type-specific hooks, like hook_node_insert(),
hook_comment_update(), etc.
```

## Properties

### $ids

```php
protected $ids = array();
```

## Methods (derived index)

- [getInfo()](EntityCrudHookTestCase/getInfo.md)
- [setUp()](EntityCrudHookTestCase/setUp.md)
- [assertHookMessage()](EntityCrudHookTestCase/assertHookMessage.md) — Pass if the message $text was set by one of the CRUD hooks in entity_crud_hook_test.module, i.e., if the $text is an element of $_SESSION['entity_crud_hook_test'].
- [testCommentHooks()](EntityCrudHookTestCase/testCommentHooks.md) — Tests hook invocations for CRUD operations on comments.
- [testFileHooks()](EntityCrudHookTestCase/testFileHooks.md) — Tests hook invocations for CRUD operations on files.
- [testNodeHooks()](EntityCrudHookTestCase/testNodeHooks.md) — Tests hook invocations for CRUD operations on nodes.
- [testTaxonomyTermHooks()](EntityCrudHookTestCase/testTaxonomyTermHooks.md) — Tests hook invocations for CRUD operations on taxonomy terms.
- [testTaxonomyVocabularyHooks()](EntityCrudHookTestCase/testTaxonomyVocabularyHooks.md) — Tests hook invocations for CRUD operations on taxonomy vocabularies.
- [testUserHooks()](EntityCrudHookTestCase/testUserHooks.md) — Tests hook invocations for CRUD operations on users.

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
