# SearchNodeAccessTest::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 2057–2064 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L2057-L2064)
- **Class:** [SearchNodeAccessTest](../SearchNodeAccessTest.md)
- **Module/theme:** search

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('search', 'node_access_test');
    node_access_rebuild();

    // Create a test user and log in.
    $this->test_user = $this->drupalCreateUser(array('access content', 'search content', 'use advanced search'));
    $this->drupalLogin($this->test_user);
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
