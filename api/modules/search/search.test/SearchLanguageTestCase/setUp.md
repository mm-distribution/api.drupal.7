# SearchLanguageTestCase::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1993–1999 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1993-L1999)
- **Class:** [SearchLanguageTestCase](../SearchLanguageTestCase.md)
- **Module/theme:** search

## Signature

```php
function setUp()
```

## Documentation

```text
Implementation setUp().
```

## Code

```php
  function setUp() {
    parent::setUp('search', 'locale');

    // Create and login user.
    $test_user = $this->drupalCreateUser(array('access content', 'search content', 'use advanced search', 'administer nodes', 'administer languages', 'access administration pages'));
    $this->drupalLogin($test_user);
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
