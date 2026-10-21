# MenuRouterTestCase::testThemeCallbackMaintenanceMode()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 205–219 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L205-L219)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testThemeCallbackMaintenanceMode()
```

## Documentation

```text
Test the theme callback when the site is in maintenance mode.
```

## Code

```php
  function testThemeCallbackMaintenanceMode() {
    variable_set('maintenance_mode', TRUE);

    // For a regular user, the fact that the site is in maintenance mode means
    // we expect the theme callback system to be bypassed entirely.
    $this->drupalGet('menu-test/theme-callback/use-admin-theme');
    $this->assertRaw('bartik/css/style.css', "The maintenance theme's CSS appears on the page.");

    // An administrator, however, should continue to see the requested theme.
    $admin_user = $this->drupalCreateUser(array('access site in maintenance mode'));
    $this->drupalLogin($admin_user);
    $this->drupalGet('menu-test/theme-callback/use-admin-theme');
    $this->assertText('Custom theme: seven. Actual theme: seven.', 'The theme callback system is correctly triggered for an administrator when the site is in maintenance mode.');
    $this->assertRaw('seven/style.css', "The administrative theme's CSS appears on the page.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
