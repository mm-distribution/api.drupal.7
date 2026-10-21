# image_test_image_toolkits()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 11–22 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L11-L22)
- **Module/theme:** batch_test
- **Implements:** [hook_image_toolkits()](../../../system/system.api.php/hook_image_toolkits.md)

## Signature

```php
function image_test_image_toolkits()
```

## Documentation

```text
Implements hook_image_toolkits().
```

## Code

```php
function image_test_image_toolkits() {
  return array(
    'test' => array(
      'title' => t('A dummy toolkit that works'),
      'available' => TRUE,
    ),
    'broken' => array(
      'title' => t('A dummy toolkit that is "broken"'),
      'available' => FALSE,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
