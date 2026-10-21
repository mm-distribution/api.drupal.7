# form_test_two_instances()

- **Type:** Function
- **File:** [`modules/simpletest/tests/form_test.module`](_file.md), lines 1921–1933 · [local source](../../../../../source/modules/simpletest/tests/form_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module#L1921-L1933)
- **Module/theme:** batch_test

## Signature

```php
function form_test_two_instances()
```

## Documentation

```text
Menu callback that returns two instances of the node form.
```

## Code

```php
function form_test_two_instances() {
  global $user;
  $node1 = (object) array(
    'uid' => $user->uid,
    'name' => (isset($user->name) ? $user->name : ''),
    'type' => 'page',
    'language' => LANGUAGE_NONE,
  );
  $node2 = clone($node1);
  $return['node_form_1'] = drupal_get_form('page_node_form', $node1);
  $return['node_form_2'] = drupal_get_form('page_node_form', $node2);
  return $return;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/form_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
