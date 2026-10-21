# MenuRouterTestCase::testMaintenanceModeLoginPaths()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 226–235 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L226-L235)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testMaintenanceModeLoginPaths()
```

## Documentation

```text
Make sure the maintenance mode can be bypassed using hook_menu_site_status_alter().

@see hook_menu_site_status_alter().
```

## Code

```php
  function testMaintenanceModeLoginPaths() {
    variable_set('maintenance_mode', TRUE);

    $offline_message = t('@site is currently under maintenance. We should be back shortly. Thank you for your patience.', array('@site' => variable_get('site_name', 'Drupal')));
    $this->drupalLogout();
    $this->drupalGet('node');
    $this->assertText($offline_message);
    $this->drupalGet('menu_login_callback');
    $this->assertText('This is menu_login_callback().', t('Maintenance mode can be bypassed through hook_login_paths().'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
