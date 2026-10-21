# NodeTitleTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1982–1986 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1982-L1986)
- **Class:** [NodeTitleTestCase](../NodeTitleTestCase.md)
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
    $this->admin_user = $this->drupalCreateUser(array('administer nodes', 'create article content', 'create page content'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
