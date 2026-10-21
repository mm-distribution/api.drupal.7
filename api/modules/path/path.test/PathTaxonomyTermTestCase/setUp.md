# PathTaxonomyTermTestCase::setUp()

- **Type:** Method
- **File:** [`modules/path/path.test`](../_file.md), lines 285–291 · [local source](../../../../../source/modules/path/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test#L285-L291)
- **Class:** [PathTaxonomyTermTestCase](../PathTaxonomyTermTestCase.md)
- **Module/theme:** path

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('path', 'taxonomy');

    // Create and login user.
    $web_user = $this->drupalCreateUser(array('administer url aliases', 'administer taxonomy', 'access administration pages'));
    $this->drupalLogin($web_user);
  }
```

---
_Drupal 7.103 · [modules/path/path.test](https://github.com/drupal/drupal/blob/7.103/modules/path/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
