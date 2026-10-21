# NodeBlockFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2058–2064 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2058-L2064)
- **Class:** [NodeBlockFunctionalTest](../NodeBlockFunctionalTest.md)
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
    parent::setUp('node', 'block');

    // Create users and test node.
    $this->admin_user = $this->drupalCreateUser(array('administer content types', 'administer nodes', 'administer blocks'));
    $this->web_user = $this->drupalCreateUser(array('access content', 'create article content'));
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
