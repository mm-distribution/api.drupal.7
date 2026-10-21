# NodeSaveTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1331–1337 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1331-L1337)
- **Class:** [NodeSaveTestCase](../NodeSaveTestCase.md)
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
    parent::setUp('node_test');
    // Create a user that is allowed to post; we'll use this to test the submission.
    $web_user = $this->drupalCreateUser(array('create article content'));
    $this->drupalLogin($web_user);
    $this->web_user = $web_user;
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
