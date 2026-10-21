# GraphUnitTest::assertReversePaths()

- **Type:** Method
- **File:** [`modules/simpletest/tests/graph.test`](../_file.md), lines 131–138 · [local source](../../../../../../source/modules/simpletest/tests/graph.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test#L131-L138)
- **Class:** [GraphUnitTest](../GraphUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function assertReversePaths($graph, $expected_reverse_paths)
```

## Documentation

```text
Verify expected reverse paths in a graph.

@param $graph
  A graph array processed by drupal_depth_first_search().
@param $expected_reverse_paths
  An associative array containing vertices with their expected reverse
  paths.
```

## Code

```php
  function assertReversePaths($graph, $expected_reverse_paths) {
    foreach ($expected_reverse_paths as $vertex => $paths) {
      // Build an array with keys = $paths and values = TRUE.
      $expected = array_fill_keys($paths, TRUE);
      $result = isset($graph[$vertex]['reverse_paths']) ? $graph[$vertex]['reverse_paths'] : array();
      $this->assertEqual($expected, $result, format_string('Expected reverse paths for vertex @vertex: @expected-paths, got @paths', array('@vertex' => $vertex, '@expected-paths' => $this->displayArray($expected, TRUE), '@paths' => $this->displayArray($result, TRUE))));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/graph.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/graph.test) · Licensed GPL-2.0-or-later (see LICENSE)._
