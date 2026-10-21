# PageViewTestCase::testPageView()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 723–747 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L723-L747)
- **Class:** [PageViewTestCase](../PageViewTestCase.md)
- **Module/theme:** node

## Signature

```php
function testPageView()
```

## Documentation

```text
Tests an anonymous and unpermissioned user attempting to edit the node.
```

## Code

```php
  function testPageView() {
    // Create a node to view.
    $node = $this->drupalCreateNode();
    $this->assertTrue(node_load($node->nid), 'Node created.');

    // Try to edit with anonymous user.
    $html = $this->drupalGet("node/$node->nid/edit");
    $this->assertResponse(403);

    // Create a user without permission to edit node.
    $web_user = $this->drupalCreateUser(array('access content'));
    $this->drupalLogin($web_user);

    // Attempt to access edit page.
    $this->drupalGet("node/$node->nid/edit");
    $this->assertResponse(403);

    // Create user with permission to edit node.
    $web_user = $this->drupalCreateUser(array('bypass node access'));
    $this->drupalLogin($web_user);

    // Attempt to access edit page.
    $this->drupalGet("node/$node->nid/edit");
    $this->assertResponse(200);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
