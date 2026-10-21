# FilterFormatAccessTestCase::setUp()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 481–522 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L481-L522)
- **Class:** [FilterFormatAccessTestCase](../FilterFormatAccessTestCase.md)
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

    // Create a user who can administer text formats, but does not have
    // specific permission to use any of them.
    $this->filter_admin_user = $this->drupalCreateUser(array(
      'administer filters',
      'create page content',
      'edit any page content',
    ));

    // Create two text formats.
    $this->drupalLogin($this->filter_admin_user);
    $formats = array();
    for ($i = 0; $i < 2; $i++) {
      $edit = array(
        'format' => drupal_strtolower($this->randomName()),
        'name' => $this->randomName(),
      );
      $this->drupalPost('admin/config/content/formats/add', $edit, t('Save configuration'));
      $this->resetFilterCaches();
      $formats[] = filter_format_load($edit['format']);
    }
    list($this->allowed_format, $this->disallowed_format) = $formats;
    $this->drupalLogout();

    // Create a regular user with access to one of the formats.
    $this->web_user = $this->drupalCreateUser(array(
      'create page content',
      'edit any page content',
      filter_permission_name($this->allowed_format),
    ));

    // Create an administrative user who has access to use both formats.
    $this->admin_user = $this->drupalCreateUser(array(
      'administer filters',
      'create page content',
      'edit any page content',
      filter_permission_name($this->allowed_format),
      filter_permission_name($this->disallowed_format),
    ));
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
