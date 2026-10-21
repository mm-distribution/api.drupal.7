# TaxonomyQueryAlterTestCase::assertQueryTagTestResult()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 2213–2217 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L2213-L2217)
- **Class:** [TaxonomyQueryAlterTestCase](../TaxonomyQueryAlterTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
protected function assertQueryTagTestResult($expected_invocations, $method)
```

## Documentation

```text
Verifies invocation of the hooks in the test module.

@param int $expected_invocations
  The number of times the hooks are expected to have been invoked.
@param string $method
  A string describing the invoked function which generated the query.
```

## Code

```php
  protected function assertQueryTagTestResult($expected_invocations, $method) {
    $this->assertIdentical($expected_invocations, variable_get('taxonomy_test_query_alter'), 'hook_query_alter() invoked when executing ' . $method);
    $this->assertIdentical($expected_invocations, variable_get('taxonomy_test_query_term_access_alter'), 'Deprecated hook_query_term_access_alter() invoked when executing ' . $method);
    $this->assertIdentical($expected_invocations, variable_get('taxonomy_test_query_taxonomy_term_access_alter'), 'Preferred hook_query_taxonomy_term_access_alter() invoked when executing ' . $method);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
