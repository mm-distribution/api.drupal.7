# theme_test_theme()

- **Type:** Function
- **File:** [`modules/simpletest/tests/theme_test.module`](_file.md), lines 6–21 · [local source](../../../../../source/modules/simpletest/tests/theme_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module#L6-L21)
- **Module/theme:** batch_test
- **Implements:** [hook_theme()](../../../system/system.api.php/hook_theme.md)

## Signature

```php
function theme_test_theme($existing, $type, $theme, $path)
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function theme_test_theme($existing, $type, $theme, $path) {
  $items['theme_test'] = array(
    'file' => 'theme_test.inc',
    'variables' => array('foo' => ''),
  );
  $items['theme_test_template_test'] = array(
    'template' => 'theme_test.template_test',
  );
  $items['theme_test_template_test_2'] = array(
    'template' => 'theme_test.template_test',
  );
  $items['theme_test_foo'] = array(
    'variables' => array('foo' => NULL),
  );
  return $items;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
