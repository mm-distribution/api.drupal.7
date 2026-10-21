# DrupalMatchPathTestCase::testDrupalMatchPath()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 38–47 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L38-L47)
- **Class:** [DrupalMatchPathTestCase](../DrupalMatchPathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalMatchPath()
```

## Documentation

```text
Run through our test cases, making sure each one works as expected.
```

## Code

```php
  function testDrupalMatchPath() {
    // Set up our test cases.
    $tests = $this->drupalMatchPathTests();
    foreach ($tests as $patterns => $cases) {
      foreach ($cases as $path => $expected_result) {
        $actual_result = drupal_match_path($path, $patterns);
        $this->assertIdentical($actual_result, $expected_result, format_string('Tried matching the path <code>@path</code> to the pattern <pre>@patterns</pre> - expected @expected, got @actual.', array('@path' => $path, '@patterns' => $patterns, '@expected' => var_export($expected_result, TRUE), '@actual' => var_export($actual_result, TRUE))));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
