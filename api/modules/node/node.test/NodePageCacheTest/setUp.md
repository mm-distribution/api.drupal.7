# NodePageCacheTest::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 3039–3050 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L3039-L3050)
- **Class:** [NodePageCacheTest](../NodePageCacheTest.md)
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

    variable_set('cache', 1);
    variable_set('page_cache_maximum_age', 300);

    $this->admin_user = $this->drupalCreateUser(array(
        'bypass node access',
        'access content overview',
        'administer nodes',
    ));
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
