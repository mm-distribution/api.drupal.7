# NodeAccessRebuildTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1772–1778 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1772-L1778)
- **Class:** [NodeAccessRebuildTestCase](../NodeAccessRebuildTestCase.md)
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

    $web_user = $this->drupalCreateUser(array('administer site configuration', 'access administration pages', 'access site reports'));
    $this->drupalLogin($web_user);
    $this->web_user = $web_user;
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
