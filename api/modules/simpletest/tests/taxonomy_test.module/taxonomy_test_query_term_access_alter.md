# taxonomy_test_query_term_access_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.module`](_file.md), lines 126–131 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module#L126-L131)
- **Module/theme:** batch_test
- **Implements:** [hook_query_TAG_alter()](../../../system/system.api.php/hook_query_TAG_alter.md)

## Signature

```php
function taxonomy_test_query_term_access_alter(QueryAlterableInterface $query)
```

## Documentation

```text
Implements hook_query_TAG_alter().
```

## Code

```php
function taxonomy_test_query_term_access_alter(QueryAlterableInterface $query) {
  $value = variable_get(__FUNCTION__);
  if (isset($value)) {
    variable_set(__FUNCTION__, ++$value);
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
