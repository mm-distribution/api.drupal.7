# NodeQueryAlter::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2278–2293 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2278-L2293)
- **Class:** [NodeQueryAlter](../NodeQueryAlter.md)
- **Module/theme:** node

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('node_access_test');
    node_access_rebuild();

    // Create some content.
    $this->drupalCreateNode();
    $this->drupalCreateNode();
    $this->drupalCreateNode();
    $this->drupalCreateNode();

    // Create user with simple node access permission. The 'node test view'
    // permission is implemented and granted by the node_access_test module.
    $this->accessUser = $this->drupalCreateUser(array('access content overview', 'access content', 'node test view'));
    $this->noAccessUser = $this->drupalCreateUser(array('access content overview', 'access content'));
    $this->noAccessUser2 = $this->drupalCreateUser(array('access content overview', 'access content'));
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
