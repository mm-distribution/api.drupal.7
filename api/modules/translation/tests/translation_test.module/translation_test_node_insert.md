# translation_test_node_insert()

- **Type:** Function
- **File:** [`modules/translation/tests/translation_test.module`](_file.md), lines 11–13 · [local source](../../../../../source/modules/translation/tests/translation_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/tests/translation_test.module#L11-L13)
- **Module/theme:** translation_test
- **Implements:** [hook_node_insert()](../../../node/node.api.php/hook_node_insert.md)

## Signature

```php
function translation_test_node_insert($node)
```

## Documentation

```text
Implements hook_node_insert().
```

## Code

```php
function translation_test_node_insert($node) {
  drupal_write_record('node', $node, 'nid');
}
```

---
_Drupal 7.103 · [modules/translation/tests/translation_test.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/tests/translation_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
