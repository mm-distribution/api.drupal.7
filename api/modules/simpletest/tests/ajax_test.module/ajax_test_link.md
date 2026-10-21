# ajax_test_link()

- **Type:** Function
- **File:** [`modules/simpletest/tests/ajax_test.module`](_file.md), lines 68–78 · [local source](../../../../../source/modules/simpletest/tests/ajax_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_test.module#L68-L78)
- **Module/theme:** batch_test

## Signature

```php
function ajax_test_link()
```

## Documentation

```text
Menu callback; Renders a #type link with #ajax.
```

## Code

```php
function ajax_test_link() {
  $build['link'] = array(
    '#type' => 'link',
    '#title' => 'Show help',
    '#href' => 'filter/tips',
    '#ajax' => array(
      'wrapper' => 'block-system-main',
    ),
  );
  return $build;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
