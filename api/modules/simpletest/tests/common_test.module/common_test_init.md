# common_test_init()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 104–111 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L104-L111)
- **Module/theme:** batch_test
- **Implements:** [hook_init()](../../../system/system.api.php/hook_init.md)

## Signature

```php
function common_test_init()
```

## Documentation

```text
Implements hook_init().
```

## Code

```php
function common_test_init() {
  if (variable_get('common_test_redirect_current_path', FALSE)) {
    drupal_goto(current_path());
  }
  if (variable_get('common_test_link_to_current_path', FALSE)) {
    drupal_set_message(l('link which should point to the current path', current_path()));
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
