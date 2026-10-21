# NodeTypeTestCase::testNodeTypeGetFunctions()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1494–1506 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1494-L1506)
- **Class:** [NodeTypeTestCase](../NodeTypeTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeTypeGetFunctions()
```

## Documentation

```text
Ensures that node type functions (node_type_get_*) work correctly.

Load available node types and validate the returned data.
```

## Code

```php
  function testNodeTypeGetFunctions() {
    $node_types = node_type_get_types();
    $node_names = node_type_get_names();

    $this->assertTrue(isset($node_types['article']), 'Node type article is available.');
    $this->assertTrue(isset($node_types['page']), 'Node type basic page is available.');

    $this->assertEqual($node_types['article']->name, $node_names['article'], 'Correct node type base has been returned.');

    $this->assertEqual($node_types['article'], node_type_get_type('article'), 'Correct node type has been returned.');
    $this->assertEqual($node_types['article']->name, node_type_get_name('article'), 'Correct node type name has been returned.');
    $this->assertEqual($node_types['page']->base, node_type_get_base('page'), 'Correct node type base has been returned.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
