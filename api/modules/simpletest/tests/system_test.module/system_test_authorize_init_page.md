# system_test_authorize_init_page()

- **Type:** Function
- **File:** [`modules/simpletest/tests/system_test.module`](_file.md), lines 501–505 · [local source](../../../../../source/modules/simpletest/tests/system_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module#L501-L505)
- **Module/theme:** batch_test

## Signature

```php
function system_test_authorize_init_page($page_title)
```

## Documentation

```text
Page callback to initialize authorize.php during testing.

@see system_authorized_init().
```

## Code

```php
function system_test_authorize_init_page($page_title) {
  $authorize_url = $GLOBALS['base_url'] . '/authorize.php';
  system_authorized_init('system_test_authorize_run', drupal_get_path('module', 'system_test') . '/system_test.module', array(), $page_title);
  drupal_goto($authorize_url);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/system_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/system_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
