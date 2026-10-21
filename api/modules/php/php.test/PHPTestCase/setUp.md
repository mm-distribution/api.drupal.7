# PHPTestCase::setUp()

- **Type:** Method
- **File:** [`modules/php/php.test`](../_file.md), lines 14–38 · [local source](../../../../../source/modules/php/php.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test#L14-L38)
- **Class:** [PHPTestCase](../PHPTestCase.md)
- **Module/theme:** php

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('php');

    // Create and login admin user.
    $admin_user = $this->drupalCreateUser(array('administer filters'));
    $this->drupalLogin($admin_user);

    // Verify that the PHP code text format was inserted.
    $php_format_id = 'php_code';
    $this->php_code_format = filter_format_load($php_format_id);
    $this->assertEqual($this->php_code_format->name, 'PHP code', 'PHP code text format was created.');

    // Verify that the format has the PHP code filter enabled.
    $filters = filter_list_format($php_format_id);
    $this->assertTrue($filters['php_code']->status, 'PHP code filter is enabled.');

    // Verify that the format exists on the administration page.
    $this->drupalGet('admin/config/content/formats');
    $this->assertText('PHP code', 'PHP code text format was created.');

    // Verify that anonymous and authenticated user roles do not have access.
    $this->drupalGet('admin/config/content/formats/' . $php_format_id);
    $this->assertFieldByName('roles[' . DRUPAL_ANONYMOUS_RID . ']', FALSE, 'Anonymous users do not have access to PHP code format.');
    $this->assertFieldByName('roles[' . DRUPAL_AUTHENTICATED_RID . ']', FALSE, 'Authenticated users do not have access to PHP code format.');
  }
```

---
_Drupal 7.103 · [modules/php/php.test](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test) · Licensed GPL-2.0-or-later (see LICENSE)._
