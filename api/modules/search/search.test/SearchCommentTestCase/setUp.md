# SearchCommentTestCase::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 768–784 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L768-L784)
- **Class:** [SearchCommentTestCase](../SearchCommentTestCase.md)
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
    parent::setUp('comment', 'search');

    // Create and log in an administrative user having access to the Full HTML
    // text format.
    $full_html_format = filter_format_load('full_html');
    $permissions = array(
      'administer filters',
      filter_permission_name($full_html_format),
      'administer permissions',
      'create page content',
      'skip comment approval',
      'access comments',
    );
    $this->admin_user = $this->drupalCreateUser($permissions);
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
