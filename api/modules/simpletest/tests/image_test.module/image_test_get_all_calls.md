# image_test_get_all_calls()

- **Type:** Function
- **File:** [`modules/simpletest/tests/image_test.module`](_file.md), lines 52–54 · [local source](../../../../../source/modules/simpletest/tests/image_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module#L52-L54)
- **Module/theme:** batch_test

## Signature

```php
function image_test_get_all_calls()
```

## Documentation

```text
Get an array with the all the calls to the toolkits since image_test_reset()
was called.

@return
  An array keyed by operation name ('load', 'save', 'settings', 'resize',
  'rotate', 'crop', 'desaturate') with values being arrays of parameters
  passed to each call.
```

## Code

```php
function image_test_get_all_calls() {
  return variable_get('image_test_results', array());
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/image_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
