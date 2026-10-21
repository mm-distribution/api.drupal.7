# NodeAccessTestCase::testNodeAccess()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1039–1070 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1039-L1070)
- **Class:** [NodeAccessTestCase](../NodeAccessTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeAccess()
```

## Documentation

```text
Runs basic tests for node_access function.
```

## Code

```php
  function testNodeAccess() {
    // Ensures user without 'access content' permission can do nothing.
    $web_user1 = $this->drupalCreateUser(array('create page content', 'edit any page content', 'delete any page content'));
    $node1 = $this->drupalCreateNode(array('type' => 'page'));
    $this->assertNodeAccess(array('create' => FALSE), 'page', $web_user1);
    $this->assertNodeAccess(array('view' => FALSE, 'update' => FALSE, 'delete' => FALSE), $node1, $web_user1);

    // Ensures user with 'bypass node access' permission can do everything.
    $web_user2 = $this->drupalCreateUser(array('bypass node access'));
    $node2 = $this->drupalCreateNode(array('type' => 'page'));
    $this->assertNodeAccess(array('create' => TRUE), 'page', $web_user2);
    $this->assertNodeAccess(array('view' => TRUE, 'update' => TRUE, 'delete' => TRUE), $node2, $web_user2);

    // User cannot 'view own unpublished content'.
    $web_user3 = $this->drupalCreateUser(array('access content'));
    $node3 = $this->drupalCreateNode(array('status' => 0, 'uid' => $web_user3->uid));
    $this->assertNodeAccess(array('view' => FALSE), $node3, $web_user3);

    // User cannot create content without permission.
    $this->assertNodeAccess(array('create' => FALSE), 'page', $web_user3);

    // User can 'view own unpublished content', but another user cannot.
    $web_user4 = $this->drupalCreateUser(array('access content', 'view own unpublished content'));
    $web_user5 = $this->drupalCreateUser(array('access content', 'view own unpublished content'));
    $node4 = $this->drupalCreateNode(array('status' => 0, 'uid' => $web_user4->uid));
    $this->assertNodeAccess(array('view' => TRUE, 'update' => FALSE), $node4, $web_user4);
    $this->assertNodeAccess(array('view' => FALSE), $node4, $web_user5);

    // Tests the default access provided for a published node.
    $node5 = $this->drupalCreateNode();
    $this->assertNodeAccess(array('view' => TRUE, 'update' => FALSE, 'delete' => FALSE), $node5, $web_user3);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
