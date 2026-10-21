# FilterAdminTestCase::setUp()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 187–201 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L187-L201)
- **Class:** [FilterAdminTestCase](../FilterAdminTestCase.md)
- **Module/theme:** filter

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

    // Create users.
    $filtered_html_format = filter_format_load('filtered_html');
    $full_html_format = filter_format_load('full_html');
    $this->admin_user = $this->drupalCreateUser(array(
      'administer filters',
      filter_permission_name($filtered_html_format),
      filter_permission_name($full_html_format),
    ));

    $this->web_user = $this->drupalCreateUser(array('create page content', 'edit own page content'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
