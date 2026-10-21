# SearchPageOverride::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1958–1968 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1958-L1968)
- **Class:** [SearchPageOverride](../SearchPageOverride.md)
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
    parent::setUp('search', 'search_extra_type');

    // Login as a user that can create and search content.
    $this->search_user = $this->drupalCreateUser(array('search content', 'administer search'));
    $this->drupalLogin($this->search_user);

    // Enable the extra type module for searching.
    variable_set('search_active_modules', array('node' => 'node', 'user' => 'user', 'search_extra_type' => 'search_extra_type'));
    menu_rebuild();
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
