# NodeAccessPagerTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2778–2782 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2778-L2782)
- **Class:** [NodeAccessPagerTestCase](../NodeAccessPagerTestCase.md)
- **Module/theme:** node

## Signature

```php
public function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  public function setUp() {
    parent::setUp('node_access_test', 'comment', 'forum');
    node_access_rebuild();
    $this->web_user = $this->drupalCreateUser(array('access content', 'access comments', 'node test view'));
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
