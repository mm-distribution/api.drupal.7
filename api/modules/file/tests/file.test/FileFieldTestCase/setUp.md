# FileFieldTestCase::setUp()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 14–27 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L14-L27)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    // Since this is a base class for many test cases, support the same
    // flexibility that DrupalWebTestCase::setUp() has for the modules to be
    // passed in as either an array or a variable number of string arguments.
    $modules = func_get_args();
    if (isset($modules[0]) && is_array($modules[0])) {
      $modules = $modules[0];
    }
    $modules[] = 'file';
    $modules[] = 'file_module_test';
    parent::setUp($modules);
    $this->admin_user = $this->drupalCreateUser(array('access content', 'access administration pages', 'administer site configuration', 'administer users', 'administer permissions', 'administer content types', 'administer nodes', 'bypass node access', 'administer fields'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
