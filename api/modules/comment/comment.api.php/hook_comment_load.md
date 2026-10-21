# hook_comment_load()

- **Type:** Hook (documentation function)
- **File:** [`modules/comment/comment.api.php`](_file.md), lines 54–59 · [local source](../../../../source/modules/comment/comment.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php#L54-L59)
- **Module/theme:** comment
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_comment_load($comments)
```

## Documentation

```text
Comments are being loaded from the database.

@param $comments
 An array of comment objects indexed by cid.
```

## Code

```php
function hook_comment_load($comments) {
  $result = db_query('SELECT cid, foo FROM {mytable} WHERE cid IN (:cids)', array(':cids' => array_keys($comments)));
  foreach ($result as $record) {
    $comments[$record->cid]->foo = $record->foo;
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_comment_load()".

- [entity_crud_hook_test_comment_load()](../../simpletest/tests/entity_crud_hook_test.module/entity_crud_hook_test_comment_load.md) — `modules/simpletest/tests/entity_crud_hook_test.module`
- [rdf_comment_load()](../../rdf/rdf.module/rdf_comment_load.md) — `modules/rdf/rdf.module`

---
_Drupal 7.103 · [modules/comment/comment.api.php](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
