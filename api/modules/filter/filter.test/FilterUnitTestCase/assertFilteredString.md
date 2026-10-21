# FilterUnitTestCase::assertFilteredString()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1595–1622 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1595-L1622)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
function assertFilteredString($filter, $tests)
```

## Documentation

```text
Asserts multiple filter output expectations for multiple input strings.

@param $filter
  A input filter object.
@param $tests
  An associative array, whereas each key is an arbitrary input string and
  each value is again an associative array whose keys are filter output
  strings and whose values are Booleans indicating whether the output is
  expected or not.

For example:
@code
$tests = array(
  'Input string' => array(
    '<p>Input string</p>' => TRUE,
    'Input string<br' => FALSE,
  ),
);
@endcode
```

## Code

```php
  function assertFilteredString($filter, $tests) {
    foreach ($tests as $source => $tasks) {
      $function = $filter->callback;
      $result = $function($source, $filter);
      foreach ($tasks as $value => $is_expected) {
        // Not using assertIdentical, since combination with strpos() is hard to grok.
        if ($is_expected) {
          $success = $this->assertTrue(strpos($result, $value) !== FALSE, format_string('@source: @value found.', array(
            '@source' => var_export($source, TRUE),
            '@value' => var_export($value, TRUE),
          )));
        }
        else {
          $success = $this->assertTrue(strpos($result, $value) === FALSE, format_string('@source: @value not found.', array(
            '@source' => var_export($source, TRUE),
            '@value' => var_export($value, TRUE),
          )));
        }
        if (!$success) {
          $this->verbose('Source:<pre>' . check_plain(var_export($source, TRUE)) . '</pre>'
            . '<hr />' . 'Result:<pre>' . check_plain(var_export($result, TRUE)) . '</pre>'
            . '<hr />' . ($is_expected ? 'Expected:' : 'Not expected:')
            . '<pre>' . check_plain(var_export($value, TRUE)) . '</pre>'
          );
        }
      }
    }
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
