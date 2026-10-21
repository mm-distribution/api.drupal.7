# SearchNodeTagTest::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 2112–2119 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L2112-L2119)
- **Class:** [SearchNodeTagTest](../SearchNodeTagTest.md)
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
    parent::setUp('search', 'search_node_tags');
    node_access_rebuild();

    // Create a test user and log in.
    $this->test_user = $this->drupalCreateUser(array('search content'));
    $this->drupalLogin($this->test_user);
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
