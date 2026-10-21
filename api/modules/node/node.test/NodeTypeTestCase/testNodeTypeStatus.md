# NodeTypeTestCase::testNodeTypeStatus()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1594–1637 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1594-L1637)
- **Class:** [NodeTypeTestCase](../NodeTypeTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeTypeStatus()
```

## Documentation

```text
Tests that node_types_rebuild() correctly handles the 'disabled' flag.
```

## Code

```php
  function testNodeTypeStatus() {
    // Enable all core node modules, and all types should be active.
    module_enable(array('blog', 'book', 'poll'), FALSE);
    node_types_rebuild();
    $types = node_type_get_types();
    foreach (array('blog', 'book', 'poll', 'article', 'page') as $type) {
      $this->assertTrue(isset($types[$type]), format_string('%type is found in node types.', array('%type' => $type)));
      $this->assertTrue(isset($types[$type]->disabled) && empty($types[$type]->disabled), format_string('%type type is enabled.', array('%type' => $type)));
    }

    // Disable poll module and the respective type should be marked as disabled.
    module_disable(array('poll'), FALSE);
    node_types_rebuild();
    $types = node_type_get_types();
    $this->assertTrue(!empty($types['poll']->disabled), "Poll module's node type disabled.");
    $this->assertTrue(isset($types['blog']) && empty($types['blog']->disabled), "Blog module's node type still active.");

    // Disable blog module and the respective type should be marked as disabled.
    module_disable(array('blog'), FALSE);
    node_types_rebuild();
    $types = node_type_get_types();
    $this->assertTrue(!empty($types['blog']->disabled), "Blog module's node type disabled.");
    $this->assertTrue(!empty($types['poll']->disabled), "Poll module's node type still disabled.");

    // Disable book module and the respective type should still be active, since
    // it is not provided by hook_node_info().
    module_disable(array('book'), FALSE);
    node_types_rebuild();
    $types = node_type_get_types();
    $this->assertTrue(isset($types['book']) && empty($types['book']->disabled), "Book module's node type still active.");
    $this->assertTrue(!empty($types['blog']->disabled), "Blog module's node type still disabled.");
    $this->assertTrue(!empty($types['poll']->disabled), "Poll module's node type still disabled.");
    $this->assertTrue(isset($types['article']) && empty($types['article']->disabled), "Article node type still active.");
    $this->assertTrue(isset($types['page']) && empty($types['page']->disabled), "Basic page node type still active.");

    // Re-enable the modules and verify that the types are active again.
    module_enable(array('blog', 'book', 'poll'), FALSE);
    node_types_rebuild();
    $types = node_type_get_types();
    foreach (array('blog', 'book', 'poll', 'article', 'page') as $type) {
      $this->assertTrue(isset($types[$type]), format_string('%type is found in node types.', array('%type' => $type)));
      $this->assertTrue(isset($types[$type]->disabled) && empty($types[$type]->disabled), format_string('%type type is enabled.', array('%type' => $type)));
    }
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
