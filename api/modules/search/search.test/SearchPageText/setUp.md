# SearchPageText::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 260–265 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L260-L265)
- **Class:** [SearchPageText](../SearchPageText.md)
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
    parent::setUp('search');

    // Create user.
    $this->searching_user = $this->drupalCreateUser(array('search content', 'access user profiles'));
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
