# DrupalWebTestCase::assertThemeOutput()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3568–3580 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3568-L3580)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertThemeOutput($callback, array $variables, $expected, $message = '', $group = 'Other')
```

## Documentation

```text
Asserts themed output.

@param $callback
  The name of the theme function to invoke; e.g. 'links' for theme_links().
@param $variables
  An array of variables to pass to the theme function.
@param $expected
  The expected themed output string.
@param $message
  (optional) A message to display with the assertion. Do not translate
  messages: use format_string() to embed variables in the message text, not
  t(). If left blank, a default message will be displayed.
@param $group
  (optional) The group this message is in, which is displayed in a column
  in test output. Use 'Debug' to indicate this is debugging output. Do not
  translate this string. Defaults to 'Other'; most tests do not override
  this default.

@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertThemeOutput($callback, array $variables, $expected, $message = '', $group = 'Other') {
    $output = theme($callback, $variables);
    $this->verbose('Variables:' . '<pre>' .  check_plain(var_export($variables, TRUE)) . '</pre>'
      . '<hr />' . 'Result:' . '<pre>' .  check_plain(var_export($output, TRUE)) . '</pre>'
      . '<hr />' . 'Expected:' . '<pre>' .  check_plain(var_export($expected, TRUE)) . '</pre>'
      . '<hr />' . $output
    );
    if (!$message) {
      $message = '%callback rendered correctly.';
    }
    $message = format_string($message, array('%callback' => 'theme_' . $callback . '()'));
    return $this->assertIdentical($output, $expected, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
