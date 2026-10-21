# path_test_path_update()

- **Type:** Function
- **File:** [`modules/simpletest/tests/path_test.module`](_file.md), lines 18–22 · [local source](../../../../../source/modules/simpletest/tests/path_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path_test.module#L18-L22)
- **Module/theme:** batch_test
- **Implements:** [hook_path_update()](../../../path/path.api.php/hook_path_update.md)

## Signature

```php
function path_test_path_update($path)
```

## Documentation

```text
Implements hook_path_update().
```

## Code

```php
function path_test_path_update($path) {
  $results = variable_get('path_test_results', array());
  $results['hook_path_update'] = $path;
  variable_set('path_test_results', $results);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/path_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
