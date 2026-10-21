# ajax_test_render()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_test.module`](_file.md), lines 49–52 · [local source](../../../../../source/modules/simpletest/tests/ajax_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_test.module#L49-L52)
- **Module/theme:** batch_test

## Signature

```php
function ajax_test_render()
```

## Documentation

```text
Menu callback; Return an element suitable for use by ajax_deliver().

Additionally ensures that ajax_render() incorporates JavaScript settings
generated during the page request by invoking drupal_add_js() with a dummy
setting.
```

## Code

```php
function ajax_test_render() {
  drupal_add_js(array('ajax' => 'test'), 'setting');
  return array('#type' => 'ajax', '#commands' => array());
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
