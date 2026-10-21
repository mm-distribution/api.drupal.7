# _image_test_log_call()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 68–72 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L68-L72)
- **Module/theme:** batch_test

## Signature

```php
function _image_test_log_call($op, $args)
```

## Documentation

```text
Store the values passed to a toolkit call.

@param $op
  One of the image toolkit operations: 'get_info', 'load', 'save',
  'settings', 'resize', 'rotate', 'crop', 'desaturate'.
@param $args
  Values passed to hook.

@see image_test_get_all_calls()
@see image_test_reset()
```

## Code

```php
function _image_test_log_call($op, $args) {
  $results = variable_get('image_test_results', array());
  $results[$op][] = $args;
  variable_set('image_test_results', $results);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
