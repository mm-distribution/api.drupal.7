# NodeLoadMultipleTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 41–45 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L41-L45)
- **Class:** [NodeLoadMultipleTestCase](../NodeLoadMultipleTestCase.md)
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
    parent::setUp();
    $web_user = $this->drupalCreateUser(array('create article content', 'create page content'));
    $this->drupalLogin($web_user);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
