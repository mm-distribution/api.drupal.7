# DrupalTestCase::verbose()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 507–516 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L507-L516)
- **Class:** [DrupalTestCase](../DrupalTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function verbose($message)
```

## Documentation

```text
Logs a verbose message in a text file.

The link to the verbose message will be placed in the test results as a
passing assertion with the text '[verbose message]'.

@param $message
  The verbose message to be stored.

@see simpletest_verbose()
```

## Code

```php
  protected function verbose($message) {
    if ($id = simpletest_verbose($message)) {
      $class_safe = str_replace('\\', '_', get_class($this));
      $url = $this->verboseDirectoryUrl . '/' . $class_safe . '-' . $id . '.html';
      // Not using l() to avoid invoking the theme system, so that unit tests
      // can use verbose() as well.
      $link = '<a href="' . $url . '" target="_blank">' . t('Verbose message') . '</a>';
      $this->error($link, 'User notice');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
