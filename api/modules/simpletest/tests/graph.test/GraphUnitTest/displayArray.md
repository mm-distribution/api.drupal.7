# GraphUnitTest::displayArray()

- **Type:** Method
- **File:** [`modules/simpletest/tests/graph.test`](../_file.md), lines 186–193 · [local source](../../../../../../source/modules/simpletest/tests/graph.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test#L186-L193)
- **Class:** [GraphUnitTest](../GraphUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function displayArray($paths, $keys = FALSE)
```

## Documentation

```text
Helper function to output vertices as comma-separated list.

@param $paths
  An array containing a list of vertices.
@param $keys
  (optional) Whether to output the keys of $paths instead of the values.
```

## Code

```php
  function displayArray($paths, $keys = FALSE) {
    if (!empty($paths)) {
      return implode(', ', $keys ? array_keys($paths) : $paths);
    }
    else {
      return '(empty)';
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/graph.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test) · Licensed GPL-2.0-or-later (see LICENSE)._
