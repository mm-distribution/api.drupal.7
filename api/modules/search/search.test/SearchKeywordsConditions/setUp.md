# SearchKeywordsConditions::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1232–1241 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1232-L1241)
- **Class:** [SearchKeywordsConditions](../SearchKeywordsConditions.md)
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
    // Create searching user.
    $this->searching_user = $this->drupalCreateUser(array('search content', 'access content', 'access comments', 'skip comment approval'));
    // Login with sufficient privileges.
    $this->drupalLogin($this->searching_user);
    // Test with all search modules enabled.
    variable_set('search_active_modules', array('node' => 'node', 'user' => 'user', 'search_extra_type' => 'search_extra_type'));
    menu_rebuild();
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
