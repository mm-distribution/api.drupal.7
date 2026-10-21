# NodeRSSContentTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 952–961 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L952-L961)
- **Class:** [NodeRSSContentTestCase](../NodeRSSContentTestCase.md)
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
    // Enable dummy module that implements hook_node_view.
    parent::setUp('node_test');

    // Use bypass node access permission here, because the test class uses
    // hook_grants_alter() to deny access to everyone on node_access
    // queries.
    $user = $this->drupalCreateUser(array('bypass node access', 'access content', 'create article content'));
    $this->drupalLogin($user);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
