# MenuBreadcrumbTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 1056–1079 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L1056-L1079)
- **Class:** [MenuBreadcrumbTestCase](../MenuBreadcrumbTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    $modules = func_get_args();
    if (isset($modules[0]) && is_array($modules[0])) {
      $modules = $modules[0];
    }
    $modules[] = 'menu_test';
    parent::setUp($modules);
    $perms = array_keys(module_invoke_all('permission'));
    $this->admin_user = $this->drupalCreateUser($perms);
    $this->drupalLogin($this->admin_user);

    // This test puts menu links in the Navigation menu and then tests for
    // their presence on the page, so we need to ensure that the Navigation
    // block will be displayed in all active themes.
    db_update('block')
      ->fields(array(
        // Use a region that is valid for all themes.
        'region' => 'content',
        'status' => 1,
      ))
      ->condition('module', 'system')
      ->condition('delta', 'navigation')
      ->execute();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
